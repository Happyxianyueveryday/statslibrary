import numpy as np

class CorreCoef:

    def pearson_coef(self, data, rowvar=True):
        '''
        :pearson_coef: 求解pearson相关系数矩阵
        :param data: 样本向量矩阵
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，rowvar=False指定每一行作为一个样本向量
        :type rowvar: bool
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
        :type rowvar: bool
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
        :type rowvar: bool
        :return: 样本向量矩阵data的kendall相关系数矩阵
        :rtype: np.array
        '''
        # 1. 若每一列为一个变量的取值，则直接将其转置为每一行为一个变量的取值
        if rowvar==False:
            data=data.T
        
        for i in range(np.shape(data)[0]):
            data[i]=np.argsort(data[i])

        # 2. 对每个两个变量之间计算kendall系数，并放入相关系数矩阵的对应位置
        size=np.shape(data)[0]    # 变量数量
        count=np.shape(data)[1]   # 样本向量数量
        res=np.zeros((size,size))
        
        for i in range(size):
            for k in range(size):
                P=Q=T=U=0
                # 检查每个元组对是concordant pair，discordant pair，tied pair in x或者是tied pair in y
                # concordant pair: {(x1,y1),(x2,y2)} and sgn(x2-x1)==sgn(y2-y1)
                # discordant pair: {(x1,y1),(x2,y2)} and sgn(x2-x1)==-sgn(y2-y1)
                # tied pair: {(x1,y1),(x2,y2)} and sgn(x2-x1)==0 or sgn(y2-y1)==0
                # tied pair in x: {(x1,y1),(x2,y2)} and sgn(x2-x1)==0 and sgn(y2-y1)!=0
                # tied pair in y: {(x1,y1),(x2,y2)} and sgn(y2-y1)==0 and sgn(x2-x1)!=0
                for m in range(count):
                    for n in range(m+1,count):
                        value1=np.sign(data[i][m]-data[i][n])
                        value2=np.sign(data[k][m]-data[k][n])
                        if value1==0 and value2==0:
                            pass
                        if value1==0 and value2!=0:
                            T+=1
                        elif value2==0 and value1!=0:
                            U+=1
                        elif value1==value2:
                            P+=1
                        elif value1==-value2:
                            Q+=1
                res[i][k]=(P-Q)/np.sqrt((P+Q+T)*(P+Q+U))
        
        return res
    
    
