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
    
   
   
