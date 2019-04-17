# FacAnaly因子分析模块
   
   FacAnaly因子分析模块包含统计分析算法中的因子分析算法。
   
   ## 1. 引用头文件"FacAnaly.py"
    import FacAnaly as fa
   
   ## 2. 创建FacAnaly对象
   > 1. 创建FacAnaly对象不需要提供任何参数。
   
    fa=fa.FacAnaly()

   ## 3. 进行因子分析
   > 0. 函数原型
   
      def analy(self, data, rowvar=True, n_components=2):
      
   > 1. 使用analy成员方法进行因子分析。
   > 2. 该成员方法的第一个参数data为样本集矩阵。
   > 3. 该成员方法的第二个参数rowvar指定样本集矩阵data的每行或者每列作为特征，rowvar=True指定样本集矩阵data的每一行作为一个特征，每一列作为一个样本；rowvar=False指定样本集矩阵的每一列作为一个特征，每一行作为一个样本。
   > 4. 该成员方法的第三个参数n_components=2指定保留的主要的因子个数。
   > 5. 返回值为因子分析的结果，即因子载荷矩阵，因子载荷矩阵的每一列代表一个特征，每一行代表一个样本，例如矩阵中坐标为(x,y)的元素表示在样本x中特征y的因子权重。
   
      data=np.array([[1,2,3],[4,5,6]])
      fa=fa.FacAnaly()
      print(fa.analy(data,rowvar=False,n_components=2))
   
   
  ## 示例代码：城市经济数据的因子分析
  考虑如下的城市经济数据。
  ![avatar](https://github.com/Happyxianyueveryday/statslibrary/blob/master/FacAnaly/pics/QQ%E6%88%AA%E5%9B%BE20190417095029.png)
  ![avatar](https://github.com/Happyxianyueveryday/statslibrary/blob/master/FacAnaly/pics/QQ%E6%88%AA%E5%9B%BE20190417095125.png)
  
  
   

