# statslibrary
中山大学统计分析与机器学习课程实验作业/Experimental homework of statistical-analysis-method-course in SYSU.

statslibrary是个人实现的，基于numpy库的小型统计分析方法库，仅基于numpy实现，不会使用较为现成的算法，包含主成分分析，聚类分析等统计分析算法的实现。

需要使用某个算法模块，只需要包含对应模块文件夹下的对应头文件即可使用，各个模块的使用说明文档也请参见对应的文件夹下的readme文档。statslibrary中所实现的各个分析算法请参见如下的目录。

其中部分标记为\*的模块暂时下架修正部分错误和瑕疵，在4月9日前将重新上架。

## 目录
### 数据描述性分析部分
#### 1. Distance：距离计算模块，包含欧氏距离，马氏距离等距离计算方法
#### 2. CorreCoef：相关系数与相关系数矩阵计算模块，包含pearman相关系数，spearman相关系数等相关系数计算方法
#### 3. GeneralStats：一般分析统计量计算模块，包含平均数，中位数，众数，分位数，方差，标准差，极差，偏度，峰度等统计量计算方法

### 方差分析与回归分析部分
#### 1. VarAnaly：方差分析模块，包含单因素方差分析和双因素方差分析
#### 2. \*LinearRegre：回归分析模块，包含一元和多元线性回归分析

### 主成分分析部分
#### 1. PCA：主成分分析模块

### 聚类分析部分
#### 1. Kmeans：K-Means, Kmeans聚类法模块
#### 2. SCM：Ward-Hierarchical-Clustering, 系统聚类法（又称层次聚类法）模块 
#### 3. \*Spectral：Spectral-Clustering, 谱聚类算法模块
#### 4. \*DBSCAN：

### 判别分析部分
#### 1. DistanceDiscri：距离判别分析模块
#### 2. BayesDiscri：朴素贝叶斯判别分析模块
#### 3. \*FisherDiscri：费歇判别分析模块

### 因子分析部分
#### 1. \*FacAnaly：因子分析模块
