from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
'''
自带数据集：load_iris load_digits load_diabetes load_breast_cancer load_boston load_linnerud
自建数据集：
1)make_blobs：多类单标签数据集，为每个类分配一个或多个正态分布的点集

2)make_classification：多类单标签数据集，为每个类分配一个或多个正态分布的点集，
提供了为数据添加噪声的方式，包括维度相关性，无效特征以及冗余特征等

3)make_gaussian-quantiles：将一个单高斯分布的点集划分为两个数量均等的点集，作为两类

4)make_hastie-10-2：产生一个相似的二元分类数据集，有10个维度

5)make_circle和make_moom：产生二维二元分类数据集来测试某些算法的性能，
可以为数据集添加噪声，可以为二元分类器产生一些球形判决界面的数据。

'''

data = load_breast_cancer()
X = data.data
y = data.target
 
X.shape
np.unique(y)
 
plt.scatter(X[:,0],X[:,1],c=y)
plt.show()
 
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X,y,test_size=0.3,random_state=420)
