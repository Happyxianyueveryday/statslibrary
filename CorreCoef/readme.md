 # CorreCoef相关系数与相关系数矩阵模块
   
   CorreCoef相关系数与相关系数矩阵模块包含统计分析学中常用的3种相关系数——Pearson，Spearman和Kendall相关系数的求解以及对应的相关系数矩阵的计算与求解。
   
   ## 1. 引用头文件"CorreCoef.py"
    import CorreCoef as co
   
   ## 2. 创建CorreCoef对象
   > 1. 创建CorreCoef对象不需要提供任何参数
   
    coe=co.CorreCoef()
   
   ## 3. 计算pearson相关系数矩阵
   > 0. 函数原型
   
      def pearson_coef(self, data, rowvar=True)
   
   > 1. 使用pearson_coef成员方法计算pearson相关系数矩阵。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。由相关系数的定义，变量和样本的数量均至少有两个，即至少为2×2矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。
   > 4. 返回值为pearson相关系数矩阵，类型为np.array。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 2, 2, 3]])
    res=coe.pearson_coef(data, rowvar=False)
    print("使用本库的pearson相关矩阵计算结果 = ")
    print(res)
    
    >>> 输出
    使用本库的pearson相关矩阵计算结果 =
    [[ 1.         -0.18898224  1.          1.          1.        ]
     [-0.18898224  1.         -0.18898224 -0.18898224 -0.18898224]
     [ 1.         -0.18898224  1.          1.          1.        ]
     [ 1.         -0.18898224  1.          1.          1.        ]
     [ 1.         -0.18898224  1.          1.          1.        ]]
    
   ## 4. 计算spearman相关系数矩阵
   > 0. 函数原型
   
      def spearman_coef(self, data, rowvar=True)
   
   > 1. 使用spearman_coef成员方法计算spearman相关系数矩阵。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。由相关系数的定义，变量和样本的数量均至少有两个，即至少为2×2矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。变量的数量必须大于或者等于2。
   > 4. 返回值为spearman相关系数矩阵，类型为np.array。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 2, 2, 3]])
    res=coe.spearman_coef(data, rowvar=False)
    print("使用本库的spearman相关矩阵计算结果 = ")
    print(res)
    
    >>> 输出
    使用本库的spearman相关矩阵计算结果 =
    [[1.  0.5 1.  1.  1. ]
     [0.5 1.  0.5 0.5 0.5]
     [1.  0.5 1.  1.  1. ]
     [1.  0.5 1.  1.  1. ]
     [1.  0.5 1.  1.  1. ]]
    
   ## 5. 计算kendall相关系数矩阵
   > 0. 函数原型
   
      def kendall_coef(self, data, rowvar=True)
   
   > 1. 使用kendall_coef成员方法计算kendall相关系数矩阵。
   > 2. 第一个参数data为由各个变量取值，或者由各个样本向量组成的矩阵。由相关系数的定义，变量和样本的数量均至少有两个，即至少为2×2矩阵。类型为np.array。
   > 3. 第二个参数rowvar指定每一行或者每一列作为样本向量，类型为bool：rowvar=True指定每一列作为一个样本向量，即每一行代表一个变量；rowvar=False指定每一行作为一个样本向量，即每一列代表一个变量。变量的数量必须大于或者等于2。
   > 4. 返回值为kendall相关系数矩阵，类型为np.array。
   
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 2, 2, 3]])
    res=coe.kendall_coef(data, rowvar=False)
    print("使用本库的kendall相关矩阵计算结果 = ")
    print(res)
    
    >>> 输出
    使用本库的kendall相关矩阵计算结果 =
    [[1.         0.33333333 1.         1.         1.        ]
     [0.33333333 1.         0.33333333 0.33333333 0.33333333]
     [1.         0.33333333 1.         1.         1.        ]
     [1.         0.33333333 1.         1.         1.        ]
     [1.         0.33333333 1.         1.         1.        ]]
    
   ## 附注：
   > 1. example.py中提供了一份使用CorreCoef相关系数与相关系数矩阵求解模块的示例代码。
    
