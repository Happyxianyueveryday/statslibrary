import numpy as np

class VarAnaly:

    def single_anova(self, data, rowvar=False):
        '''
        :single_anova: 单因素方差分析
        :param data: 样本集矩阵，因素的不同水平的样本数必须相同
        :type data: np.array
        :param rowvar: 指定每一行或者每一列作为因素的不同水平；rowvar=True指定每一行代表因素的一个水平，即每一列作为一个观察结果；rowvar=False指定每一列代表因素的一个水平，即每一行作为一个观察结果，默认rowvar=True
        :type rowvar: bool
        :return: 元组形式的方差分析试验表:(sa,se,st,fa,fe,ft,_sa,_se,f)
        :        sa=该单因素平方和，se=误差平方和，st=平方和总和=sa+se
        :        fa=因素自由度，fe=误差自由度，ft=自由度总和=fa+fe
        :        _sa=因素均方，_se=误差均方
        :        f=F比=_sa/_se
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

    def double_anova(self, data):
        '''
        :single_anova: 双因素方差分析
        :param data: 因素A和因素B的样本集矩阵
        :            矩阵data格式: 假设因素A有r种水平，因素B有s种水平，则data为r×s矩阵，每一行代表因素A的一种水平，每一列代表因素B的一种水平，矩阵中的每个元素是一个
        :            矩阵data示例: np.array([[[58.2,52.6],[56.2,41.2],[65.3,60.8]], [[49.1,42.8],[54.1,50.5],[51.6,48.4]], [[60.1,58.3],[70.9,73.2],[39.2,40.7]], [[75.8,71.5],[58.2,51.0],[48.7,41.4]]])
        :type data: np.array
        :return: 元组形式的方差分析试验表:(sa,sb,sab,se,st,ta,tb,tab,te,tt,_sa,_sb,_sab,_se,fa,fb,fab)
        :        sa=因素A平方和，sb=因素B平方和，sab=交互作用平方和，se=误差平方和，st=平方和总和=sa+sb+sab+se
        :        ta=因素A自由度，tb=因素B自由度，tab=交互作用自由度，te=误差自由度，tt=自由度总和=ta+tb+tab+te
        :        _sa=因素A均方，_sb=因素B均方，_sab=交互作用均方，_se=误差均方
        :        fa=因素A的F比，fb=因素B的F比，fab=交互作用F比
        :rtype: tuple
        '''
        # 1. 计算过程中所需的样本均值
        size1=np.shape(data)[0]    # 因素A的水平总数r
        size2=np.shape(data)[1]    # 因素B的水平总数s
        count=np.shape(data)[2]    # 每对因素取值(A,B)=(a,b)的观察数/样本数

        avg=np.zeros((size1,size2))  #因素A和因素B每个水平组合(每格)的均值_Xij
        factor_avg_1=[]              #因素A每个水平(每行)的均值_Xi
        factor_avg_2=[]              #因素B每个水平(每列)的均值_Xj
        total_avg=0                  #样本总体均值_X

        for i in range(size1):
            for k in range(size2):
                avg[i][k]=np.average(data[i][k])
        
        for i in range(size1):
            factor_avg_1.append(np.average(data[i]))
        factor_avg_1=np.array(factor_avg_1)
        
        for i in range(size2):
            factor_avg_2.append(np.average(data[:,i]))
        factor_avg_2=np.array(factor_avg_2)

        total_avg=np.average(data)
        a_total_avg=np.array([total_avg for i in range(size1)])
        b_total_avg=np.array([total_avg for i in range(size2)])

        # 2. 计算sa=因素A平方和，sb=因素B平方和，sab=交互作用平方和，se=误差平方和，st=平方和总和=sa+sb+sab+se
        sa=size2*count*np.sum(np.square(factor_avg_1-a_total_avg))
        sb=size1*count*np.sum(np.square(factor_avg_2-b_total_avg))
        
        sab=0
        for i in range(size1):
            for j in range(size2):
                sab+=count*np.square(avg[i][j]-factor_avg_1[i]-factor_avg_2[j]+total_avg)
        
        se=0
        for i in range(size1):
            for j in range(size2):
                for k in range(count):
                    se+=np.sum(np.square(data[i][j][k]-avg[i][j]))
        
        st=sa+sb+sab+se

        # 3. 计算ta=因素A自由度，tb=因素B自由度，tab=交互作用自由度，te=误差自由度，tt=自由度总和=ta+tb+tab+te
        ta=size1-1
        tb=size2-1
        tab=(size1-1)*(size2-1)
        te=size1*size2*(count-1)
        tt=ta+tb+tab+te

        # 4. 计算_sa=因素A均方，_sb=因素B均方，_sab=交互作用均方，_se=误差均方
        _sa=sa/ta
        _sb=sb/tb
        _sab=sab/tab
        _se=se/te

        # 5. 计算fa=因素A的F比，fb=因素B的F比，fab=交互作用F比
        fa=_sa/_se
        fb=_sb/_se
        fab=_sab/_se

        return (sa,sb,sab,se,st,ta,tb,tab,te,tt,_sa,_sb,_sab,_se,fa,fb,fab)

        
        
        

            



        
        

        



        
