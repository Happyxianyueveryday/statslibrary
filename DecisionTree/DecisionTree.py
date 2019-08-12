import time
import pandas as pd
import numpy as np

class TreeNode:
    def __init__(self, data_index, left=None, right=None, feature=None, split=None, out = None):
        self.data_index = data_index            # 当前结点的集合的行索引
        self.left = left                        # 当前结点的左子结点下标
        self.right = right                      # 当前结点的右子结点下标
        self.feature = feature                  # 分裂特征值
        self.split = split                      # 结点分割值
        self.out = out                          # 叶子结点的输出值


class DecisionTree:
    def __init__(self, S, min_sample_leaf):
        '''
        : __init__: 构造CART决策树
        : param S: 训练和构造决策树的训练集
        : type S: pd.DataFrame
        : param min_sample_leaf: 每个叶结点的最小样本数
        : type min_sample_leaf: int
        ''' 
        self.root = TreeNode(S.index)   # 决策树的根结点
        self.tree = []                  # 决策树的结点列表
        self.tree.append(self.root)
        i = 0    # 指向当前处理的叶节点的下标
        j = 0    # 指向最后一个叶结点的下标
        # 1. 循环构造决策树的每一个结点
        while True:
            res = self.divide(S, self.tree[i], min_sample_leaf)
            if res:   # 1.1 若当前结点可以划分，则将当前结点进行划分
                self.tree.extend(res)    
                self.tree[i].left = j+1
                self.tree[i].right = j+2
                j += 2
                i += 1
            elif i == j:  
                break
            else:    # 1.2 若当前结点不可以划分，则按顺序处理下一个结点
                i += 1


    def divide(self, S, leaf, min_sample_leaf):
        '''
        : divide: 判断叶子结点是否可以划分
        : param S: 当前结点的训练集
        : type S: pd.DataFrame
        : param leaf: 当前叶子结点
        : type leaf: TreeNode
        : param min_sample_leaf: 每个叶结点的最小样本数
        : type min_sample_leaf: int
        '''
        # 1. 得到当前结点的数据集 
        data = S.loc[leaf.data_index]
        res = self.gini_divide(data,min_sample_leaf)
        if not res:
            leaf.out = data.iloc[:,0].mode()[0]   # 出现次数最多的值就是当前结点的值
            return None
        feature, split = res
        leaf.feature = feature
        leaf.split = split
        left = TreeNode(data[data[feature] <= split].index)
        right = TreeNode(data[data[feature] > split].index)
        return left, right


    def gini_divide(self, data, min_sample_leaf):
        '''
        : gini_divide: 计算特征的分割值
        : return: (当前特征的最佳分割特征,分割值)
        : rtype: (float, float)
        '''
        # 1. 根据基尼系数得到数据集上的最佳划分
        res = [] 
        S = data.shape[0]
        for feature in np.arange(1,data.shape[1]):
            if self.is_one_hot(data,feature):
                index_bool_value = data.iloc[:,feature] == 0
                s1 = data.loc[index_bool_value,data.columns[0]]
                S1 = s1.shape[0]
                S2 = S-S1
                if S1<min_sample_leaf or S2<min_sample_leaf:
                    continue
                s2 = data.loc[not index_bool_value,data.columns[0]]
                res.append(((S1*self.gini(s1) + S2*self.gini(s2))/S,feature,0))
            else:
                Gini_list = []# 二元组列表(gini,split)，存放每个特征的最优gini值和分割点
                s = data.iloc[:,[0,feature]]
                s = s.sort_values(s.columns[1])
                for i in np.arange(min_sample_leaf-1,S-min_sample_leaf):
                    if s.iloc[i,1] == s.iloc[i+1,1]:
                        continue
                    else:
                        S1 = i+1
                        S2 = S-S1
                        s1 = data.iloc[:(i+1),0]
                        s2 = data.iloc[(i+1):,0]
                        Gini_list.append(((S1*self.gini(s1) + S2*self.gini(s2))/S,s.iloc[i,1]))
                if Gini_list:
                    gini_divide,split = min(Gini_list,key=lambda x:x[0])
                    res.append((gini_divide,feature,split))
        if res:
            _,feature,split = min(res,key=lambda x:x[0])
            return (data.columns[feature],split)
        else:
            return None
    
       
    def gini(self, s):
        '''
        : gini: 计算基尼系数
        : param s: 样本向量
        : type s: np.array
        '''
        p = np.array(s.value_counts(True))
        res = 1-np.sum(np.square(p))
        return res


    def is_one_hot(self, data,feature):
        for i in range(data.shape[0]):
            v = data.iloc[i,feature]
            if v != 0 or v != 1:
                return False
        return True


    def classifier(self, sample):
        '''
        : classifier: 分类器
        : param sample: 测试集
        : type sample: pd.DataFrame
        : return: 预测准确率
        : rtype: float
        '''
        # 1. 对每一个结点，从节点的划分属性和分割值，来观察其子结点
        i = 0
        while True:
            node = self.tree[i]
            # 2. 判断子节点是否为叶节点
            if node.out != None:
                return node.out
            
            # 3. 若是叶子结点，则得到输出，否则继续寻找子节点
            if sample[node.feature] <= node.split:
                i = node.left
            else:
                i = node.right
    
    










