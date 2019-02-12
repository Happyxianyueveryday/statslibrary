import numpy as np

class PCA:

    def __init__(self, n_components=2):
        '''
        :__init__: 初始化PCA类
        :param n_components: PCA降维后所保留的维数，默认值为2，该值不得超过原始数据的总维数
        :type n_components: int
        '''
        self.__components=n_components   # 降维后保留的维数
        self.__eigvalue=[]               # 样本矩阵的特征值
        self.__eigvec=[]                 # 每个特征值所对应的特征向量
        self.__tarvalue=[]               # 降维后所保留的特征对应的特征值
        self.__tarvec=[]                 # 降维后所保留的特征对应的特征向量
        self.__transmat=np.array([])     # 降维变换矩阵

        return 

    def fit(self, data, rowvar=True):
        '''
        :fit: 对原始数据进行PCA主成分分析，得出需要保留的特征，并将PCA主成分分析的结果信息保存在当前对象中
        :param data: 训练集矩阵，即进行PCA分析的数据集，在该方法中首先会对训练集矩阵进行标准化
        :type data: np.array
        :param rowvar: 指定每一行或者每一列代表一个特征：rowvar=True指定每一行代表一个特征，即每一列代表一个样本向量；rowvar=False指定每一列代表一个特征，即每一行代表一个样本向量，默认值为rowvar=True
        :type rowvar: bool
        '''
        # 1. 首先将训练集矩阵变换为rowvar=False的情况，即每一列代表一个特征，每一行代表一个样本
        if rowvar==True:
            data=data.T
        
        # 2. 然后对训练集矩阵进行标准化
        size=np.shape(data)[1]     # 特征的数量
        count=np.shape(data)[0]    # 每个特征的样本数
        mean=np.array([np.mean(data[:,i]) for i in range(size)])    # 各个特征的均值向量
        data=data-mean             # 原始矩阵每行(也即每个样本)减去均值向量得到标准化后的矩阵

        # 3. 求解标准化后的训练集矩阵的协方差矩阵
        cov=np.cov(data,rowvar=False)

        # 4. 对得到的协方差矩阵进行特征值分解，分解得到特征值和对应的特征向量
        self.__eigvalue, self.__eigvec=np.linalg.eig(cov)   # 附注: self.__eigvec中的每一列为一个特征向量，此处负号可选，因为特征向量符号取反仍为特征向量
        self.__eigvec=-self.__eigvec

        # 5. 将特征值和对应的特征向量从小到大排列，选出后self.__components个特征值和特征向量
        conn=[(self.__eigvalue[i], self.__eigvec[:,i]) for i in range(self.__components)]
        conn.sort(reverse=True)
        self.__tarvalue=np.array([conn[i][0] for i in range(self.__components)])
        self.__tarvec=np.array([conn[i][1] for i in range(self.__components)])

        # 6. 使用上述选出的self.__components个特征矩阵生成PCA降维的变换矩阵
        self.__transmat=np.array([self.__tarvec[i] for i in range(self.__components)]).T

        return

    def transform(self, data, rowvar=True):
        '''
        :transform: 根据fit成员方法的主成分分析结果信息，对数据进行PCA降维变换
        :param data: 测试集矩阵，即进行降维变换的数据，测试集矩阵无需归一化
        :type data: np.array
        :param rowvar: 指定每一行或者每一列代表一个特征：rowvar=True指定每一行代表一个特征，即每一列代表一个样本向量；rowvar=False指定每一列代表一个特征，即每一行代表一个样本向量，默认值为rowvar=True
        :type rowvar: bool
        '''
        # 1. 首先将训练集矩阵变换为rowvar=False的情况，即每一列代表一个特征，每一行代表一个样本
        if rowvar==True:
            data=data.T

        # 2. 然后对样本集矩阵进行标准化
        size=np.shape(data)[1]     # 特征的数量
        count=np.shape(data)[0]    # 每个特征的样本数
        mean=np.array([np.mean(data[:,i]) for i in range(size)])    # 各个特征的均值向量
        data=data-mean      

        # 3. 标准化后的测试集矩阵和变换矩阵相乘得到降维后的结果矩阵
        res=np.dot(data,self.__transmat)

        return res
    
    def eigenvalue(self, only=False):
        '''
        :eigenvalue: 返回根据训练集得到的各个特征的特征根
        :param only: 指定是否仅保留降维后的特征的特征根，only=True指定仅保留降维后的特征的特征根，only=False则保留全部特征的特征根，默认值为only=False
        :type only: bool
        :return: 训练集矩阵在PCA主成分分析中的各个特征的对应特征根
        :rtype: np.array
        '''
        if only==False:
            return self.__eigvalue
        else:
            return self.__tarvalue
    
    def eigenvector(self, only=False):
        '''
        :eigenvector: 返回根据训练集得到的各个特征的特征向量
        :param only: 指定是否仅保留降维后的特征的特征向量，only=True指定仅保留降维后的特征的特征向量，only=False则保留全部特征的特征向量，默认值为only=False
        :type only: bool
        :return: 训练集矩阵在PCA主成分分析中的各个特征的对应特征向量的矩阵，返回矩阵的每一行为一个特征向量
        :rtype: np.array
        '''
        if only==False:
            return self.__eigvec
        else:
            return self.__tarvec

    def set_components(self, n_components=2):
        '''
        :set_components: 改变保留的特征数
        :param n_components: 保留的特征数目
        :type n_components: int
        '''
        self.__components=n_components
        return 

    def variance_ratio(self, only=False):
        '''
        :variance_ratio: 计算各个特征的权重
        :param only: 指定是否仅保留降维后的特征的权重，only=True指定仅保留降维后的特征的权重，only=False则保留全部特征的权重，默认值为only=False
        :type only: bool
        :return: 各个特征的权重列表
        :rtype: np.array
        '''
        if only==False:
            return np.divide(self.__eigvalue,np.sum(self.__eigvalue))
        else:
            return np.divide(self.__tarvalue,np.sum(self.__eigvalue))
