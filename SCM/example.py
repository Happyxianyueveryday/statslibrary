import SCM
import numpy as np

if __name__ == "__main__":

    data=np.array([[1,3,5,7,9],[2,4,6,8,10],[1,4,5,8,9],
                   [1100,1300,1500,1700,1900],[1200,1400,1600,1800,2000],[1100,1400,1500,1800,1900],
                   [11000,13000,15000,17000,19000],[12000,14000,16000,18000,20000],[11000,14000,15000,18000,19000]
                   ]) #12个样本，明显属于3类
    
    # 1. 欧氏距离

    print("欧氏距离测试: ")

    scm=SCM.SCM(classdist='nearest', sampledist='euc')
    res=scm.fit(data,kind=3)
    print("样本间欧氏距离+类间最近距离: res = ", res)

    scm=SCM.SCM(classdist='farthest', sampledist='euc')
    res=scm.fit(data,kind=3)
    print("样本间欧氏距离+类间最远距离: res = ", res)

    scm=SCM.SCM(classdist='average', sampledist='euc')
    res=scm.fit(data,kind=3)
    print("样本间欧氏距离+类间平均距离: res = ", res)

    scm=SCM.SCM(classdist='centroid', sampledist='euc')
    res=scm.fit(data,kind=3)
    print("样本间欧氏距离+类间重心距离: res = ", res)

    scm=SCM.SCM(classdist='square', sampledist='euc')
    res=scm.fit(data,kind=3)
    print("样本间欧氏距离+离差平方距离: res = ", res)

    print("")
    print("")

    # 2. 马氏距离

    print("马氏距离测试: ")

    scm=SCM.SCM(classdist='nearest', sampledist='mah')
    res=scm.fit(data,kind=3)
    print("样本间马氏距离+类间最近距离: res = ", res)

    scm=SCM.SCM(classdist='farthest', sampledist='mah')
    res=scm.fit(data,kind=3)
    print("样本间马氏距离+类间最远距离: res = ", res)

    scm=SCM.SCM(classdist='average', sampledist='mah')
    res=scm.fit(data,kind=3)
    print("样本间马氏距离+类间平均距离: res = ", res)

    scm=SCM.SCM(classdist='centroid', sampledist='mah')
    res=scm.fit(data,kind=3)
    print("样本间马氏距离+类间重心距离: res = ", res)

    scm=SCM.SCM(classdist='square', sampledist='mah')
    res=scm.fit(data,kind=3)
    print("样本间马氏距离+离差平方距离: res = ", res)

    print("")
    print("")

    # 3. 曼哈顿距离

    print("曼哈顿距离测试: ")

    scm=SCM.SCM(classdist='nearest', sampledist='man')
    res=scm.fit(data,kind=3)
    print("样本间曼哈顿距离+类间最近距离: res = ", res)

    scm=SCM.SCM(classdist='farthest', sampledist='man')
    res=scm.fit(data,kind=3)
    print("样本间曼哈顿距离+类间最远距离: res = ", res)

    scm=SCM.SCM(classdist='average', sampledist='man')
    res=scm.fit(data,kind=3)
    print("样本间曼哈顿距离+类间平均距离: res = ", res)

    scm=SCM.SCM(classdist='centroid', sampledist='man')
    res=scm.fit(data,kind=3)
    print("样本间曼哈顿距离+类间重心距离: res = ", res)

    scm=SCM.SCM(classdist='square', sampledist='man')
    res=scm.fit(data,kind=3)
    print("样本间曼哈顿距离+离差平方距离: res = ", res)

    print("")
    print("")

    # 4. 闵可夫斯基距离

    print("闵科夫斯基距离测试，维数 = 2: ")

    scm=SCM.SCM(classdist='nearest', sampledist='min', p=2)
    res=scm.fit(data,kind=3)
    print("样本间闵可夫斯基距离+类间最近距离: res = ", res)

    scm=SCM.SCM(classdist='farthest', sampledist='min', p=2)
    res=scm.fit(data,kind=3)
    print("样本间闵可夫斯基距离+类间最远距离: res = ", res)

    scm=SCM.SCM(classdist='average', sampledist='min', p=2)
    res=scm.fit(data,kind=3)
    print("样本间闵可夫斯基距离+类间平均距离: res = ", res)

    scm=SCM.SCM(classdist='centroid', sampledist='min', p=2)
    res=scm.fit(data,kind=3)
    print("样本间闵可夫斯基距离+类间重心距离: res = ", res)

    scm=SCM.SCM(classdist='square', sampledist='min', p=2)
    res=scm.fit(data,kind=3)
    print("样本间闵可夫斯基距离+离差平方距离: res = ", res)

    print("")
    print("")

    # 5. 余弦距离

    print("余弦距离测试，维数 = 3: ")

    scm=SCM.SCM(classdist='nearest', sampledist='cos')
    res=scm.fit(data,kind=3)
    print("样本间余弦距离+类间最近距离: res = ", res)

    scm=SCM.SCM(classdist='farthest', sampledist='cos')
    res=scm.fit(data,kind=3)
    print("样本间余弦距离+类间最远距离: res = ", res)

    scm=SCM.SCM(classdist='average', sampledist='cos')
    res=scm.fit(data,kind=3)
    print("样本间余弦距离+类间平均距离: res = ", res)

    scm=SCM.SCM(classdist='centroid', sampledist='cos')
    res=scm.fit(data,kind=3)
    print("样本间余弦距离+类间重心距离: res = ", res)

    scm=SCM.SCM(classdist='square', sampledist='cos')
    res=scm.fit(data,kind=3)
    print("样本间余弦距离+离差平方距离: res = ", res)

    print("")
    print("")