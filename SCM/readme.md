 # SCM系统聚类法模块  
 
 SCM系统聚类法模块包含系统聚类算法的实现。
 

 ## 1. 引用头文件"SCM.py"      
    import SCM
    
 ## 2. 创建一个SCM对象
 > 1. 创建一个SCM对象最多需要三个参数。
 > 2. 第一个参数classdist指定系统聚类法中所使用的类间距离的种类,类型为str。取值范围为classdist={'nearest','farthest','average','centroid','square'}，默认值为classdist='nearest'，参数的取值的具体含义如下所示：
 >>  + 'nearest' : 类间最近距离，类间最近距离为两个类别之间样本距离的最小值
 >>  + 'farthest': 类间最远距离，类间最远距离为两个类别之间样本距离的最小值
 >>  + 'average' : 类间平均距离，类间平均距离为两个类别之间样本距离的平均值
 >>  + 'centroid': 类间重心距离，类间重心距离为两个类别的重心/均值向量之间的距离
 >>  + 'square'  : 类间离差平方和距离，类间离差平方和距离=类别a的直径-类别b的直径-类别a，b的合并大类直径
 > 3. 第二个参数sampledist指定系统聚类法中所使用的样本间距离的种类，类型为str，取值范围为sampledist={'euc','mah','man','min','cos'}，默认值为sampledist='euc'。若参数classdist=='square'，则此参数不使用
 >>  + 'euc': 样本间欧氏距离
 >>  + 'mah': 样本间马氏距离
 >>  + 'man': 样本间曼哈顿距离
 >>  + 'min': 样本间闵可夫斯基距离
 >>  + 'cos': 样本间余弦距离
 > 4. 第三个参数p为闵可夫斯基距离的维数p，类型为int。默认值为p=1。若参数classdist=='square'或者参数sampledist!='min'，则此参数不被使用，可以保持缺省。
  
    scm=SCM.SCM(classdist='nearest', sampledist='euc')
