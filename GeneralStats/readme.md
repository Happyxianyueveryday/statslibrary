 # GeneralStats一般统计量计算模块
   
   GeneralStats一般统计量计算模块包含常见统计量的计算与求解方法，这些常见统计量包括：平均数，中位数，众数，分位数，极差，方差，标准差，偏度，峰度。
   
   ## 1. 引用头文件"GeneralStats.py"
    import GeneralStats as gs
   
   ## 2. 创建GeneralStats对象
   > 1. 创建GeneralStats对象不需要提供任何参数。
   
    gen=gs.GeneralStats()
   
   ## 3. 计算样本的平均值
   > 0. 函数原型
   
      def average(self, data, rowvar=True)
   
   > 1. 使用average成员方法计算样本的平均值。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.average(data,rowvar=True)
    res1=gen.average(data1,rowvar=True)
    print("data平均值 = ",res)
    print("data1平均值 = ",res1)
    
    >>> 输出
    data平均值 =  [[1.8 3.  2.8 3.8]]
    data1平均值 =  [3.]
   
   ## 4. 计算样本的中位值
   > 0. 函数原型
   
      def median(self, data, rowvar=True)
   
   > 1. 使用median成员方法计算样本的中位值。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.median(data,rowvar=True)
    res1=gen.median(data1,rowvar=True)
    print("data中位值 = ",res)
    print("data1中位值 = ",res1)
    
    >>> 输出
    data中位值 =  [[2. 3. 3. 4.]]
    data1中位值 =  [3]
   
   ## 5. 计算样本的众数
   > 0. 函数原型
   
      def mode(self, data, rowvar=True)
   
   > 1. 使用mode成员方法计算样本的众数。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.mode(data,rowvar=True)
    res1=gen.mode(data1,rowvar=True)
    print("data众数值 = ",res)
    print("data1众数值 = ",res1)
    
    >>> 输出
    data众数值 =  [[1 2 3 5]]
    data1众数值 =  [1]
   
   ## 6. 计算样本的分位数
   > 0. 函数原型
   
      def quantile(self, data, fraction, rowvar=True, interpolation='linear')
   
   > 1. 使用quantile成员方法计算样本的分位数。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数fraction指定分位百分比，类型为float，fraction必须满足大于等于0且小于等于1。
   > 4. 第三个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   > 5. 第四个参数指定当所需分位数位于两个数据点i<j之间时要使用的插值方法，类型为str，取值范围为{'linear', 'lower', 'higher', 'midpoint'}。若分位值fraction(0和1之间)计算得到的分位数下标不是整数，该下标两侧的数组元素分别为i和j，则:
   > + 'linear': i+fraction*(j-i)
   > + 'lower': i
   > + 'higher': j
   > + 'midpoint': (i+j)/2
   > + 若使用该参数取值范围之外的其他值，均将默认使用'midpoint'模式进行分位数的求解
     
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.quantile(data,0.5,rowvar=True,interpolation='lower')      #若元素个数为偶数，则模式为'midpoint'的0.5分位数值等价于中位数
    res1=gen.quantile(data1,0.5,rowvar=True,interpolation='lower')    #若元素个数为奇数，则模式为'lower'的0.5分位数值等价于中位数
    print("data 0.5分位数值 = ",res)
    print("data1 0.5分位数值 = ",res1)
    res=gen.quantile(data,0.25,rowvar=True,interpolation='lower')
    res1=gen.quantile(data1,0.25,rowvar=True,interpolation='lower')
    print("data 0.25分位数值s = ",res)
    print("data1 0.25分位数值 = ",res1)
    res=gen.quantile(data,0.75,rowvar=True,interpolation='lower')
    res1=gen.quantile(data1,0.75,rowvar=True,interpolation='lower')
    print("data 0.75分位数值 = ",res)
    print("data1 0.75分位数值 = ",res1)
    res=gen.quantile(data,1.0,rowvar=True,interpolation='lower')
    res1=gen.quantile(data1,1.0,rowvar=True,interpolation='lower')
    print("data 1.0分位数值 = ",res)
    print("data1 1.0分位数值 = ",res1)
    
    >>> 输出
    data 0.5分位数值 =  [[2. 3. 3. 4.]]
    data1 0.5分位数值 =  [3]
    data 0.25分位数值s =  [[1. 2. 3. 3.]]
    data1 0.25分位数值 =  [2]
    data 0.75分位数值 =  [[2. 3. 3. 5.]]
    data1 0.75分位数值 =  [4]
    data 1.0分位数值 =  [[3. 5. 4. 5.]]
    data1 1.0分位数值 =  [5]
    
   ## 7. 计算样本的极差
   > 0. 函数原型
   
      def range(self, data, rowvar=True)
   
   > 1. 使用range成员方法计算样本的极差。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.range(data,rowvar=True)
    res1=gen.range(data1,rowvar=True)
    print("data极差 = ",res)
    print("data1极差 = ",res1)
    
    >>> 输出
    data极差 =  [[2. 3. 3. 3.]]
    data1极差 =  [4]
    
   ## 8. 计算样本的方差
   > 0. 函数原型
   
      def variance(self, data, rowvar=True)
   
   > 1. 使用variance成员方法计算样本的方差。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.variance(data,rowvar=True)
    res1=gen.variance(data1,rowvar=True)
    print("data方差 = ",res)
    print("data1方差 = ",res1)
    
    >>> 输出
    data方差 =  [[0.56 1.2  0.96 1.36]]
    data1方差 =  [2.]

   ## 9. 计算样本的标准差
   > 0. 函数原型
   
      def standard_dev(self, data, rowvar=True)
   
   > 1. 使用standard_dev成员方法计算样本的标准差。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
  
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.standard_dev(data,rowvar=True)
    res1=gen.standard_dev(data1,rowvar=True)
    print("data标准差 = ",res)
    print("data1标准差 = ",res1)
    
    >>> 输出
    data标准差 =  [[0.74833148 1.09544512 0.9797959  1.16619038]]
    data1标准差 =  [1.41421356]
   
   ## 10. 计算样本的偏度
   > 0. 函数原型
   
      def skewness(self, data, rowvar=True)
   
   > 1. 使用skewness成员方法计算样本的偏度。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
  
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.skewness(data,rowvar=True)
    res1=gen.skewness(data1,rowvar=True)
    print("data偏度 = ",res)
    print("data1偏度 = ",res1)
    res=np.array([skew(data[0]),skew(data[1]),skew(data[2]),skew(data[3])])
    print("使用scipy skew方法验证的data偏度 = ",res)
    res1=np.array(skew(data1))
    print("使用scipy skew方法验证的data1偏度 = ",res1)
    
    >>> 输出
    data偏度 =  [[ 0.3436216   0.91287093 -0.86752762 -0.36317347]]
    data1偏度 =  [0.]
    使用scipy skew方法验证的data偏度 =  [ 0.3436216   0.91287093 -0.86752762 -0.36317347]
    使用scipy skew方法验证的data1偏度 =  0.0
    
    
   ## 11. 计算样本的峰度
    > 0. 函数原型
   
      def kurtosis(self, data, rowvar=True)
   
   > 1. 使用kurtosis成员方法计算样本的峰度。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([53, 61, 49, 66, 78, 47])
    res=gen.kurtosis(data,rowvar=True)
    res1=gen.kurtosis(data1,rowvar=True)
    print("data峰度 = ",res)
    print("data1峰度 = ",res1)
    data_0=pd.Series(data[0])
    data_1=pd.Series(data[1])
    data_2=pd.Series(data[2])
    data_3=pd.Series(data[3])
    print("使用pandas kurt方法验证的data峰度 = ",[data_0.kurt(),data_1.kurt(),data_2.kurt(),data_3.kurt()])
    data1=pd.Series(data1)
    print("使用pandas kurt方法验证的data1峰度 = ",data1.kurt())
    
    >>> 输出
    data峰度 =  [[-0.6122449   2.          2.91666667 -1.48788927]]
    data1峰度 =  [-0.26316554]
    使用pandas kurt方法验证的data峰度 =  [-0.6122448979591839, 2.0, 2.9166666666666625, -1.4878892733564015]
    使用pandas kurt方法验证的data1峰度 =  -0.2631655441038463
   
    
   
   
