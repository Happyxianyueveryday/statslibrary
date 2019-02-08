 # GeneralStats一般统计量计算模块
   
   GeneralStats一般统计量计算模块包含常见统计量的计算方法，这些常见统计量包括：平均数，中位数，众数，分位数，极差，方差，标准差，偏度，峰度。
   
   ## 1. 引用头文件"GeneralStats.py"
    import GeneralStats as gs
   
   ## 2. 创建GeneralStats对象
   > 1. 创建GeneralStats对象不需要提供任何参数。
   
    gen=gs.GeneralStats()
   
   ## 3. 计算样本的平均值
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
    data众数值 =  [1 2 3 5]
    data1众数值 =  [1]
   
   ## 6. 计算样本的分位数
   > 1. 使用mode成员方法计算样本的众数。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。类型为np.array。
   > 3. 第二个参数fraction指定分位百分比，类型为float，fraction必须满足大于等于0且小于等于1。
   > 4. 第三个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   > 5. 第四个参数指定当所需分位数位于两个数据点i<j之间时要使用的插值方法，类型为str，取值范围为{'linear', 'lower', 'higher', 'midpoint'}。
   >> 若分位值fraction(0和1之间)计算得到的分位数下标不是整数，该下标两侧的数组元素分别为i和j，则:
   >> 'linear': i+fraction*(j-i)
   >> 'lower': i
   >> 'higher': j
   >> 'midpoint': (i+j)/2
   >> 若使用范围之外的可选参数，均将默认使用'midpoint'模式进行分位数的求解
     
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
    
   
   
