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

