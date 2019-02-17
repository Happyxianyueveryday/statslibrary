import DistanceDiscri 
import numpy as np
import csv     #导入python的csv库文件
import os 
import sys
import math
import numpy as np
import pandas as pd

if __name__ == "__main__":
    # 1. 从csv文件中读取训练集中的所有数据
    data=pd.read_csv(sys.path[0]+'/train.csv')
    del data['safety']   #删除本实验中不使用的safety列
    #print(data)         #需要特别注意data中所有的元素均以字符串形式读入


    # 2. 训练集查找和替换，将除了综合评价（最后一列）以外的列中的等级全部替换为数值0,1,2,...
    buying_replace_dic={'low':0,'med':1,'high':2,'vhigh':3}
    maint_replace_dic={'low':0,'med':1,'high':2,'vhigh':3}
    doors_replace_dic={'2':0,'3':1,'4':2,'5more':3}
    persons_replace_dic={'2':0,'4':1,'more':2}
    lug_boot_replace_dic={'small':0,'med':1,'big':2}

    data['buying'].replace(buying_replace_dic,inplace=True)
    data['maint'].replace(maint_replace_dic,inplace=True)
    data['doors'].replace(doors_replace_dic,inplace=True)
    data['persons'].replace(persons_replace_dic,inplace=True)
    data['lug_boot'].replace(lug_boot_replace_dic,inplace=True)


    # 3. 将所有训练数据按照综合评价的结果（最后一列）划分为四个样本集unacc,acc,good,vgood，并将结果转化为np.array类型
    train_unacc=data[data['remark']=='unacc']
    del train_unacc['remark']
    train_unacc=train_unacc.values     # unacc类别的训练集

    train_acc=data[data['remark']=='acc']
    del train_acc['remark']
    train_acc=train_acc.values         # acc类别的训练集       

    train_good=data[data['remark']=='good']
    del train_good['remark']
    train_good=train_good.values       # good类别的训练集

    train_vgood=data[data['remark']=='vgood']
    del train_vgood['remark']
    train_vgood=train_vgood.values     # vgood类别的训练集

    # 4. 读取和预处理测试集数据
    test_data=pd.read_csv(sys.path[0]+'/test.csv')

    test_data['buying'].replace(buying_replace_dic,inplace=True)
    test_data['maint'].replace(maint_replace_dic,inplace=True)
    test_data['doors'].replace(doors_replace_dic,inplace=True)
    test_data['persons'].replace(persons_replace_dic,inplace=True)
    test_data['lug_boot'].replace(lug_boot_replace_dic,inplace=True)

    del test_data['safety']
    del test_data['remark']

    test_data=test_data.values

    # print(train_unacc)
    # print(train_acc)
    # print(train_good)
    # print(train_vgood)
    # print(test_data)
    # print(type(train_acc))

    # 5. 通过上述步骤已经得到了四个类别'unacc','acc','good','vgood'的训练集，这些训练集分别为train_unacc,train_acc,train_good,train_vood
    #    而待进行判别分析的测试集为test_data，其中每一行为一个样本，每一列代表一个变量
    
    dcr=DistanceDiscri.DistanceDiscri()

    dcr.train(train_unacc, train_acc, train_good, train_vgood, rowvar=False, label=['unacc','acc','good','vgood'])
    
    res=dcr.discriminate(test_data,rowvar=False)

    print(res)

    