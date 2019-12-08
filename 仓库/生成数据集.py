from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np


# 生成二分类数据 50个点，2簇，离散程度0.6
X,y = make_blobs(n_samples=50, centers=2, random_state=0,cluster_std=0.6)

# 绘图
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="rainbow")#rainbow彩虹色 颜色按y分类
# 指定横纵坐标
plt.xticks([]) #可为空，可填坐标
plt.yticks([])
plt.show()

---------------------------------------------------------
# 生成环形数据
from sklearn.datasets import make_circles
X,y = make_circles(100, factor=0.1, noise=.1)
 
X.shape
 
y.shape
 
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="rainbow")
plt.show()

----------------------------------------------------------
# 生成4种数据集
n_samples = 100
 
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_blobs(n_samples=n_samples, centers=2, random_state=5),#分簇的数据集
    make_classification(n_samples=n_samples,n_features = 2,n_informative=2,n_redundant=0, random_state=5)
                #n_features：特征数，n_informative：带信息的特征数，n_redundant：不带信息的特征数
    ]
 
Kernel = ["linear","poly","rbf","sigmoid"]
 
# 画图展示
for X,Y in datasets:
    plt.figure(figsize=(5,4))
    plt.scatter(X[:,0],X[:,1],c=Y,s=50,cmap="rainbow")

