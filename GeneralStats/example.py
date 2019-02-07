import GeneralStats as gs
import numpy as np

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
    print("data 0.25分位数值 = ",res)
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



