import Distance as di
import numpy as np
from scipy.spatial.distance import pdist

if __name__ == "__main__":

    dis=di.Distance()
    a=np.array([1.5 for i in range(128)])
    b=np.array([2 for i in range(128)])
    s=np.array([0.27 for i in range(128)])

    print("使用本库的计算结果: ")
    print("欧氏距离 = ", dis.euc_distance(a,b))                         #欧氏距离
    print("曼哈顿距离 = ", dis.man_distance(a,b))                       #曼哈顿距离
    print("闵科夫斯基距离 = ", dis.min_distance(a,b,3))                 #闵可夫斯基距离 (p=2时相当于欧氏距离)
    print("标准欧氏距离 = ", dis.standard_euc_distance(a,b,s))          #标准欧氏距离
    print("余弦距离 = ", dis.cos_distance(a,b))                         #余弦距离

    print("使用python标准库的计算结果: ")
    print("欧氏距离 = ", pdist(np.vstack([a,b]),'euclidean'))           #欧氏距离
    print("曼哈顿距离 = ", pdist(np.vstack([a,b]),'cityblock'))         #曼哈顿距离
    print("闵科夫斯基距离 = ", pdist(np.vstack([a,b]),'minkowski', p=3))#闵可夫斯基距离 (p=2时相当于欧氏距离)
    print("标准欧氏距离 = ", pdist(np.vstack([a,b]),'seuclidean', V=s)) #标准欧氏距离
    print("余弦距离 = ", 1-pdist(np.vstack([a,b]),'cosine'))            #余弦距离(pdist中求得的是1-余弦距离)


