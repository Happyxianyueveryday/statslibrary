# PCA主成分分析模块

  PCA主成分分析模块包括主成分分析算法。
  
  ## 1. 引用头文件"PCA.py"
    import PCA as pc
    
  ## 2. 创建一个PCA对象
  > 1. PCA类的初始化需要一个参数。
  > 2. 该唯一参数n_components为PCA降维后所保留的特征数或者维数，类型为int，默认值为2。该值不得超过原始样本集数据的总特征数。
  
    pca = pc.PCA(n_components=1)
    
  ## 3. 使用训练集进行PCA主成分分析
  > 1. 使用fit成员方法用训练集进行PCA主成分分析的训练过程。
  > 2. 第一个参数data为训练集矩阵，即进行PCA分析的数据集，类型为np.array。在该方法中首先会对训练集矩阵进行标准化。
  > 3. 第二个参数rowvar指定参数data的每一行或者每一列代表一个特征，类型为bool。rowvar=True指定每一行代表一个特征，即每一列代表一个样本向量；rowvar=False指定每一列代表一个特征，即每一行代表一个样本向量，默认值为rowvar=True。
  
    data = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca.fit(data,rowvar=False)
    
  ## 4. 使用测试集进行PCA降维
  > 1. 使用transform成员方法对测试集进行PCA降维。
  > 2. 第一个参数data为测试集矩阵，即进行PCA降维的数据集，类型为np.array。在该方法中首先会对测试集矩阵进行标准化。
  > 3. 第二个参数rowvar指定参数data的每一行或者每一列代表一个特征，类型为bool。rowvar=True指定每一行代表一个特征，即每一列代表一个样本向量；rowvar=False指定每一列代表一个特征，即每一行代表一个样本向量，默认值为rowvar=True。
  
    data = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    res = pca.transform(data,rowvar=False)
    print("使用本库进行计算得到的PCA降维结果为: res = ", res)
    
    >>> 输出
    使用本库进行计算得到的PCA降维结果为: res =  [[ 1.38340578]
    [ 2.22189802]
    [ 3.6053038 ]
    [-1.38340578]
    [-2.22189802]
    [-3.6053038 ]]
    
  > 可以将上述结果与sklearn.decomposition.PCA的结果进行对比以验证其正确性，如下所示。
  
    from sklearn.decomposition import PCA
    pca1 = PCA(n_components=1)
    res = pca1.fit_transform(data)
    print("使用sklearn.decomposition.PCA 验证的结果为: res = ", res)
    
    >>> 输出
    使用sklearn.decomposition.PCA 验证的结果为: res =  [[ 1.38340578]
    [ 2.22189802]
    [ 3.6053038 ]
    [-1.38340578]
    [-2.22189802]
    [-3.6053038 ]]
   
    
  ## 5. 输出
   
   
   
  
    
   
  
    

