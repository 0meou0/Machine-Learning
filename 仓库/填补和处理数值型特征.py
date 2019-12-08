from sklearn.impute import SimpleImputer #0.20, conda, pip


# 1.填补缺失值
# 找出数值型特征，数值型特征没有单独的类型说明，要把分类型特征挑出来
col = Xtrain.columns.tolist()

for i in cate:
    col.remove(i)

#实例化模型，填补策略为"mean"表示均值
impmean = SimpleImputer(missing_values=np.nan,strategy = "mean")
#用训练集来fit模型
impmean = impmean.fit(Xtrain.loc[:,col])
#分别在训练集和测试集上进行均值填补
Xtrain.loc[:,col] = impmean.transform(Xtrain.loc[:,col])
Xtest.loc[:,col] = impmean.transform(Xtest.loc[:,col])


# 检查一下
Xtrain.isnull().mean()
Xtest.isnull().mean()

# 2.数据无量纲化
from sklearn.preprocessing import StandardScaler #数据转换为均值为0，方差为1的数据
#标准化不改变数据的分布，不会把数据变成正态分布的


ss = StandardScaler()
ss = ss.fit(Xtrain.loc[:,col])
Xtrain.loc[:,col] = ss.transform(Xtrain.loc[:,col])
Xtest.loc[:,col] = ss.transform(Xtest.loc[:,col])


# 查看结果
Xtrain.head()
Xtest.head()