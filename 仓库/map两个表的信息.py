

#在这里设定locafinal的索引为地点，是为了之后进行map的匹配
locafinal = locafinal.set_index(keys="Location")

#气象站的名字替换成了对应的城市对应的气候
Xtrain["Location"] = Xtrain["Location"].map(locafinal.iloc[:,0])