import GeneralStats as gs
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosistest
import pandas as pd


if __name__ == "__main__":

    gen=gs.GeneralStats()

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])

    print("data = ", data)
    print("data1 = ", data1)

    res=gen.average(data,rowvar=True)
    res1=gen.average(data1,rowvar=True)
    print("data平均值 = ",res)
    print("data1平均值 = ",res1)

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.median(data,rowvar=True)
    res1=gen.median(data1,rowvar=True)
    print("data中位值 = ",res)
    print("data1中位值 = ",res1)

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.mode(data,rowvar=True)
    res1=gen.mode(data1,rowvar=True)
    print("data众数值 = ",res)
    print("data1众数值 = ",res1)

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.quantile(data,0.5,rowvar=True,interpolation='lower')      #若元素个数为偶数，则模式为'midpoint'的0.5分位数值等价于中位数
    res1=gen.quantile(data1,0.5,rowvar=True,interpolation='lower')    #若元素个数为奇数，则模式为'lower'的0.5分位数值等价于中位数
    print("data 0.5分位数值 = ",res)
    print("data1 0.5分位数值 = ",res1)
    res=gen.quantile(data,0.25,rowvar=True,interpolation='lower')
    res1=gen.quantile(data1,0.25,rowvar=True,interpolation='lower')
    print("data 0.25分位数值s = ",res)
    print("data1 0.25分位数值 = ",res1)
    res=gen.quantile(data,0.75,rowvar=True,interpolation='lower')
    res1=gen.quantile(data1,0.75,rowvar=True,interpolation='lower')
    print("data 0.75分位数值 = ",res)
    print("data1 0.75分位数值 = ",res1)
    res=gen.quantile(data,1.0,rowvar=True,interpolation='lower')
    res1=gen.quantile(data1,1.0,rowvar=True,interpolation='lower')
    print("data 1.0分位数值 = ",res)
    print("data1 1.0分位数值 = ",res1)

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.range(data,rowvar=True)
    res1=gen.range(data1,rowvar=True)
    print("data极差 = ",res)
    print("data1极差 = ",res1)

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.variance(data,rowvar=True)
    res1=gen.variance(data1,rowvar=True)
    print("data方差 = ",res)
    print("data1方差 = ",res1)

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.standard_dev(data,rowvar=True)
    res1=gen.standard_dev(data1,rowvar=True)
    print("data标准差 = ",res)
    print("data1标准差 = ",res1)

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([1,2,3,4,5])
    res=gen.skewness(data,rowvar=True)
    res1=gen.skewness(data1,rowvar=True)
    print("data偏度 = ",res)
    print("data1偏度 = ",res1)
    res=np.array([skew(data[0]),skew(data[1]),skew(data[2]),skew(data[3])])
    print("使用scipy skew方法验证的data偏度 = ",res)
    res1=np.array(skew(data1))
    print("使用scipy skew方法验证的data1偏度 = ",res1)

    data=np.array([[1, 1, 2, 2, 3],[2, 2, 3, 3, 5],[1, 4, 3, 3, 3],[2, 4, 5, 5, 3]])
    data1=np.array([53, 61, 49, 66, 78, 47])
    res=gen.kurtosis(data,rowvar=True)
    res1=gen.kurtosis(data1,rowvar=True)
    print("data峰度 = ",res)
    print("data1峰度 = ",res1)
    data_0=pd.Series(data[0])
    data_1=pd.Series(data[1])
    data_2=pd.Series(data[2])
    data_3=pd.Series(data[3])
    print("使用pandas kurt方法验证的data峰度 = ",[data_0.kurt(),data_1.kurt(),data_2.kurt(),data_3.kurt()])
    data1=pd.Series(data1)
    print("使用pandas kurt方法验证的data1峰度 = ",data1.kurt())



    



