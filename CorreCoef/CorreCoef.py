import numpy as np

class CorreCoef:

    def pearson_coef(self, data, rowvar=True):
        '''
        :pearson_coef: 求解pearson相关系数矩阵
        :param data: 样本向量矩阵
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，rowvar=False指定每一行作为一个样本向量
        :type rowvar: np.array
        :return: 样本向量矩阵data的pearson相关系数矩阵
        :rtype: np.array
        '''
        
        # 1. 计算每对任意两行，也即两个变量之间的相关系数
        cov=np.cov(data,rowvar=rowvar)

        # 2. 生成pearson相关系数矩阵
        size=np.shape(data)[0] if rowvar==True else np.shape(data)[1]
        res=np.zeros((size,size))

        for i in range(size):
            for k in range(size):
                res[i][k]=cov[i][k]/np.sqrt((cov[i][i]*cov[k][k])) 
        
        return res
    
    def spearman_coef(self, data, rowvar=True):
        '''
        :spearman_coef: 求解spearman相关系数矩阵
        :param data: 样本向量矩阵
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，rowvar=False指定每一行作为一个样本向量
        :type rowvar: np.array
        :return: 样本向量矩阵data的spearman相关系数矩阵
        :rtype: np.array
        '''
        # 1. 若每一列为一个变量的取值，则直接将其转置为每一行为一个变量的取值
        if rowvar==False:
            data=data.T
        
        # 2. 对每一行进行排序，返回每个变量取值的排序序号
        for i in range(np.shape(data)[0]):
            data[i]=np.argsort(data[i])
        
        # 3. 根据公式计算spearman相关系数
        size=np.shape(data)[0]
        res=np.zeros((size,size))

        for i in range(np.shape(data)[0]):
            for k in range(np.shape(data)[0]):
                ranksum=0.0
                n=np.shape(data)[1]
                for r in range(n):
                    ranksum+=np.square(data[i][r]-data[k][r])
                res[i][k]=1-6*ranksum/(n*(n**2-1))
        
        return res

    def kendall_coef(self, data, rowvar=True):
        '''
        :kendall_coef: 求解kendall相关系数矩阵
        :param data: 样本向量矩阵
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，rowvar=False指定每一行作为一个样本向量
        :type rowvar: np.array
        :return: 样本向量矩阵data的kendall相关系数矩阵
        :rtype: np.array
        '''
        return 
    
    
