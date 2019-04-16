# coding = utf-8

import numpy as np
from sklearn import preprocessing

class FacAnaly:
    
    def __init__(self, n_components=2):
        '''
        : __init: 初始化方法
        '''
        pass
    
    def analy(self, data, rowvar=True, n_components=2):
        '''
        : analy: 进行因子分析，计算得到因子载荷矩阵
        : param data: 样本集矩阵
        : type data: np.array
        : param rowvar: 指定样本集的矩阵的每行或每列代表一个变量，rowvar=True指定样本集矩阵的每一行代表一个向量，rowvar=False指定样本集矩阵的每一列代表一个向量
        : type rowvar: bool
        : param n_components: 保留的因子数
        : type n_components: int
        : return: 因子分析结果，即因子载荷矩阵，因子载荷矩阵的每一列代表一个特征，每一行代表一个样本，例如矩阵元素(x,y)表示在样本x中特征y的因子权重
        : rtype: np.array
        '''
        # 1. 首先将样本集矩阵变换为rowvar=False的情况，即每一列代表一个特征，每一行代表一个样本
        if rowvar==True:
            data=data.T
        
        # 2. 然后对样本集矩阵进行标准化，标准化为正态分布，这时均值为0，方差为1
        data = preprocessing.scale(data, axis = 1)   # axis=1指定按行标准化

        # 3. 计算标准化后的矩阵的相关系数矩阵
        corr = np.corrcoef(data)
        print(corr.shape)
        #print(corr)

        # 4. 计算相关矩阵R的特征根和特征向量
        root, vec = np.linalg.eig(corr)
        dic={}   #将特征值和对应的特征值相对应
        for i in range(len(root)):
            dic[root[i]]=vec[:,i]     #附注:此处容易处理错误，使用库函数时必须严格查阅在线手册，每一个特征和vec中的一个列对应，而不是与一个行对应，不要想当然地处理参数

        # 5. 生成载荷矩阵并作为结果返回
        root = sorted(root, reverse = True)
        #print(root)
        res=[]
        for i in range(n_components):
            res.append((-np.sqrt(root[i]))*dic[root[i]])    #附注: 按照因子分析的课件中的公式应该是math.sqrt(root[i])*dic[root[i]]，之所以加负号取相反数，是因为特征向量取反仍然是特征向量，而不取反，结果会和课本的结果相差一个负号
        res = np.array(res).T

        return res




