int(Xtrain.loc[0,"Date"].split("-")[1]) #提取出月份


Xtrain["Date"] = Xtrain["Date"].apply(lambda x:int(x.split("-")[1]))
# 要避免使用循环，用lambda代替


# 修改列名
Xtrain = Xtrain.rename(columns={"Date":"Month"})