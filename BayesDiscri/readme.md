 # BayesDiscri 朴素贝叶斯判别模块
 
 朴素贝叶斯判别算法是统计分析方法中最为经典和基础的判别算法。相关的算法介绍可以参见：
 https://zhuanlan.zhihu.com/p/26262151
 本说明文档仅提供本人实现的贝叶斯判别模块的具体使用方法。
 
 BayesDiscri朴素贝叶斯判别模块主要包括朴素贝叶斯判别算法的实现。

 # 1. 引用头文件"BayesDiscri.py"
 
    import BayesDiscri as bayes
    
 # 2. 创建BayesDiscri对象
 
    by=bayes.BayesDiscri()
    
 # 3. 使用训练集进行训练
 > 0. 函数原型
 
    def train(self, data, rowvar=False)
    
 > 1. 使用train成员方法使用训练集进行训练。
 > 2. 
