import Kmeans as km
import numpy as np

if __name__ == "__main__":
    
    data=np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25],[26,27,28,29,30]])
    label=np.array([0,0,0,1,1,1])
    
    kmeans=km.Kmeans(data,kind=2,rowsam=True)
    
    res=kmeans.cluster()
    print("聚类结果为 res = ", res)

    acc=kmeans.accuracy(label)
    print("聚类准确度为 acc = ",acc)