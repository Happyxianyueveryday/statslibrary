# Kmeans聚类模块

  Kmeans聚类模块包含Kmeans聚类算法(K-means)，以及准确率分析等算法的具体实现。
  
  ## 1. 引用头文件"Kmeans.py"
  
    import Kmeans as km
   
  ## 2. 创建一个Kmeans对象
  > 0. 函数原型
  
     def __init__(self, data, kind=2, rowsam=True)
  
  > 1. Kmeans聚类对象的默认构造函数需要三个参数。
  > 2. 第一个参数data为需要聚类的样本集矩阵，类型为二维np.array。
  > 3. 第二个参数kind指定聚类中的类别数目，类型为int，默认值为kind=2。
  > 4. 第三个参数rowsam指定样本集矩阵(也即第一个参数data)的行或者列作为样本向量，rowsam=True指定data的每一行代表一个样本向量，rowsam=False指定data的每一列代表一个样本向量。
  
    data=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])   #样本集矩阵
    kmeans=km.Kmeans(data,kind=2,rowsam=True)   #6个样本向量进行二分类
  
  ## 3. 进行Kmeans聚类
  > 0. 函数原型
  
     def cluster(self)
  
  > 1. 使用cluster成员方法进行Kmeans聚类，该方法无需任何参数。
  > 2. 聚类过程中，样本集矩阵中的每个样本向量(每行或者每列)将被依次编号为0,1,2,...，聚类中的各个类别将被依次编号为0,1,2,...，聚类过程存在一定的随机性。
  > 3. 返回值为聚类结果res，类型为list，聚类结果res的格式为：二维list数组形式，其中res[i]即为编号为i的类别所含有的样本编号的列表。
  
  ## 4. 计算准确度
  > 0. 函数原型
  
     def accuracy(self, real)
  
  > 1. 使用accuracy成员方法计算准确度，该方法必须在聚类完成后使用才能得到正确结果，该成员方法接受一个参数。
  > 2. 本方法的准确度定义是：将每个类别中出现次数最多的真实标签作为整个类别的标签，样本的标签与所在类别标签相等即认为成功预测，最终准确率即为成功预测的样本数量除以样本总数。
  > 3. 第一个参数real为样本真实分类标签结果，类型为一维np.array，其中real[i]即为编号为i的样本的真实类别标签
  > 4. 返回值为本次Kmeans聚类的准确度，类型为float，该准确度在0和1之间。
 
    label=np.array([0,0,0,1,1,1])   #样本集标签：即data的前三个向量属于类别0，后三个属于类别1
    
    res=kmeans.cluster()
    print("聚类结果为 res = ", res)
    
    acc=kmeans.accuracy(label)
    print("聚类准确度为 acc = ",acc)
    
    >>> 输出结果1
    聚类结果为 res =  [[0, 1, 2], [3, 4, 5]]
    聚类准确度为 acc =  1.0
    
    >>> 输出结果2
    聚类结果为 res =  [[2, 3, 4, 5], [0, 1]]
    聚类准确度为 acc =  0.8333333333333334
    
  ## 5. 获得聚类的样本集矩阵和类别数
  > 0. 函数原型
  
     def getdata(self, rowsam=True)
     def getkind(self)
  
  > 1. 使用getdata和getkind成员方法分别获取样本集矩阵和类别数。
  > 2. 该两个方法调用时均无需任何参数。
  > 3. getdata的返回值为样本集矩阵，类型为二维np.array；getkind的返回值为类别数，类型为int。
  
  ## 6. 重新载入样本集矩阵和重新修改类别数
  > 0. 函数原型
  
     def reload(self, data, kind=2, rowsam=True)
  
  > 1. 使用reload成员方法重新设定样本集矩阵和类别数，该方法接受三个参数。
  > 2. 第一个参数data为需要聚类的样本集矩阵，类型为二维np.array。
  > 3. 第二个参数kind指定聚类中的类别数目，类型为int，默认值为kind=2。
  > 4. 第三个参数rowsam指定样本集矩阵(也即第一个参数data)的行或者列作为样本向量，rowsam=True指定data的每一行代表一个样本向量，rowsam=False指定data的每一列代表一个样本向量。
    
