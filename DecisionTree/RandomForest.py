import DecisionTree as DT
import numpy as np
import pandas as pd
import time

class RandomForest:
    '''
    : RandomForest: 随机森林类
    : note: 该随机森林基于CART决策树进行构建
    '''
    def __init__(self, train, n_trees, sample_leaf_limits, sample_ratio, chara_ratio):
        '''
        : __init__: 根据参数初始化随机森林，并根据训练集进行训练
        : note: 实现步骤可以直接参照李航的统计学习方法中的步骤依次进行实现
        : param train: 训练集，其中第一列为样本类别标签
        : type train: pd.Dataframe
        : param n_trees: 随机森林中的决策树个数
        : type n_trees: int
        : param sample_leaf_limits: 随机挑选的样本比例，范围在[0,1]
        : type sample_leaf_limits: float
        : param sample_ratio: 随机挑选的特征比例，范围在[0,1]
        : type chara_ratio: float
        '''
        self.forest = []
        fn = int(chara_ratio*(train.shape[1]-1))
        for n in range(n_trees):
            temp1 = time.time()
            sf = np.random.choice(np.arange(1,train.shape[1]),fn,replace=False)
            sf = np.append(0,sf) 
            train_n = train.iloc[:,sf]
            p = np.random.random_sample()*(1-sample_ratio)+sample_ratio
            train_n = train_n.loc[np.random.choice(train_n.index, int(p*train_n.index.size), replace=False)]
            tree=DT.DecisionTree(train_n, sample_leaf_limits)
            self.forest.append(tree)
            temp2 = time.time()
            print('随机森林中的第%d棵树构造成功，耗时%f'%(n,temp2-temp1))  


    def predict(self, test):
        '''
        : predict: 使用测试集进行预测
        : param test: 测试集矩阵，其中第一列为样本类别标签
        : type test: pd.DataFrame
        : return: 预测的准确度
        : rtype: float
        '''
        y = test.pop(test.columns[0])
        length = y.size
        y_process = pd.Series([0]*length,index=y.index)
        n_trees = len(self.forest)
        res = [0]*n_trees     # 构造出的随机森林中的每一个树的结果
        for i in range(length):
            x = test.iloc[i]
            for t in range(n_trees):
                res[t] = self.forest[t].classifier(x)
            y_process.iloc[i] = max(res,key=res.count)
        data = y-y_process
        return data[data==0].size/length
    



