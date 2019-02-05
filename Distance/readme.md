# Distance距离度量模块
   
   Distance距离度量模块包括6种统计分析中常用的距离度量——欧氏距离，马氏距离，曼哈顿距离，闵可夫斯基距离，标准欧氏距离和余弦距离。
   
   ## 1. 引用头文件"Distance.py"
    import Distance as di

   ## 2. 创建一个Distance对象
   > 1. 初始化一个Pattern对象无需提供任何参数。
   
    dis=di.Distance()
    
   ## 3. 求解欧氏距离
   > 1. 使用euc_distance成员方法来计算和求解欧氏距离。
   > 2. 第一个参数为第一个向量a，类型为np.array。
   > 3. 第二个参数为第二个向量b，类型为np.array。
    
    a=np.array([1.5 for i in range(128)])
    b=np.array([2 for i in range(128)])
    res=dis.euc_distance(a,b)  #求解欧氏距离
    print("欧氏距离 = ", res)        
    
   ## 4. 求解马氏距离
   > 1. 使用mah_distance成员方法来计算和求解马氏距离，该马氏距离成员函数有如下三种常见的应用场景，对应于不同的参数调用方法。假设第一个参数为向量a，第二个参数为向量b，第三个参数为协方差矩阵cov_vec。
   > 2. 场景1：计算一个未分类向量到一个类别的马氏距离: 这时a为未分类向量，b为一个类别的均值向量，cov_vec为该类别的协方差矩阵，返回未分类变量a到某个类别的马氏距离。
   > 3. 场景2：计算同一个类别中两个样本向量的马氏距离: 这时a, b分别为属于同一类别的两个样本向量，cov_vec为该列别的协方差矩阵，返回同类别下的向量a, b间的马氏距离
   
    a=np.array([1.5 for i in range(128)])
    b=np.array([2 for i in range(128)])
    cov=np.cov(np.vstack((a,b)),rowvar=False)
    res=dis.mah_distance(a,b,cov)  #求解马氏距离
    print("马氏距离 = ", res) 
    
   ## 5. 求解曼哈顿距离
   > 1. 使用man_distance成员方法来计算和求解曼哈顿距离。
   > 2. 第一个参数为第一个向量a，类型为np.array。
   > 3. 第二个参数为第二个向量b，类型为np.array。
   
    a=np.array([1.5 for i in range(128)])
    b=np.array([2 for i in range(128)])
    res=dis.man_distance(a,b)  #求解曼哈顿距离
    print("曼哈顿距离 = ", res) 
    
   ## 6. 求解闵可夫斯基距离
   > 1. 使用min_distance成员方法来计算和求解闵可夫斯基距离。
   > 2. 第一个参数为第一个向量a，类型为np.array。
   > 3. 第二个参数为第二个向量b，类型为np.array。
   > 4. 第三个参数为闵可夫斯基距离范数/维数p，类型为int。
   
    a=np.array([1.5 for i in range(128)])
    b=np.array([2 for i in range(128)])
    res=dis.min_distance(a,b,3)  #求解闵可夫斯基距离
    print("闵可夫斯基距离 = ", res) 
   
   ## 7. 求解标准欧氏距离
   > 1. 使用standard_euc_distance成员方法来计算和求解标准欧氏距离。
   > 2. 第一个参数为第一个向量a，类型为np.array。
   > 3. 第二个参数为第二个向量b，类型为np.array。
   > 4. 第三个参数为向量a, b所属的类别的样本集合的方差向量s，类型为np.array。
   
    a=np.array([1.5 for i in range(128)])
    b=np.array([2 for i in range(128)])
    s=np.array([0.27 for i in range(128)])
    res=dis.standard_euc_distance(a,b,s)  #求解标准欧氏距离
    print("标准欧氏距离 = ", res)          
   
   ## 8. 求解余弦距离
   > 1. 使用cos_distance成员方法来计算和求解余弦距离。
   > 2. 第一个参数为第一个向量a，类型为np.array。
   > 3. 第二个参数为第二个向量b，类型为np.array。
   
    a=np.array([1.5 for i in range(128)])
    b=np.array([2 for i in range(128)])
    res=dis.cos_distance(a,b)       #求解余弦距离
    print("标准余弦距离 = ", res)       
   
 
