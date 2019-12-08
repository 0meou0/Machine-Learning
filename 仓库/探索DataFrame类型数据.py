import pandas as pd
from sklearn.model_selection import train_test_split


data = pd.DataFrame(X)
# or
data = pd.read_csv(r"xx.csv",index_col=0)
Ytest.to_csv("你想要保存这个文件的地址.文件名.csv")

data.head()
data.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.9,0.99]).T#描述性统计
#从mean列和std列可以看出是否量纲不统一
#从1%的数据和最小值相对比，90%的数据和最大值相对比，查看是否是正态分布或偏态分布，
#如果差的太多就是偏态分布，谁大方向就偏向谁
#如果特征存在偏态问题，这个时候就需要对数据进行标准化

#将特征矩阵和标签Y分开
X = weather.iloc[:,:-1]
Y = weather.iloc[:,-1]

X.shape

#探索数据类型
X.info()

#探索缺失值
X.isnull().mean() 
#缺失值所占总值的比例 isnull().sum(全部的True)/X.shape[0]

Y.isnull().sum() #加和的时候，True是1，False是0

#探索标签的分类
np.unique(Y) 

#分训练集和测试集
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X,Y,test_size=0.3,random_state=420) #随机抽样

#恢复索引
for i in [Xtrain, Xtest, Ytrain, Ytest]:
    i.index = range(i.shape[0])


#是否有样本不平衡问题？
Ytrain.value_counts()
Ytrain.value_counts()[0]/Ytrain.value_counts()[1] #样本标签比例

# 将样本按某一列排序
Xtrain.sort_values(by="列名")

# 将样本的某一列统计输出
Xtrain.iloc[:,0].value_counts()

# 定位到符合某一条件的样本
Xtrain.loc[Xtrain.iloc[:,0] == "2015-08-24",:]

# 查看分类型变量的总类别数
Xtrain.iloc[:,0].value_counts().count()

# 修改列名
Xtrain = Xtrain.rename(columns={"Date":"Month"})