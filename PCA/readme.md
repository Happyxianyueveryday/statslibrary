# PCA主成分分析模块

  PCA主成分分析模块包括主成分分析算法。
  
  ## 1. 引用头文件"PCA.py"
    import PCA as pc
    
  ## 2. 创建一个PCA对象
  > 0. 函数原型
  
     def __init__(self, n_components=2)
  
  > 1. PCA类的初始化需要一个参数。
  > 2. 该唯一参数n_components为PCA降维后所保留的特征数或者维数，类型为int，默认值为2。该值不得超过原始样本集数据的总特征数。
  
    pca = pc.PCA(n_components=1)
    
  ## 3. 使用训练集进行PCA主成分分析
  > 0. 函数原型
  
     def fit(self, data, rowvar=True)
  
  > 1. 使用fit成员方法用训练集进行PCA主成分分析的训练过程。
  > 2. 第一个参数data为训练集矩阵，即进行PCA分析的数据集，类型为np.array。在该方法中首先会对训练集矩阵进行标准化。
  > 3. 第二个参数rowvar指定参数data的每一行或者每一列代表一个特征，类型为bool。rowvar=True指定每一行代表一个特征，即每一列代表一个样本向量；rowvar=False指定每一列代表一个特征，即每一行代表一个样本向量，默认值为rowvar=True。
  
    data = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca.fit(data,rowvar=False)
    
  ## 4. 使用测试集进行PCA降维
  > 0. 函数原型
  
     def transform(self, data, rowvar=True)
  
  > 1. 使用transform成员方法对测试集进行PCA降维。特别地，在使用该方法进行PCA降维之前，首先应当调用fit进行PCA主成分分析。
  > 2. 第一个参数data为测试集矩阵，即进行PCA降维的数据集，类型为np.array。在该方法中首先会对测试集矩阵进行标准化。
  > 3. 第二个参数rowvar指定参数data的每一行或者每一列代表一个特征，类型为bool。rowvar=True指定每一行代表一个特征，即每一列代表一个样本向量；rowvar=False指定每一列代表一个特征，即每一行代表一个样本向量，默认值为rowvar=True。
  > 4. 返回值为降维后的测试集矩阵，其中每一列代表一个特征，类型为np.array。
  
    data = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca.fit(data,rowvar=False)
    res = pca.transform(data,rowvar=False)
    print("使用本库进行计算得到的PCA降维结果为: res = ", res)
    
    >>> 输出
    使用本库进行计算得到的PCA降维结果为: res =  [[ 1.38340578]
    [ 2.22189802]
    [ 3.6053038 ]
    [-1.38340578]
    [-2.22189802]
    [-3.6053038 ]]
    
  > 可以将上述结果与sklearn库的sklearn.decomposition.PCA类的结果进行对比以验证其正确性，如下所示。
  
    from sklearn.decomposition import PCA
    pca1 = PCA(n_components=1)
    data = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    res = pca1.fit_transform(data)
    print("使用sklearn.decomposition.PCA 验证的结果为: res = ", res)
    
    >>> 输出
    使用sklearn.decomposition.PCA 验证的结果为: res =  [[ 1.38340578]
    [ 2.22189802]
    [ 3.6053038 ]
    [-1.38340578]
    [-2.22189802]
    [-3.6053038 ]]
   
    
  ## 5. 输出特征的权重
  > 0. 函数原型
  
     def variance_ratio(self, only=False)
  
  > 1. 使用variance_ratio方法输出特征的权重。特别地，在使用该方法获得特征权重之前，首先应当调用fit进行PCA主成分分析。
  > 2. 唯一参数only指定是否仅保留降维后的特征的权重，类型为bool。only=True指定仅保留降维后的n_components个特征的权重，only=False则保留全部特征的权重，默认值为only=False。
  > 3. 返回值为各个特征权重的向量，类型为np.array。
  
    pca1 = PCA(n_components=1)
    data = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca.fit(data,rowvar=False)
    ratio = pca.variance_ratio(only=True)
    print("各特征的权重为: ratio = ",ratio)
   
    >>> 输出
    各特征的权重为: ratio =  [0.99244289]
  
  > 可以将上述结果与sklearn库的sklearn.decomposition.PCA类的结果进行对比以验证其正确性，如下所示。
    
    ratio = pca1.explained_variance_ratio_
    print("各特征的权重为: ratio = ",ratio)
    
    >>> 输出
    各特征的权重为: ratio =  [0.99244289]
    
   ## 6. 修改保留的特征数
   > 0. 函数原型
  
     def set_components(self, n_components=2)
  
   > 1. 使用set_components方法修改需要保留的特征数。特别地，修改需要保留的特征数后，需要重新使用fit成员方法进行训练。
   > 2. 唯一参数n_components指定新的需要保留的特征数，类型为int。
   
    pca = pc.PCA(n_components=1)
    pca.set_components(n_components=2)
    
   ## 7. 输出各个特征对应的特征值和特征向量
   > 0. 函数原型
   
      def eigenvalue(self, only=False)
      def eigenvector(self, only=False)
   
   > 1. 分别使用eigenvalue, eigenvector成员方法输出各个特征对应的特征值和特征向量。特别地，在使用该方法获得特征值或特征向量之前，首先应当调用fit进行PCA主成分分析。
   > 2. 这两个成员方法的唯一参数only指定是否仅保留降维后的特征的特征值或特征向量，类型为bool。only=True指定仅保留降维后的n_components个特征的特征值或特征向量，only=False则保留全部特征的特征值或特征向量，默认值为only=False。
   > 3. eigenvalue, eigenvector成员方法的返回值分别为特征值组成的向量和特征向量组成的矩阵，类型均为np.array。
   
    data = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    pca = pc.PCA(n_components=1)
    pca.fit(data,rowvar=False)
    value=pca.eigenvalue(only=True)
    vector=pca.eigenvector(only=True)
    print("各特征的特征值为: ",pca.eigenvalue(only=False))
    print("各特征的特征向量为: ",pca.eigenvector(only=False))
    
    >>> 输出
    各特征的特征值为:  [7.93954312 0.06045688]
    各特征的特征向量为:  [[-0.83849224  0.54491354]
    [-0.54491354 -0.83849224]]
   
   ## 附注：
   > 1. example.py中提供了一份使用PCA模块的示例代码。
  
  
   
   
   
  
    
   
  
    

