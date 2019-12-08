#将标签编码
from sklearn.preprocessing import LabelEncoder #标签专用，第三章讲过
encorder = LabelEncoder().fit(Ytrain) #允许一维数据的输入的


#使用训练集进行训练，然后在训练集和测试集上分别进行transform
Ytrain = pd.DataFrame(encorder.transform(Ytrain))
Ytest = pd.DataFrame(encorder.transform(Ytest))

#如果我们的测试集中，出现了训练集中没有出现过的标签类别，要重新训练或划分

