import numpy as np
import random as rd

class Kmeans:

    def __init__(self, data, kind=2, rowsam=True):
        '''
        :__init__: Kmeans类初始化
        :param data: 样本矩阵，样本矩阵中的每个样本向量(每行或者每列)将被依次编号为0,1,2,...
        :type data: np.array
        :param kind: 聚类的类别数量，默认值为2，即聚类为2类，这些类别将被依次编号为0,1,2,...
        :type kind: int
        :param rowsam: 指定指定每一行或者每一列作为样本向量，rowsam=True指定每一行作为一个样本向量，rowsam=False指定每一列作为一个样本向量，默认值为rowsam=True
        :type rowsam: bool
        '''
        # 1. 将样本矩阵统一转换为rowsam=True的情况，即每一行作为一个样本向量
        if rowsam==False:
            data=data.T
        
        # 2. 使用原始样本矩阵初始化类的变量
        self.__data=data
        self.__kind=kind
        self.__res=[]

        return 

    def reload(self, data, kind=2, rowsam=True):
        '''
        :reload: 重新载入Kmeans类对象的数据
        :param data: 新的样本矩阵，样本矩阵中的每个样本向量(每行或者每列)将被依次编号为0,1,2,...
        :type data: np.array
        :param kind: 新的聚类的类别数量，默认值为2，即聚类为2类，这些类别将被依次编号为0,1,2,...
        :type kind: int
        :param rowsam: 指定指定每一行或者每一列作为样本向量，rowsam=True指定每一行作为一个样本向量，rowsam=False指定每一列作为一个样本向量，默认值为rowsam=True
        :type rowsam: bool
        '''
        # 1. 将样本矩阵统一转换为rowsam=True的情况，即每一行作为一个样本向量
        if rowsam==False:
            data=data.T
        
        # 2. 重设样本矩阵和类别数量
        self.__data=data
        self.__kind=kind

        return 
    
    def getdata(self, rowsam=True):
        '''
        :getdata: 返回准备聚类的原始样本向量矩阵
        :param rowsam: 指定指定每一行或者每一列作为样本向量，rowsam=True指定每一行作为一个样本向量，rowsam=False指定每一列作为一个样本向量，默认值为rowsam=True
        :type rowsam: bool
        :return: 原始样本向量矩阵
        :rtype: np.array
        '''
        if rowsam==False:
            return self.__data.T
        else:
            return self.__data
        
    def getkind(self):
        '''
        :getkind: 返回聚类的类别数量
        :return: 聚类的类别数量
        :rtype: int
        '''
        return self.__kind
    
    def cluster(self):
        '''
        :cluster: 执行Kmeans聚类，经典Kmeans聚类使用欧氏距离
        :return: 聚类结果，聚类结果res的格式为：二维list数组形式，其中res[i]即为编号为i的类别所含有的样本编号的列表
        :rtype: list
        '''
        # 1. 首先从原始数据中随机选择self.__kind个样本作为各个类别的质心
        size=np.shape(self.__data)[0]     #样本数量
        count=np.shape(self.__data)[1]    #单个样本维度
        
        focus=[]          #各个类别的质心集合
        for i in range(self.__kind):
            focus.append(rd.choice(self.__data))   #随机选择self.__kind个样本作为质心
        focus=np.array(focus)

        # 2. 将所有的样本分类到距离类别质心最近的类别中，然后更新类别的质心为类别中所有样本的均值向量，接着重复上述步骤直到所有类别的质心都不再变化
        res=[]        #各类别的样本集合

        while 1:
            # 2.1 对每个样本进行分类
            res=[[] for i in range(self.__kind)]         #每轮迭代的各类别的样本集合，这里需要特别注意每轮迭代过程中需要清空上一次迭代的结果

            for i in range(size):     
                dist=[0 for i in range(self.__kind)]     #样本到各个质心的距离
                for k in range(self.__kind):
                    dist[k]=np.linalg.norm(self.__data[i]-focus[k])
                res[dist.index(min(dist))].append(i)
            
            # 2.2 重新计算类别质心
            newfocus=np.array([[0.0 for i in range(count)] for k in range(self.__kind)])
            for i in range(self.__kind):
                if len(res[i])!=0:      #类别中有样本才重新计算质心，否则直接取原质心
                    for k in range(len(res[i])):
                        newfocus[i]+=self.__data[res[i][k]]
                    newfocus[i]/=len(res[i])
                else:
                    newfocus[i]=focus[i]
            
            # 2.3 判断新的质心是否和原质心相等
            if (focus==newfocus).all():
                break
            else:
                focus=newfocus

        self.__res=res
        return res


    def accuracy(self, real):
        '''
        :accuracy: 根据聚类结果计算准确度，本方法需要在调用cluster方法得到聚类结果后使用才可以得到正确结果
        :param real: 样本真实分类标签结果，为一维np.array数组形式，其中real[i]即为编号为i的样本的真实类别标签
        :type real: np.array
        :return: Kmeans聚类准确率。这里准确率的定义是，将每个类别中出现次数最多的真实标签作为整个类别的标签，样本的标签与所在类别标签相等即认为成功预测，最终准确率即为成功预测的样本数量除以样本总数
        :rtype: float
        '''
        # 1. 首先计算每个类别中出现次数最多的样本标签，将该标签作为类别的标签
        res=self.__res
        tags=[0 for i in range(self.__kind)]
        for i in range(len(res)):
            counts=[0 for i in range(self.__kind)]
            for k in range(len(res[i])):
                counts[real[res[i][k]]]+=1
            tags[i]=counts.index(max(counts))
        
        # 2. 然后计算准确率
        total=0.0
        corr=0.0
        for i in range(len(res)):
            for k in range(len(res[i])):
                if real[res[i][k]]==tags[i]:
                    corr+=1
                total+=1

        return corr/total
