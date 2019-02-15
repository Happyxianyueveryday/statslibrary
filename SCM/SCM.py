import numpy as np

class SCM:

    # public functions

    def __init__(self, classdist='nearest', sampledist='euc', p=1):
        '''
        :__init__: 初始化标准聚类法类SCM
        :param classdist: 指定系统聚类法中所使用的类间距离的种类，取值范围为classdist={'nearest','farthest','average','centroid','square'}，默认值为classdist='nearest'
        :                 'nearest' : 类间最近距离，类间最近距离为两个类别之间样本距离的最小值
        :                 'farthest': 类间最远距离，类间最远距离为两个类别之间样本距离的最小值
        :                 'average' : 类间平均距离，类间平均距离为两个类别之间样本距离的平均值
        :                 'centroid': 类间重心距离，类间重心距离为两个类别的重心/均值向量之间的距离
        :                 'square'  : 类间离差平方和距离，类间离差平方和距离=类别a的直径-类别b的直径-类别a，b的合并大类直径
        :type classdist: str
        :param sampledist: 指定系统聚类法中所使用的样本间距离的种类，取值范围为sampledist={'euc','mah','man','min','cos'}，默认值为sampledist='euc'。若参数classdist=='square'，则此参数不使用
        :                  'euc': 样本间欧氏距离
        :                  'mah': 样本间马氏距离
        :                  'man': 样本间曼哈顿距离
        :                  'min': 样本间闵可夫斯基距离
        :                  'cos': 样本间余弦距离
        :type sampledist: str
        :param p: 闵可夫斯基距离的维数p，默认值为p=1。若参数classdist=='square'或者参数sampledist!='min'，则此参数不使用
        :type p: int
        '''
        self.__classdist=classdist     # 类间距离的种类
        self.__sampledist=sampledist   # 样本间距离的种类
        self.__p=p                     # 闵可夫斯基距离维数p

        return 
    
    def fit(self, data, kind=2, rowvar=False):
        '''
        :fit: 对样本数据集进行系统分类
        :param data: 原始样本矩阵或者数据集
        :type data: np.array
        :param rowvar: 指定每行代表一个变量或者每列代表一个变量；rowvar=True指定每行代表一个变量，即每列代表一个样本；rowvar=False指定每列代表一个变量，即每行代表一个样本。默认值为rowvar=False
        :type rowvar: bool
        :param kind: 指定分类中的类别数目，默认值为2
        :type kind: int
        :return: 分类结果，分类结果的形式为一个列表，该列表中包含若干个子列表，每个子列表代表一个类别，该子列表中含有该类别中的样本序号(样本序号为该样本向量在样本矩阵data中所在行下标或者列下标，从下标0开始)
        :rtype: list
        '''
        # 1. 将原始样本矩阵统一转换为每行代表一个样本向量，每列代表一个变量
        if rowvar==True:
            data=data.T
        
        # 2. 初始情况下将每个样本向量作为一个类别
        size=np.shape(data)[0]    # 样本向量数量
        count=np.shape(data)[1]   # 样本向量维数
        classlist=[[i] for i in range(size)]  # 初始情况下每个样本自身作为一个类别，classlist中仅存储样本的下标

        # 3. 正式进行聚类过程，每轮迭代的过程为: 首先计算各个类别之间的距离，然后取出两个距离最近的类别，将其合并为一个类别，一轮迭代结束，然后进行下一轮迭代，直到剩下的类别数量等于用户指定的类别数目
        while len(classlist)>kind:  
            # 3.1 计算各个类别之间的距离
            # 附注: 提交实验时没有注意，假期中recheck时发现本处代码存在较大优化空间，后续更新中将进行优化，每次迭代后，由于仅仅合并了两个类别，因此其他的类别之间的距离无需计算，仅仅只需要计算合并后得到的新类别与其他类别之间的距离即可
            kind_count=len(classlist)
            dist=np.full((kind_count,kind_count),float('inf'))   # 附注:不能初始化为全0矩阵，否则在后续矩阵求解min时会出现问题，因为不是所有的矩阵元素均用于储存距离
            for i in range(kind_count):
                for k in range(i+1,kind_count):   # 附注: 注意下标处理，类别m和类别n之间的距离只需要计算1次
                    if self.__classdist=='nearest':
                        a=np.vstack([data[classlist[i][m]] for m in range(len(classlist[i]))])
                        b=np.vstack([data[classlist[k][m]] for m in range(len(classlist[k]))])
                        dist[i][k]=self.__nearest_distance(a,b,mode=self.__sampledist,p=self.__p)
                    elif self.__classdist=='farthest':
                        a=np.vstack([data[classlist[i][m]] for m in range(len(classlist[i]))])
                        b=np.vstack([data[classlist[k][m]] for m in range(len(classlist[k]))])
                        dist[i][k]=self.__farthest_distance(a,b,mode=self.__sampledist,p=self.__p)
                    elif self.__classdist=='average':
                        a=np.vstack([data[classlist[i][m]] for m in range(len(classlist[i]))])
                        b=np.vstack([data[classlist[k][m]] for m in range(len(classlist[k]))])
                        dist[i][k]=self.__average_distance(a,b,mode=self.__sampledist,p=self.__p)
                    elif self.__classdist=='centroid':
                        a=np.vstack([data[classlist[i][m]] for m in range(len(classlist[i]))])
                        b=np.vstack([data[classlist[k][m]] for m in range(len(classlist[k]))])
                        dist[i][k]=self.__centroid_distance(a,b,mode=self.__sampledist,p=self.__p)
                    elif self.__classdist=='square':
                        a=np.vstack([data[classlist[i][m]] for m in range(len(classlist[i]))])
                        b=np.vstack([data[classlist[k][m]] for m in range(len(classlist[k]))])
                        dist[i][k]=self.__square_distance(a,b)
            # 3.2 选择距离最小的两个类别进行合并，若有多对类别的距离相同，则随机选择一对类别进行合并
            tar=np.where(dist==np.min(dist))      #注意取min而非max
            a=min(np.random.choice(tar[0]),np.random.choice(tar[1]))   # 待合并的类别较小下标a
            b=max(np.random.choice(tar[0]),np.random.choice(tar[1]))   # 待合并的类别较大下标b
            temp=classlist[b]
            classlist.pop(b)             # 注意列表顺序，先删除较大下标的类别b
            classlist[a]+=temp           # 将类别b并入类别a

        return classlist
    
    def reset(self, classdist='nearest', sampledist='euc', p=1):
        '''
        :reset: 重新设置标准聚类法类SCM的聚类距离种类
        :param classdist: 指定系统聚类法中所使用的类间距离的种类，取值范围为classdist={'nearest','farthest','average','centroid','square'}，默认值为classdist='nearest'
        :                 'nearest' : 类间最近距离，类间最近距离为两个类别之间样本距离的最小值
        :                 'farthest': 类间最远距离，类间最远距离为两个类别之间样本距离的最小值
        :                 'average' : 类间平均距离，类间平均距离为两个类别之间样本距离的平均值
        :                 'centroid': 类间重心距离，类间重心距离为两个类别的重心/均值向量之间的距离
        :                 'square'  : 类间离差平方和距离，类间离差平方和距离=类别a的直径-类别b的直径-类别a，b的合并大类直径
        :type classdist: str
        :param sampledist: 指定系统聚类法中所使用的样本间距离的种类，取值范围为sampledist={'euc','mah','man','min','cos'}，默认值为sampledist='euc'。若参数classdist=='square'，则此参数不使用
        :                  'euc': 样本间欧氏距离
        :                  'mah': 样本间马氏距离
        :                  'man': 样本间曼哈顿距离
        :                  'min': 样本间闵可夫斯基距离
        :                  'cos': 样本间余弦距离
        :type sampledist: str
        :param p: 闵可夫斯基距离的维数p，默认值为p=1。若参数classdist=='square'或者参数sampledist!='min'，则此参数不使用
        :type p: int
        '''
        self.__classdist=classdist     # 类间距离的种类
        self.__sampledist=sampledist   # 样本间距离的种类
        self.__p=p                     # 闵可夫斯基距离维数p

        return 

    # private functions

    # 5种样本距离求解方法
    def __euc_distance(self, a, b):
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

    def __man_distance(self, a, b):
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

    def __min_distance(self, a, b, p):
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
    
    def __cos_distance(self, a, b):
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
    
    # 5种类间距离计算方法
    def __nearest_distance(self, a, b, mode='euc', p=1):
        '''
        :__nearest_distance: 求解类间的最短距离。类间的最短距离定义为两个类的样本之间的距离的最小值
        :param a: 类别a的样本矩阵，矩阵a的每一行代表类别中的一个样本向量
        :type a: np.array
        :param b: 类别b的样本矩阵，矩阵b的每一行代表类别中的一个样本向量
        :type b: np.array
        :param mode: 指定样本之间的距离定义，取值范围为mode={'euc','mah','man','min','cos'}
        :type mode: str
        :param p: 闵可夫斯基距离的维数p，若不使用闵可夫斯基距离，即mode!='min'，则该参数可省略，默认值为p=1
        :type p: int
        :return: 类别a和类别b之间的最短距离
        :rtype: float
        '''
        flag=0
        if a.ndim==1:     # 处理向量的一维情况的方法均为向量矩阵化
            a=np.array([a])
        if b.ndim==1:
            b=np.array([b])
            flag=1

        size1=np.shape(a)[0]    # 类别a的样本数量
        size2=np.shape(b)[0]    # 类别b的样本数量

        res=float('inf')    # 初始值为正无穷

        if mode=='euc':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__euc_distance(a[i],b[k])
                    res=tempres if tempres<res else res
        elif mode=='mah':
            for i in range(size1):
                for k in range(size2):
                    # 计算类别b的协方差矩阵: 若样本数小于特征数，这时协方差矩阵无法求逆，则这时协方差矩阵直接设为I(对角阵)；否则按照正常方法求解协方差矩阵
                    cov_vec=np.cov(b,rowvar=False) 
                    avg=np.average(b,axis=0)       # 计算类别b的均值向量
                    tempres=self.__mah_distance(a[i],avg,cov_vec)
                    res=tempres if tempres<res else res
        elif mode=='man':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__man_distance(a[i],b[k])
                    res=tempres if tempres<res else res
        elif mode=='min':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__min_distance(a[i],b[k],p)
                    res=tempres if tempres<res else res
        else:
            for i in range(size1):
                for k in range(size2):
                    # 余弦距离范围为[-1,1]，余弦距离为1表示两个类别相近，余弦距离为-1表示两个类别完全相远
                    # 因此使用余弦差=1-余弦距离表征类别之间的距离，范围为[0,2]，余弦差越小表示类别之间越相近，否则类别之间越相远
                    tempres=1-self.__cos_distance(a[i],b[k])
                    res=tempres if tempres<res else res
        return res
    
    def __farthest_distance(self, a, b, mode='euc', p=1):
        '''
        :__farthest_distance: 求解类间的最长距离。类间的最长距离定义为两个类的样本之间的距离的最大值
        :param a: 类别a的样本矩阵，矩阵a的每一行代表类别中的一个样本向量
        :type a: np.array
        :param b: 类别b的样本矩阵，矩阵b的每一行代表类别中的一个样本向量
        :type b: np.array
        :param mode: 指定样本之间的距离定义，取值范围为mode={'euc','mah','man','min','cos'}
        :type mode: str
        :param p: 闵可夫斯基距离的维数p，若不使用闵可夫斯基距离，即mode!='min'，则该参数可省略，默认值为p=1
        :type p: int
        :return: 类别a和类别b之间的最长距离
        :rtype: float
        '''
        flag=0
        if a.ndim==1:     # 处理向量的一维情况的方法均为向量矩阵化
            a=np.array([a])
        if b.ndim==1:
            b=np.array([b])
            flag=1
        
        size1=np.shape(a)[0]    # 类别a的样本数量
        size2=np.shape(b)[0]    # 类别b的样本数量

        res=float('-inf')      # 初始值为负无穷

        if mode=='euc':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__euc_distance(a[i],b[k])
                    res=tempres if tempres>res else res
        elif mode=='mah':
            for i in range(size1):
                for k in range(size2):
                    # 计算类别b的协方差矩阵: 若只有一个样本，则协方差矩阵为全0阵
                    cov_vec=np.cov(b,rowvar=False)
                    avg=np.average(b,axis=0)           # 计算类别b的均值向量
                    tempres=self.__mah_distance(a[i],avg,cov_vec)
                    res=tempres if tempres>res else res
        elif mode=='man':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__man_distance(a[i],b[k])
                    res=tempres if tempres>res else res
        elif mode=='min':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__min_distance(a[i],b[k],p)
                    res=tempres if tempres>res else res
        else:
            for i in range(size1):
                for k in range(size2):
                    # 余弦距离范围为[-1,1]，余弦距离为1表示两个类别相近，余弦距离为-1表示两个类别完全相远
                    # 因此使用余弦差=1-余弦距离表征类别之间的距离，范围为[0,2]，余弦差越小表示类别之间越相近，否则类别之间越相远
                    tempres=1-self.__cos_distance(a[i],b[k])    
                    res=tempres if tempres>res else res
        return res

    def __average_distance(self, a, b, mode='euc', p=1):
        '''
        :__average_distance: 求解类间的平均距离。类间的平均距离定义为所有两个类的样本之间的距离的平均值
        :param a: 类别a的样本矩阵，矩阵a的每一行代表类别中的一个样本向量
        :type a: np.array
        :param b: 类别b的样本矩阵，矩阵b的每一行代表类别中的一个样本向量
        :type b: np.array
        :param mode: 指定样本之间的距离定义，取值范围为mode={'euc','mah','man','min','cos'}
        :type mode: str
        :param p: 闵可夫斯基距离的维数p，若不使用闵可夫斯基距离，即mode!='min'，则该参数可省略，默认值为p=1
        :type p: int
        :return: 类别a和类别b之间的平均距离
        :rtype: float
        '''
        flag=0
        if a.ndim==1:     # 处理向量的一维情况的方法均为向量矩阵化
            a=np.array([a])
        if b.ndim==1:
            b=np.array([b])
            flag=1
        
        size1=np.shape(a)[0]    # 类别a的样本数量
        size2=np.shape(b)[0]    # 类别b的样本数量

        res=0.0      #初始值为0.0

        if mode=='euc':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__euc_distance(a[i],b[k])
                    res+=tempres
        elif mode=='mah':
            for i in range(size1):
                for k in range(size2):
                    # 计算类别b的协方差矩阵: 若只有一个样本，则协方差矩阵为全0阵
                    cov_vec=np.cov(b,rowvar=False) 
                    avg=np.average(b,axis=0)        #计算类别b的均值向量
                    tempres=self.__mah_distance(a[i],avg,cov_vec)
                    res+=tempres
        elif mode=='man':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__man_distance(a[i],b[k])
                    res+=tempres
        elif mode=='min':
            for i in range(size1):
                for k in range(size2):
                    tempres=self.__min_distance(a[i],b[k],p)
                    res+=tempres
        else:
            for i in range(size1):
                for k in range(size2):
                    # 余弦距离范围为[-1,1]，余弦距离为1表示两个类别相近，余弦距离为-1表示两个类别完全相远
                    # 因此使用余弦差=1-余弦距离表征类别之间的距离，范围为[0,2]，余弦差越小表示类别之间越相近，否则类别之间越相远
                    tempres=1-self.__cos_distance(a[i],b[k])    
                    res+=tempres

        res=res/(size1*size2)
        return res
    
    def __centroid_distance(self, a, b, mode='euc', p=1):
        '''
        :__centroid_distance: 求解类间的重心距离。类间的平均距离定义为两个类的样本的均值向量之间的距离
        :param a: 类别a的样本矩阵，矩阵a的每一行代表类别中的一个样本向量
        :type a: np.array
        :param b: 类别b的样本矩阵，矩阵b的每一行代表类别中的一个样本向量
        :type b: np.array
        :param mode: 指定样本之间的距离定义，取值范围为mode={'euc','mah','man','min','cos'}
        :type mode: str
        :param p: 闵可夫斯基距离的维数p，若不使用闵可夫斯基距离，即mode!='min'，则该参数可省略，默认值为p=1
        :type p: int
        :return: 类别a和类别b之间的重心距离
        :rtype: float
        '''
        if a.ndim==1:     # 处理向量的一维情况的方法均为向量矩阵化
            a=np.array([a])
        if b.ndim==1:
            b=np.array([b])
        
        res=0.0      #初始值为0.0
        avg_a=np.average(a,axis=0)   #类别a的重心/均值向量
        avg_b=np.average(b,axis=0)   #类别b的重心/均值向量

        if mode=='euc':
            res=self.__euc_distance(avg_a,avg_b)
        elif mode=='mah':
            cov_vec=np.cov(b,rowvar=False)  #计算类别b的协方差矩阵
            res=self.__mah_distance(avg_a,avg_b,cov_vec)
        elif mode=='man':
            res=self.__man_distance(avg_a,avg_b)
        elif mode=='min':
            res=self.__min_distance(avg_a,avg_b,p)
        else:
            # 余弦距离范围为[-1,1]，余弦距离为1表示两个类别相近，余弦距离为-1表示两个类别完全相远
            # 因此使用余弦差=1-余弦距离表征类别之间的距离，范围为[0,2]，余弦差越小表示类别之间越相近，否则类别之间越相远
            res=1-self.__cos_distance(avg_a,avg_b)    
        
        return res

    def __square_distance(self, a, b):
        '''
        :__square_distance: 求解类间的离差平方和距离。类间的离差平方和距离的定义请参见wiki
        :param a: 类别a的样本矩阵，矩阵a的每一行代表类别中的一个样本向量
        :type a: np.array
        :param b: 类别b的样本矩阵，矩阵b的每一行代表类别中的一个样本向量
        :type b: np.array
        :return: 类别a和类别b之间的离差平方和距离
        :rtype: float
        '''
        if a.ndim==1:     # 处理向量的一维情况的方法均为向量矩阵化
            a=np.array([a])
        if b.ndim==1:
            b=np.array([b])
        
        size1=np.shape(a)[0]    # 类别a的样本数量
        size2=np.shape(b)[0]    # 类别b的样本数量

        avg_a=np.average(a,axis=0)   #类别a的重心/均值向量
        avg_b=np.average(b,axis=0)   #类别b的重心/均值向量
        avg_all=np.average(np.vstack([a,b]),axis=0)   #类别a和类别b的大类重心/均值向量

        res=0      #最终离差平方和距离结果

        # 1. 分别计算类别a和类别b的直径
        da=0.0
        for i in range(size1):
            da+=np.dot(a[i]-avg_a,(a[i]-avg_a).T)
        
        db=0.0
        for i in range(size2):
            db+=np.dot(b[i]-avg_b,(b[i]-avg_b).T)
        
        # 2. 计算类别a和类别b的大类直径
        dab=0.0
        for i in range(size1):
            dab+=np.dot(a[i]-avg_all,(a[i]-avg_all).T)
        for i in range(size2):
            dab+=np.dot(b[i]-avg_all,(b[i]-avg_all).T)
        
        res=dab-da-db
        return res




        
        
        
        