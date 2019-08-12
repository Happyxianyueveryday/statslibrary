import numpy as np
import os, sys
import math 

class TreeNode:
    '''
    : TreeNode: 决策树的结点类
    '''
    def __init__(self, _val='', _feature='', _label='', _isleaf=True):
        '''
        : __init__: 初始化决策树的结点
        : param _val: 若当前结点为非叶子结点，则表示当前非叶子结点所表示的特征的值
        : type _val: str
        : param _feature: 若当前结点为非叶子结点，则表示当前非叶子结点所选择的特征名称
        : type _feature: str
        : param _label: 若当前结点为叶子结点，则表示当前叶子结点最终所属的类别标签
        : type _label: str
        : param _isleaf: 若当前结点为非叶子结点，则值为True；否则值为false
        : type _isleaf: bool
        '''
        self.isleaf=_isleaf
        self.child=[] 
        
        if self.isleaf:
            self.label=_label 
        else:
            self.val=_val
            self.feature=_feature


    def print(self):
        print('----------------------------')
        print('是否叶子结点: ', self.isleaf)
        if self.isleaf:
            print('当前叶子结点的类别标签为: ', self.label)
        else:
            print('当前结点的特征标准为: ', self.feature)
            print('当前结点的特征值为: ', self.val)
        print('----------------------------')

    
    
