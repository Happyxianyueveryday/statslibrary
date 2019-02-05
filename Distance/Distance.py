import math
import numpy as np

class Distance:
    def euc_distance(self,a,b):
        '''
        :euc_distance: 求解欧氏距离
        :param a: 向量a
        :type a: np.array
        :param b: 向量b
        :type b: np.array
        :return -> 向量a和向量b的欧式距离
        :rtype: float
        '''
        res=np.sqrt(np.sum(np.square(a-b)))
        return res
    
    def mah_distance(self,a,b,cov_vec):
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
        rev_vec=np.linalg.pinv(cov_vec)  #求协方差矩阵的逆矩阵
        tmp=a-b                          #行向量, tmp.T为列向量
        res=np.sqrt(np.dot(np.dot(tmp,rev_vec),tmp.T)) 

        return res

    def man_distance(self,a,b):
        '''
        :man_distance: 求解曼哈顿距离
        :param a: 向量a
        :type a: np.array
        :param b: 向量b
        :type b: np.array
        :return -> 向量a和向量b的曼哈顿距离
        :rtype: float
        '''
        res=np.sum(np.abs(a-b))
        return res

    def min_distance(self,a,b,p):
        '''
        :min_distance: 求解闵可夫斯基距离
        :param a: 向量a
        :type a: np.array
        :param b: 向量b
        :type b: np.array
        :param p: 闵科夫斯基距离的维数p
        :type p: int
        :return -> 向量a和向量b的闵可夫斯基距离
        :rtype: float
        '''
        res=np.power(np.sum(np.power(np.abs(a-b),p)),1/p)
        return res

    def standard_euc_distance(self,a,b,s):
        '''
        :standard_euc_distance: 求解标准欧几里得距离
        :param a: 向量a
        :type a: np.array
        :param b: 向量b
        :type b: np.array
        :param s: 向量a, b所属的类别的方差向量s
        :type s: np.array
        :return -> 向量a和向量b的标准欧几里得距离
        :rtype: float
        '''
        res=np.power(np.sum(np.divide(np.power(a-b,2),s)),1/2)
        return res
    
    def cos_distance(self,a,b):
        '''
        :standard_euc_distance: 求解余弦距离
        :param a: 向量a
        :type a: np.array
        :param b: 向量b
        :type b: np.array
        :return -> 向量a和向量b的余弦距离
        :rtype: float
        '''
        res1=np.sum(np.multiply(a,b))
        res2=np.sqrt(np.sum(np.square(a)))*np.sqrt(np.sum(np.square(b)))
        res=res1/res2
        return res


