from sklearn.preprocessing import StandardScaler

data.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.9,0.99]).T

X = StandardScaler().fit_transform(X)#将数据转化为0,1正态分布
data = pd.DataFrame(X)

data.describe([0.01,0.05,0.1,0.25,0.5,0.75,0.9,0.99]).T#均值很接近，方差为1了