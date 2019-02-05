# Distance距离度量模块

   ## 1. 引用头文件"Distance.py"
    import Distance as di

   ## 2. 创建一个Distance对象
   > 1. 初始化一个Pattern对象无需提供任何参数。
   
    dis=di.Distance()
    
   ## 3. 求解欧氏距离
   > 1. 使用euc_distance成员方法来改变加密模式。
   > 2. 第一个参数为第一个向量a。
   > 3. 第二个参数为第二个向量b。
    
    a=np.array([1.5 for i in range(128)])
    b=np.array([2 for i in range(128)])
    res=dis.euc_distance(a,b)  #求解欧氏距离
    print("欧氏距离 = ", res)                         
    
  
