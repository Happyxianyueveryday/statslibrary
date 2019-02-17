import numpy as np

class BayesDiscri:

    def __init__(self):
        '''
        :__init__: 初始化BayesDiscri类
        '''
        self.varipro=[]   # 各个特征xk在各个类别yi下的条件概率
        self.priorpro={}  # 各个类别yi的先验概率
        self.respro=[]    # 测试集中每个样本向量属于各个类别的概率

    def train(self, data, rowvar=False):
        '''
        :train: 使用训练集进行训练
        :param data: 训练数据集矩阵，矩阵元素可以是数字或者表示特征取值的字符串，其最后一行或者最后一列为样本的类别标签，训练数据集矩阵至少有两个样本和两个特征
        :type data: np.array
        :param rowvar: 指定每行或者每列代表一个变量；rowvar=True指定每行作为一个变量，每列作为一个样本向量；rowvar=False指定每列作为一个变量，每行作为一个样本向量。默认值为rowvar=False
        :type rowvar: bool
        '''
        # 1. 首先训练集矩阵统一转换为rowvar=False的情况，即每行为一个样本向量
        if rowvar==True:
            data=data.T

        # 2. 计算各个类别yi的先验概率，最后一列为样本标签
        size=np.shape(data)[0]    # 样本数量
        count=np.shape(data)[1]   # 特征数量

        dic={}
        for i in range(size):
            if data[i][count-1] in dic.keys():
                dic[str(data[i][count-1])]+=1
            else:
                dic[str(data[i][count-1])]=1
        
        for i in dic.keys():
            dic[i]/=size
        
        self.priorpro=dic

        # 3. 计算各个特征xk在各个类别yi下的条件概率
        for i in range(count-1):
            dic={}
            for k in range(size):
                temp=str(data[k][i])+'|'+str(data[k][count-1])    # dic的标签形式为: 特征取值+'|'+类别标签，表示条件概率p(特征取值|类别标签)
                if temp in dic.keys():
                    dic[temp]+=1
                else:
                    dic[temp]=1
            for k in dic.keys():
                kind=k.split('|')[1]                           # 抽取类别标签
                dic[k]/=data[:,count-1].tolist().count(kind)   # 统计类别标签的数目
            self.varipro.append(dic)
        
        # print(self.priorpro)
        # print(self.varipro)

        return

    def discriminate(self, data, rowvar=False):
        '''
        :discriminate: 对测试集进行分类
        :param data: 测试数据集矩阵，矩阵元素可以是数字或者表示特征取值的字符串
        :type data: np.array
        :param rowvar: 指定每行或者每列代表一个变量；rowvar=True指定每行作为一个变量，每列作为一个样本向量；rowvar=False指定每列作为一个变量，每行作为一个样本向量。默认值为rowvar=False
        :type rowvar: bool
        :return: 元组(res, respro)
        :        res: 分类结果列表，类型为list，其中res[i]为行数或者列数下标为i(下标从0开始)的样本向量的类别标签
        :        respro: 样本属于各个类别的概率列表，类型为list，其中respro[i]为行数或者列数下标为i(下标从0开始)的样本向量属于各个类别的概率
        :        示例: 假设有两个测试集样本，可能的一个返回值为(res,respro)，其中res=['类别A','类别A']，respro=[{'类别A':0.22,'类别B':0.78}, {'类别A':0.99,'类别B':0.01}]
        :rtype: tuple
        '''
        # 1. 首先训练集矩阵统一转换为rowvar=False的情况，即每行为一个样本向量
        if rowvar==True:
            data=data.T
        if data.ndim==1:
            data=np.array([data])

        # 2. 对于各个测试集的样本向量，对类别的每一个取值yi，首先计算p(x|yi)p(yi)=p(x1|yi)*p(x2|yi)*...*p(xn|yi)p(yi)，计算结果最大的一个作为分类结果
        size=np.shape(data)[0]
        count=np.shape(data)[1]

        res=[]    #分类结果

        for i in range(size):
            p=[]
            kind=[]
            for k in self.priorpro.keys():
                prior=self.priorpro[k]
                for m in range(count):
                    name=str(data[i][m])+'|'+str(k)
                    if name in self.varipro[m].keys():
                        prior*=self.varipro[m][name]
                    else:
                        prior*=0
                        break
                p.append(prior)   # 类别yi的后验概率的分子部分p(x|yi)p(yi)
                kind.append(k)    # 类别yi的对应标签
            res.append(kind[p.index(max(p))])
            add=sum(p)
            p=[x/add for x in p]                  # 计算后验概率，因为后验概率的分母部分均相同，因此后验概率的分母部分即为各个分子部分之和，而无需重新计算
            self.respro.append(dict(zip(kind,p)))
        
        return (res,self.respro)
