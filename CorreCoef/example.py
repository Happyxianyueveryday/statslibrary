import CorreCoef as co
import numpy as np
import scipy.stats as sc

if __name__ == "__main__":

    # 1. pearson相关系数
    # pearson相关系数计算公式参见https://docs.scipy.org/doc/numpy/reference/generated/numpy.corrcoef.html?highlight=corrcoef#numpy.corrcoef
    
    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 2, 2, 3]])
    coe=co.CorreCoef()

    res=coe.pearson_coef(data, rowvar=False)
    print("使用本库的pearson相关矩阵计算结果 = ")
    print(res)

    res1=np.corrcoef(data, rowvar=False)
    print("使用numpy.corrcoef标准库的计算结果 = ")
    print(res1)

    # 2. spearman相关系数
    res=coe.spearman_coef(data, rowvar=False)
    print("使用本库的spearman相关矩阵计算结果 = ")
    print(res)

    res1=sc.spearmanr(data, axis=0)
    print("使用scipy.spearmanr标准库的计算结果 = ")
    print(res1[0])

    # 3. kendall相关系数
    res=coe.kendall_coef(data, rowvar=False)
    print("使用本库的kendall相关矩阵计算结果 = ")
    print(res)
    
    data1=data.T
    size=np.shape(data)[1]
    res1=np.zeros((size,size))
    for i in range(size):
        for k in range(size):
            res1[i][k]=sc.kendalltau(data1[i],data1[k])[0]
    print("使用scipy.kendalltau标准库的计算结果 = ")
    print(res1)



    