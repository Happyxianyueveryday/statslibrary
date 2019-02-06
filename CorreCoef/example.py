import CorreCoef as co
import numpy as np
import scipy.stats as sc

if __name__ == "__main__":

    # 1. pearson相关系数
    # pearson相关系数计算公式参见https://docs.scipy.org/doc/numpy/reference/generated/numpy.corrcoef.html?highlight=corrcoef#numpy.corrcoef
    
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 2, 2, 3]])
    coe=co.CorreCoef()

    res=coe.pearson_coef(data, rowvar=False)
    print("使用本库的计算结果 = ")
    print(res)

    res1=np.corrcoef(data, rowvar=False)
    print("使用numpy.corrcoef标准库的计算结果 = ")
    print(res1)

    # 1. spearson相关系数
    res=coe.spearman_coef(data, rowvar=False)
    print("使用本库的计算结果 = ")
    print(res)

    res1=sc.spearmanr(data, axis=0)
    print("使用numpy.corrcoef标准库的计算结果 = ")
    print(res1[0])



    