import VarAnaly as va
import numpy as np
from scipy.stats import f_oneway

if __name__ == "__main__":

    var=va.VarAnaly()
    
    # 1. 单因素方差分析
    data=np.array([[0.236, 0.238, 0.248, 0.245, 0.243],[0.257, 0.253, 0.255, 0.254, 0.261],[0.258, 0.264, 0.259, 0.267, 0.262]])
    res=var.single_anova(data,rowvar=True)

    print("使用本库函数的方差分析结果，元组最后一个元素为F值，res = ", res)

    res=f_oneway(data[0],data[1],data[2])
    print("使用scipy.stats.f_oneway的方差分析检验结果，F值 = ", res[0])
