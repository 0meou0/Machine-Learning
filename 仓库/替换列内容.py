import re

#城市的气候中所含的逗号和空格都去掉
Xtrain["Location"] = Xtrain["Location"].apply(lambda x:re.sub(",","",x.strip()))