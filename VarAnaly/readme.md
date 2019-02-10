# VarAnaly方差分析模块
   
   VarAnaly方差分析模块包含单因素方差分析和两因素方差分析方法。
   
   ## 1. 引用头文件"VarAnaly.py"
    import VarAnaly as va
   
   ## 2. 创建VarAnaly对象
   > 1. 创建VarAnaly对象不需要提供任何参数。
   
    var=va.VarAnaly()

   ## 3. 进行单因素方差分析
   > 1. 使用single_anova成员方法进行单因素方差分析
   > 2. 第一个参数data为样本集矩阵，类型为np.array
   > 3. 第二个参数rowvar指定每一行或者每一列作为因素的不同水平，类型为bool。rowvar=True指定每一行代表因素的一个水平，即每一列作为一个观察结果；rowvar=False指定每一列代表因素的一个水平，即每一行作为一个观察结果，默认rowvar=True。
   > 4. 返回值为元组形式的方差分析试验表(sa,se,st,fa,fe,ft,\_sa,\_se,f)。该元组中的各个元素参数对应的方差分析表如下。
   
   > |方差来源|平方和|自由度|均方|F比
   > | - | :-: | -: | 
   > |因素A|sa|fa|\_sa|f
   > |误差|se|fe|\_se| 
   > |总和|st|ft| | 
   
   
