import numpy as np

class DistanceDiscri:

    def __init__(self):
        '''
        :__init: DistanceDiscri类的初始化方法
        ''' 
        self.cov=[]   # 各个类别的协方差矩阵的列表
        self.avg=[]   # 各个类别的协方差矩阵的列表
        self.label=[] # 各个类别的标签名称

        return

    def train(self, *data, rowvar=True, label=[]):
        '''
        :train: 各个类别的训练集，该方法从训练集中计算出各个类别的协方差矩阵和均值向量(重心)
        :param *data: 不定数目的各个类别的训练集，这些类别分别被编号为0,1,...
        :type *data: np.array
        :param rowvar: 指定每行或者每列代表一个变量；rowvar=True指定每行作为一个变量，每列作为一个样本向量；rowvar=False指定每列作为一个变量，每行作为一个样本向量
        :type rowvar: bool
        :param label: 各个类别的训练集所对应的类别名称，该名称必须与训练集在参数的顺序一一对应
        :type label: list
        '''
        # 1. tuple转换为list
        data=list(data)

        # 2. 将各个类别的原始训练集统一转换为rowvar=False的情况，即每列作为一个变量，每行作为一个样本向量
        if rowvar==True:
            data=[x.T for x in data]
        
        # 3. 计算各个类别训练集的均值向量(重心)和协方差矩阵，并储存在类中，同时储存类别的标签
        for i in range(len(data)):
            self.cov.append(np.cov(data[i],rowvar=False))
            self.avg.append(np.average(data[i],axis=0))
        self.label=label

        return

    def discriminate(self, data, rowvar=True):
        '''
        :discrinate: 对测试集的样本进行距离判别
        :param data: 测试集样本矩阵
        :type data: np.array
        :param rowvar: 指定每行或者每列代表一个变量；rowvar=True指定每行作为一个变量，每列作为一个样本向量；rowvar=False指定每列作为一个变量，每行作为一个样本向量
        :type rowvar: bool
        :return: 各个样本的分类结果res，res[i]为第i个样本所属的类别标签
        :rtype: list
        '''
        # 1. 将各个类别的原始训练集统一转换为rowvar=False的情况，即每列作为一个变量，每行作为一个样本向量
        if rowvar==True:
            data=data.T
        
        if data.ndim==1:
            data=np.array([data])
        
        # 2. 对每个样本向量，计算该样本向量到所有类别均值向量的马氏距离
        res=[]                  # 分类结果
        size=np.shape(data)[0]  # 测试集的样本向量数量
        count=len(self.label)   # 分类的类别个数
        
        for i in range(size):
            dist=[0 for i in range(count)]    #当前样本向量到各个类别的距离
            for k in range(count):
                dist[k]=self.__mah_distance(data[i],self.avg[k],self.cov[k])
            res.append(self.label[dist.index(min(dist))])

        return res

    def __mah_distance(self, a, b, cov_vec):
        '''
        :mah_distance :求解马氏距离
        :comment: 该方法存在如下两种主要的调用方法:
        :1. 计算一个未分类向量到一个类别的马氏距离: 这时a为未分类向量，b为一个类别的均值向量，cov_vec为该类别的协方差矩阵，返回未分类变量a到某个类别的马氏距离
        :2. 计算同一个类别中两个样本向量的马氏距离: 这时a, b分别为属于同一类别的两个样本向量，cov_vec为该列别的协方差矩阵，返回同类别下的向量a, b间的马氏距离

        :type a: np.array
        :type b: np.array
        :type cov_vec: np.array
        :rtype: float
        '''
        if cov_vec.ndim<2:   #判断协方差矩阵是否为2维以上，若非2维以上，则无法求逆，因此无法求解马氏距离，这时直接返回欧氏距离
            return self.__euc_distance(a,b)
        rev_vec=np.linalg.pinv(cov_vec)  # 求协方差矩阵的逆矩阵
        tmp=a-b                          # 行向量, tmp.T为列向量
        res=np.sqrt(np.dot(np.dot(tmp,rev_vec),tmp.T)) 

        return res