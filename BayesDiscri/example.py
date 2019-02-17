import BayesDiscri as bayes
import numpy as np

if __name__ == "__main__":
    
    train_data=np.array([['帅','不好','高','不上进','不嫁'],
                   ['不帅','好','高','上进','不嫁'],
                   ['帅','好','矮','上进','嫁'],
                   ['不帅','好','高','上进','嫁'],
                   ['帅','不好','矮','上进','不嫁'],
                   ['帅','不好','矮','上进','不嫁'],
                   ['帅','好','高','不上进','嫁'],
                   ['不帅','好','中','上进','嫁'],
                   ['帅','好','中','上进','嫁'],
                   ['不帅','不好','高','上进','嫁'],
                   ['帅','好','矮','不上进','不嫁'],
                   ['帅','好','矮','不上进','不嫁']])
    
    by=bayes.BayesDiscri()
    by.train(train_data,rowvar=False)

    test_data=np.array([['不帅','不好','矮','不上进'],
                        ['不帅','好','高','不上进']])

    res=by.discriminate(test_data,rowvar=False)
    print('分类结果: res = ', res[0])
    print('测试集样本属于各个类别的概率: res = ', res[1])
    

