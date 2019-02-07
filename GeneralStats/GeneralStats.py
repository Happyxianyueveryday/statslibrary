import numpy as np
import math as mt

class GeneralStats:
    
    def average(self, data, rowvar=True):
        '''
        :average: 求解样本的平均数
        :param data: 样本集
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，也即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，也即每一列代表一个变量
        :type rowvar: bool
        :return: 各个变量的平均数组成的向量
        :rtype: np.array
        '''
        # 1. 统一变换为rowvar==False的情况，即每一列代表一个变量，每一行代表一个样本向量
        if rowvar==True:
            data=data.T

        # 2. 特别处理一维数组的情况
        if data.ndim==1:
            return data
        
        # 3. 各个样本向量进行求和
        size=np.shape(data)[1]
        count=np.shape(data)[0]
        add=np.zeros((1,size))
        for i in range(count):
            add=np.add(add,data[i])

        # 4. 求解平均向量
        res=np.divide(add,count)
        return res

    def median(self, data, rowvar=True):
        '''
        :median: 求解样本的中位数
        :param data: 样本集
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，也即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，也即每一列代表一个变量
        :type rowvar: bool
        :return: 各个变量的中位数组成的向量
        :rtype: np.array
        '''
        # 1. 统一变换为rowvar==True的情况，即每一行代表一个变量，每一列代表一个样本向量
        if rowvar==False:
            data=data.T
        
        # 2. 特别处理一维数组的情况
        if data.ndim==1:
            count=np.shape(data)[0]
            data=np.sort(data)
            if count%2:
                return np.array([data[mt.floor(count/2)]])
            else:
                return np.array([(data[mt.floor(count/2)]+data[mt.floor(count/2)-1])/2.0])

        # 3. 通过排序生成中位数
        size=np.shape(data)[0]
        count=np.shape(data)[1]
        for i in range(size):
            data[i]=np.sort(data[i])

        res=np.zeros((1,size))

        if count%2:
            for i in range(size):
                res[:,i]=data[i][mt.floor(count/2)]
        else:
            for i in range(size):
                res[:,i]=(data[i][mt.floor(count/2)]+data[i][mt.floor(count/2)-1])/2.0
        
        return res

    def mode(self, data, rowvar=True):
        '''
        :mode: 求解样本的众数
        :param data: 样本集
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，也即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，也即每一列代表一个变量
        :type rowvar: bool
        :return: 各个变量的众数组成的向量
        :rtype: np.array
        '''
        # 1. 统一变换为rowvar==True的情况，即每一行代表一个变量，每一列代表一个样本向量
        if rowvar==False:
            data=data.T
        
        # 2. 特别处理一维数组的情况
        if data.ndim==1:
            dic={}
            for i in range(np.shape(data)[0]):
                if data[i] in dic:
                    dic[data[i]]+=1
                else:
                    dic[data[i]]=1
            res=np.array([max(dic,key=dic.get)])
            return res
        
        # 3. 生成众数结果
        size=np.shape(data)[0]
        count=np.shape(data)[1]
        res=[]
        for i in range(size):
            dic={}
            for k in range(count):
                if data[i][k] in dic:
                    dic[data[i][k]]+=1
                else:
                    dic[data[i][k]]=1
            res.append(max(dic,key=dic.get))
        return np.array(res)

    def quantile(self, data, fraction, rowvar=True, interpolation='linear'):
        '''
        :quantile: 求解样本的分位数
        :param data: 样本集
        :type data: np.array
        :param fraction: 分位值，满足fraction>=0且fraction<=1
        :type fraction: float
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，也即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，也即每一列代表一个变量
        :type rowvar: bool
        :param interpolation: 此可选参数指定当所需分位数位于两个数据点i<j之间时要使用的插值方法，
        :                     取值为{'linear', 'lower', 'higher', 'midpoint'}。
        :                     若分位值fraction(0和1之间)计算得到的分位数下标不是整数，该下标两侧的数组元素分别为i和j，则:
        :                     'linear': i+fraction*(j-i)
        :                     'lower': i
        :                     'higher': j
        :                     'midpoint': (i+j)/2
        :type interpolation: str
        :return: 各个变量的分位数组成的向量
        :rtype: np.array
        '''

        # 1. 统一变换为rowvar==True的情况，即每一行代表一个变量，每一列代表一个样本向量
        if rowvar==False:
            data=data.T

        # 2. 特殊处理data为向量的情况
        if data.ndim==1:
            data=np.sort(data)
            tar=fraction*(np.shape(data)[0]-1)
            res=0
            if interpolation=='linear':
                res=data[mt.floor(tar)]+(data[mt.ceil(tar)]-data[mt.floor(tar)])*fraction
            elif interpolation=='lower':
                res=data[mt.floor(tar)]
            elif interpolation=='higher':
                res=data[mt.ceil(tar)]
            else:
                res=(data[mt.floor(tar)]+data[mt.ceil(tar)])/2  
            return np.array([res])

        # 3. 生成分位数
        size=np.shape(data)[0]
        count=np.shape(data)[1]
        res=np.zeros((1,size))
        for i in range(size):
            data[i]=np.sort(data[i])
            tar=fraction*(count-1) 
            if interpolation=='linear':
                res[:,i]=data[i][mt.floor(tar)]+(data[i][mt.ceil(tar)]-data[i][mt.floor(tar)])*fraction
            elif interpolation=='lower':
                res[:,i]=data[i][mt.floor(tar)]
            elif interpolation=='higher':
                res[:,i]=data[i][mt.ceil(tar)]
            else:
                res[:,i]=(data[i][mt.floor(tar)]+data[i][mt.ceil(tar)])/2        

        return res

    def range(self, data, rowvar=True):
        '''
        :range: 求解样本的极差
        :param data: 样本集
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，也即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，也即每一列代表一个变量
        :type rowvar: bool
        :return: 各个变量的极差组成的向量
        :rtype: np.array
        '''
        # 1. 统一变换为rowvar==True的情况，即每一行代表一个变量，每一列代表一个样本向量
        if rowvar==False:
            data=data.T
        
        # 2. 特殊处理data为向量的情况
        if data.ndim==1:
            return np.array([np.max(data)-np.min(data)])
        
        # 3. 计算data为矩阵时的极差
        size=np.shape(data)[0]
        res=np.zeros((1,size))
        
        for i in range(size):
            res[:,i]=np.max(data[i])-np.min(data[i])

        return res

    def variance(self, data, rowvar=True):
        '''
        :variance: 求解样本的方差
        :param data: 样本集
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，也即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，也即每一列代表一个变量
        :type rowvar: bool
        :return: 各个变量的方差组成的向量
        :rtype: np.array
        '''
        # 1. 统一变换为rowvar==True的情况，即每一行代表一个变量，每一列代表一个样本向量
        if rowvar==False:
            data=data.T
        
        # 2. 特殊处理data为向量的情况
        if data.ndim==1:
            avg=np.sum(data)/np.shape(data)[0]
            res=np.sum(np.square(np.add(data,-avg)))/np.shape(data)[0]
            return res
        
        # 3. 计算data为矩阵时的方差
        size=np.shape(data)[0]    #变量数
        count=np.shape(data)[1]   #每个变量的样本数
        res=np.zeros((1,size))

        for i in range(size):
            avg=np.sum(data[i])/count
            res[:,i]=np.sum(np.square(np.add(data[i],-avg)))/count
        
        return np.array([res])

    def standard_dev(self, data, rowvar=True):
        '''
        :variance: 求解样本的标准差
        :param data: 样本集
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为样本向量；rowvar=True指定每一列作为一个样本向量，也即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，也即每一列代表一个变量
        :type rowvar: bool
        :return: 各个变量的标准差组成的向量
        :rtype: np.array
        '''
        # 1. 统一变换为rowvar==True的情况，即每一行代表一个变量，每一列代表一个样本向量
        if rowvar==False:
            data=data.T
        
        # 2. 特殊处理data为向量的情况
        if data.ndim==1:
            avg=np.sum(data)/np.shape(data)[0]
            res=np.sqrt(np.sum(np.square(np.add(data,-avg)))/np.shape(data)[0])
            return np.array([res])
        
        # 3. 计算data为矩阵时的标准差
        size=np.shape(data)[0]    #变量数
        count=np.shape(data)[1]   #每个变量的样本数
        res=np.zeros((1,size))

        for i in range(size):
            avg=np.sum(data[i])/count
            res[:,i]=np.sqrt(np.sum(np.square(np.add(data[i],-avg)))/count)
        
        return res
            
            


            

        


