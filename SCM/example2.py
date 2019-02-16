import SCM
import numpy as np

def replace(lis,dic):
    for i in range(len(lis)):
        for k in range(len(lis[i])):
            lis[i][k]=dic[lis[i][k]]
    return lis

if __name__ == "__main__":
    
    data=np.array([[1772.14,568.25,298.66,352.20,307.21,490.83,364.28,202.50],    # 辽宁            # 原始样本矩阵
                   [2752.25,569.95,662.31,541.06,623.05,917.23,599.98,354.39],    # 浙江
                   [1386.76,460.99,312.97,280.78,246.24,407.26,547.19,188.52],    # 河南
                   [1552.77,517.16,402.03,272.44,265.29,563.10,302.27,251.41],    # 甘肃
                   [1711.03,458.57,334.91,307.24,297.72,495.34,274.48,306.45]])   # 青海            # 总计5个样本
    
    dic={0:'辽宁',1:'浙江',2:'河南',3:'甘肃',4:'青海'}
                
    scm=SCM.SCM(classdist='nearest', sampledist='euc')

    res=scm.fit(data,kind=5)                     # 获得分类后的样本下标
    res=replace(res,dic)                         # 替换样本下标为样本标签名
    print("分为5类结果 res = :",res)
    
    res=scm.fit(data,kind=4)                     # 获得分类后的样本下标
    res=replace(res,dic)                         # 替换样本下标为样本标签名
    print("分为4类结果 res = :",res)

    res=scm.fit(data,kind=3)                     # 获得分类后的样本下标
    res=replace(res,dic)                         # 替换样本下标为样本标签名
    print("分为3类结果 res = :",res)

    res=scm.fit(data,kind=2)                     # 获得分类后的样本下标
    res=replace(res,dic)                         # 替换样本下标为样本标签名
    print("分为2类结果 res = :",res)

    res=scm.fit(data,kind=1)                     # 获得分类后的样本下标
    res=replace(res,dic)                         # 替换样本下标为样本标签名
    print("分为1类结果 res = :",res)
    
