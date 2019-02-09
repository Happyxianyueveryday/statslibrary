import numpy as np

class VarAnaly:

    def single_anova(self, data, rowvar=False):
        '''
        :single_anova: 单因素方差分析
        :param data: 样本集矩阵，因素的不同水平的样本数必须相同
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为因素的不同水平；rowvar=True指定每一行代表因素的一个水平，即每一列作为一个观察结果；rowvar=False指定每一列代表因素的一个水平，即每一行作为一个观察结果，默认rowvar=True
        :type rowvar: bool
        :return: 元组形式的方差分析试验表:(sa,se,st,fa,fe,ft,_sa,_se,f)，其中sa=该单因素平方和，se=误差平方和，st=平方和总和=sa+se，fa=因素自由度，fe=误差自由度，ft=自由度总和=fa+fe，_sa=因素均方，_se=误差均方，f=F比=_sa/_se
        :rtype: tuple
        '''
        # 1. 将原始数据统一变换为每一行代表因素的一个水平，即每一列作为一个观察结果的情况
        if rowvar==False:
            data=data.T
        
        # 2. 计算各个样本的均值
        size=np.shape(data)[0]
        count=np.shape(data)[1]

        avg=[]                       #同水平下的样本均值
        for i in range(size):
            avg.append(np.average(data[i]))
        avg=np.array(avg) 
        avg_all=np.average(avg)      #数据总平均数
        avg_all=np.array([avg_all for i in range(count)])  #总体平均数向量化
         
        # 3. 计算因素平方和sa，误差平方和se与平方和总和st
        sa=0.0
        se=0.0
        for i in range(size):
            se+=np.sum(np.square(np.add(data[i],-avg[i])))
            sa+=np.sum(np.square(np.add(avg[i],-avg_all)))
        st=sa+se
        
        # 4. 计算因素自由度fa，误差自由度fe，自由度总和ft
        fa=size-1
        fe=count*size-size
        ft=fa+fe

        # 5. 计算因素均方_sa，误差均方_se，F比f
        _sa=sa/fa
        _se=se/fe
        f=_sa/_se

        return (sa,se,st,fa,fe,ft,_sa,_se,f)



        
