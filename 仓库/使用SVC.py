from sklearn.datasets import make_blobs
from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X,y,test_size=0.3,random_state=420)
 
Kernel = ["linear","poly","rbf","sigmoid"]
 
for kernel in Kernel:
    time0 = time()
    clf= SVC(kernel = kernel
             , gamma="auto"
            # , degree = 1 只对poly有用
             , cache_size=1000#使用计算的内存，单位是MB，默认是200MB
            ).fit(Xtrain,Ytrain)
    print("The accuracy under kernel %s is %f" % (kernel,clf.score(Xtest,Ytest)))
    print(time()-time0)

# 调用画图函数
plt.scatter(X[:,0],X[:,1],c=y,s=50,cmap="rainbow")
plot_svc_decision_function(clf)

clf.predict(X)
#根据决策边界，对X中的样本进行分类，返回的结构为n_samples
 
clf.score(X,y)
#返回给定测试数据和标签的平均准确度
 
clf.support_vectors_
#返回支持向量坐标
 
clf.n_support_#array([2, 1])
#返回每个类中支持向量的个数