class EleDecisionTree:
    '''
    : EleDecisionTree: 使用id3和c4.5算法构造的决策树
    '''
    def __init__(self):
        '''
        : __init__: 初始化函数
        '''
        self.root=None


    def cal_gross(self, data, label):
        '''
        : note: private method
        : __cal_gross: 计算各个特征中的信息增益
        : param data: 训练集样本特征向量组成的矩阵
        : type data: np.array
        : param label: 训练集样本特征向量的标签，例如label[0]就是训练集样本特征向量data[0]的类别标签
        : type label: list[str]
        : return: 各个特征的信息增益值
        : rtype: np.array
        '''
        # 1. 计算原始数据集D中的经验熵H(D)
        hD=0                     # 经验熵hD
        label_set=set(label)                  
        label_count={}           # 各个类别样本的数量

        for x in label_set:
            label_count[x]=label.count(x)

        for x in label_set:
            hD-=(label_count[x]/len(label))*math.log(label_count[x]/len(label), 2)

        # 2. 计算各个特征A对数据集D的经验条件熵hDA
        features_count=np.shape(data)[1]        # 特征数
        samples_count=np.shape(data)[0]         # 样本数
        
        hDA=[0.0 for i in range(features_count)]   # 各个特征对数据集D的经验条件熵

        for i in range(features_count):
            features_set=set(data[:,i])                               # 当前特征的取值集合
            features_analy={}                                         # 各个特征取值的样本对应的标签的样本数，每行代表一个特征的取值，每列代表样本的标签
            features_value_set={}                                     # 各个特征取值的总数
            
            for m in features_set:
                features_value_set[m]=0
                for n in label_set:
                    features_analy[m+'+'+n]=0

            for k in range(samples_count):
                features_value_set[data[k][i]]+=1
                features_analy[str(data[k][i])+'+'+str(label[k])]+=1

            for r in features_set:
                temp=0
                for x in features_analy.keys():
                    if x.split('+')[0]==r and features_analy[x]!=0 and features_value_set[x.split('+')[0]]!=0:
                        dik_di=float(features_analy[x])/float(features_value_set[r.split('+')[0]])
                        temp+=(dik_di)*math.log(dik_di, 2)
                hDA[i]-=(features_value_set[r]/samples_count)*temp

            res=np.add(hD, -np.array(hDA))
        
        return res


    def train_id3(self, data, label, threshold, lis):
        '''
        : train_id3: 使用id3算法对训练集进行训练，得到决策树
        : param data: 训练集样本特征向量组成的矩阵
        : type data: np.array
        : param label: 训练集样本特征向量的标签，例如label[0]就是训练集样本特征向量data[0]的类别标签
        : type label: np.array
        : param threshold: 设定的阈值
        : param lis: 各个特征对应的名称
        : type lis: list[str]
        : type threshold: float
        '''
        self.root=self.__real_id3(data, label, lis)
    

    def __real_id3(self, data, label, lis):
        '''
        : note: private methods
        : __real_id3: 递归实现的id3算法构建决策树
        : param data: 训练集样本特征向量组成的矩阵
        : type data: np.array
        : param label: 训练集样本特征向量的标签，例如label[0]就是训练集样本特征向量data[0]的类别标签
        : type label: np.array
        : param lis: 各个特征对应的名称
        : type lis: list[str]
        : return: 递归构建的决策树的根结点
        : rtype: TreeNode
        '''
        # 0. 判断特征数量是否为0，若为0则递归结束
        if np.shape(data)[0]==0 or np.shape(data)[1]==0 or len(lis)==0:
            return None

        # 1. 若所有的样本都属于一类，则直接返回一个单结点树
        if len(set(label))==1:
            return TreeNode(_isleaf=True, _label=label[0])

        # 2. 计算各个特征的信息增益
        gross=self.cal_gross(data, label).tolist()

        # 2. 选出最大的信息增益的对应特征，并计算该特征中出现最高次数的值
        index=gross.index(max(gross))
        feature_name=lis[index]

        feature_val_count={}
        for i in range(np.shape(data)[0]):
            if data[i][index] in feature_val_count.keys():
                feature_val_count[data[i][index]]+=1
            else:
                feature_val_count[data[i][index]]=1

        # 3. 创建当前结点
        max_count, max_val=max(zip(feature_val_count.values(), feature_val_count.keys()))
        root=TreeNode(_isleaf=False, _val=max_val, _feature=feature_name)
        # root.print()

        # 4. 依次递归创建当前结点的子结点
        for x in set(data[:,index]):
            temp_data=[]
            temp_label=[]
            temp_lis=[]
            
            for i in range(np.shape(data)[0]):   # 根据样本在最大增益的特征的取值划分为多个集合分别进行递归
                if data[i][index]==x:
                    temp_data.append(data[i])
                    temp_label.append(label[i])

            for x in lis:
                if x!=feature_name:
                    temp_lis.append(x)
            
            temp_data=np.array(temp_data)
            temp_data=np.delete(temp_data, index, axis = 1)
            # print(temp_lis)
            # print(temp_label)
            # print(temp_data)

            child=self.__real_id3(temp_data, temp_label, temp_lis)

            if child:
                root.child.append(child)

        return root


    def cal_gross_ratio(self, data, label):
        '''
        : note: private method
        : __cal_gross: 计算各个特征中的信息增益比
        : param data: 训练集样本特征向量组成的矩阵
        : type data: np.array
        : param label: 训练集样本特征向量的标签，例如label[0]就是训练集样本特征向量data[0]的类别标签
        : type label: list[str]
        : return: 各个特征的信息增益比
        : rtype: np.array
        '''
        # 1. 计算原始数据集D中的经验熵H(D)
        hD=0                     # 经验熵hD 
        label_set=set(label)                  
        label_count={}           # 各个类别样本的数量

        for x in label_set:
            label_count[x]=label.count(x)

        for x in label_set:
            hD-=(label_count[x]/len(label))*math.log(label_count[x]/len(label), 2)
        
        # 2. 计算信息增益比
        gross=self.cal_gross(data, label)
        gross=np.divide(gross, hD)

        return gross
    
    def train_c45(self, data, label, threshold, lis):
        '''
        : train_c45: 使用c4.5算法对训练集进行训练，得到决策树
        : note: c4.5算法和id3算法基本一致，只是每次选择特征时，换用了信息增益比而非信息增益
        : param data: 训练集样本特征向量组成的矩阵
        : type data: np.array
        : param label: 训练集样本特征向量的标签，例如label[0]就是训练集样本特征向量data[0]的类别标签
        : type label: np.array
        : param threshold: 设定的阈值
        : param lis: 各个特征对应的名称
        : type lis: list[str]
        : type threshold: float
        '''
        self.root=self.__real_c45(data, label, lis)


    def __real_c45(self, data, label, lis):
        '''
        : note: private methods
        : __real_id3: 递归实现的id3算法构建决策树
        : param data: 训练集样本特征向量组成的矩阵
        : type data: np.array
        : param label: 训练集样本特征向量的标签，例如label[0]就是训练集样本特征向量data[0]的类别标签
        : type label: np.array
        : param lis: 各个特征对应的名称
        : type lis: list[str]
        : return: 递归构建的决策树的根结点
        : rtype: TreeNode
        '''
        # 0. 判断特征数量是否为0，若为0则递归结束
        if np.shape(data)[0]==0 or np.shape(data)[1]==0 or len(lis)==0:
            return None

        # 1. 若所有的样本都属于一类，则直接返回一个单结点树
        if len(set(label))==1:
            return TreeNode(_isleaf=True, _label=label[0])

        # 2. 计算各个特征的信息增益
        gross=self.cal_gross_ratio(data, label).tolist()

        # 2. 选出最大的信息增益的对应特征，并计算该特征中出现最高次数的值
        index=gross.index(max(gross))
        feature_name=lis[index]

        feature_val_count={}
        for i in range(np.shape(data)[0]):
            if data[i][index] in feature_val_count.keys():
                feature_val_count[data[i][index]]+=1
            else:
                feature_val_count[data[i][index]]=1

        # 3. 创建当前结点
        max_count, max_val=max(zip(feature_val_count.values(), feature_val_count.keys()))
        root=TreeNode(_isleaf=False, _val=max_val, _feature=feature_name)
        # root.print()

        # 4. 依次递归创建当前结点的子结点
        for x in set(data[:,index]):
            temp_data=[]
            temp_label=[]
            temp_lis=[]
            
            for i in range(np.shape(data)[0]):   # 根据样本在最大增益的特征的取值划分为多个集合分别进行递归
                if data[i][index]==x:
                    temp_data.append(data[i])
                    temp_label.append(label[i])

            for x in lis:
                if x!=feature_name:
                    temp_lis.append(x)
            
            temp_data=np.array(temp_data)
            temp_data=np.delete(temp_data, index, axis = 1)
            # print(temp_lis)
            # print(temp_label)
            # print(temp_data)

            child=self.__real_c45(temp_data, temp_label, temp_lis)

            if child:
                root.child.append(child)

        return root
    

    def print(self):
        '''
        : print: 按层次遍历输出当前决策树
        '''
        if not self.root:
            return

        que=[]
        que.append(self.root)
        
        while len(que):
            now=que[0]

            if now:
                now.print()
            
            que.pop(0)
            
            for x in now.child:
                if x:
                    que.append(x)
        





