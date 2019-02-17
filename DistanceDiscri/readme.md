# DistanceDiscri距离判别模块
   
   DistanceDiscri距离判别模块包含距离判别算法的实现。
   
   ## 1. 引用头文件"DistanceDiscri.py"
    import DistanceDiscri
    
   ## 2. 创建一个DistanceDiscri对象
   > 0. 函数原型
   
    def __init__(self)
   
   > 1. 创建DistanceDiscri对象无需任何参数。
   
    dcr=DistanceDiscri.DistanceDiscri()
   
   ## 3. 使用训练集进行训练
   > 0. 函数原型
   
    def train(self, *data, rowvar=True, label=[])
   
   > 1. 使用train成员方法根据训练集进行训练，该方法从训练集中计算出各个类别的协方差矩阵和均值向量(重心)。
   > 2. 第一个参数\*data为不定参数，为不定数目的各个类别的训练集，类型为np,array。这些类别分别被编号为0,1,...
   > 3. 第二个参数rowvar指定每行或者每列代表一个变量，类型为bool。rowvar=True指定参数data的每行作为一个变量，每列作为一个样本向量；rowvar=False指定参数data的每列作为一个变量，每行作为一个样本向量。默认值为True。
   > 4. 第三个参数label指定各个类别所对应的类别名称，类型为list，list中的元素类型为str。该名称必须与各个类别的训练集在不定参数\*data的顺序一一对应。
    
    # 训练集
    train_0=np.array([[0.1, 0.2, 0.3],[0.4, 0.5, 0.6],[0.7, 0.8, 0.9]])
    train_1=np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    train_2=np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])
    train_3=np.array([[100, 200, 300],[400, 500, 600],[700, 800, 900]])
    
    dcr.train(train_0, train_1, train_2, train_3, rowvar=False, label=['类别A','类别B','类别C','类别D'])
    
   ## 4. 对测试集进行距离判别得到测试集样本所属的类别
   > 0. 函数原型
   
     def discriminate(self, data, rowvar=True)
   
   > 1. 使用discriminate成员方法判别测试集中的每个样本向量所属的类别，该方法必须在训练(即调用train成员方法）后使用。
   > 2. 第一个参数data为测试集样本矩阵，类型为np.array。
   > 3. 第二个参数rowvar指定每行或者每列代表一个变量，类型为bool。rowvar=True指定参数data的每行作为一个变量，每列作为一个样本向量；rowvar=False指定参数data的每列作为一个变量，每行作为一个样本向量。默认值为True。
   > 4. 各个样本的分类结果res，类型为list。其中res\[i]为第i个样本所属的类别标签。
   
     test_data=np.array([[7, 5.8, 9.2],[0.02, 0.14, 0.86],[87, 16, 5]])
     res=dcr.discriminate(test_data,rowvar=False)
   
   ## 附注：
   > 1. example文件夹中展示了使用该模块解决的，基于汽车评价数据集的一个微型的距离判别分析案例，具体请参见example文件夹下的readme.md说明文档。
   
   
   
   
   
   
   
      
