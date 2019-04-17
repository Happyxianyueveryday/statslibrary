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
  
  我们对上述的城市经济数据进行因子分析，计算出因子载荷矩阵，从而判断每个特征的影响的大小。
  
  ```
  import numpy as np
import FacAnaly as fa
import pandas as pd
import math
import sys

# 1. 按列读取原始数据
np.set_printoptions(suppress = True)
data = pd.read_csv(sys.path[0]+'\\data.csv')
del data['城市']                                                       # 删除无效的城市名一列
col_data = np.array([data['x'+str(i)].values for i in range(1,13)])    # 读取各个特征所在的列

data=col_data

fa=fa.FacAnaly()

print("m = 12的载荷矩阵")
print(fa.analy(data,rowvar=False,n_components=12))

print("m = 3的载荷矩阵")
print(fa.analy(data,rowvar=False,n_components=3))

print("m = 4的载荷矩阵")
print(fa.analy(data,rowvar=False,n_components=4))

print("m = 5的载荷矩阵")
print(fa.analy(data,rowvar=False,n_components=5))
  ```
  
分析结果如下所示。

+ m = 12时的载荷矩阵
![avatar](https://github.com/Happyxianyueveryday/statslibrary/blob/master/FacAnaly/pics/QQ%E6%88%AA%E5%9B%BE20190417005816.png)

+ m = 3，4，5时的载荷矩阵
![avatar](https://github.com/Happyxianyueveryday/statslibrary/blob/master/FacAnaly/pics/QQ%E6%88%AA%E5%9B%BE20190417005321.png)
![avatar](https://github.com/Happyxianyueveryday/statslibrary/blob/master/FacAnaly/pics/QQ%E6%88%AA%E5%9B%BE20190417005816.png)
  
  
   

