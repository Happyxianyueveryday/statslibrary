import VarAnaly as va
import numpy as np
from scipy.stats import f_oneway

if __name__ == "__main__":

    var=va.VarAnaly()
    
    # 1. 单因素方差分析
    data=np.array([[0.236, 0.238, 0.248, 0.245, 0.243],[0.257, 0.253, 0.255, 0.254, 0.261],[0.258, 0.264, 0.259, 0.267, 0.262]])
    res=var.single_anova(data,rowvar=True)
    
    print("单因素方差分析:")
    print("使用本库函数的方差分析结果，res = ", res)
    print("使用本库函数的方差分析结果，F值 = ", res[8])

    res=f_oneway(data[0],data[1],data[2])
    print("使用scipy.stats.f_oneway的方差分析检验结果，F值 = ", res[0])


    # 2. 双因素方差分析
    data=np.array([[[58.2,52.6],[56.2,41.2],[65.3,60.8]], [[49.1,42.8],[54.1,50.5],[51.6,48.4]], [[60.1,58.3],[70.9,73.2],[39.2,40.7]], [[75.8,71.5],[58.2,51.0],[48.7,41.4]]])
    res=var.double_anova(data)

    print("双因素方差分析:")
    print(res)
    print("使用本库函数的方差分析结果，res = ", res)
    print("使用本库函数的方差分析结果，因素A的F值 = ", res[14])
    print("使用本库函数的方差分析结果，因素A的F值 = ", res[15])
    print("使用本库函数的方差分析结果，交互作用A×B的F值 = ", res[16])

