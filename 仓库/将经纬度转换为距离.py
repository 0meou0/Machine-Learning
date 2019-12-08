#使用radians将角度转换成弧度
from math import radians, sin, cos, acos

#有度数符号的去掉经纬度中度数的符号，在同一个半球的舍弃我们的经纬度的方向
samplecity["Latitudenum"] = samplecity["Latitude"].apply(lambda x:float(x[:-1]))

# 依次处理出发地、目的地的经纬度
citylld.loc[:,"slat"] = citylld.iloc[:,1].apply(lambda x : radians(x))



dist = 6371.01 * np.arccos(np.sin(slat)*np.sin(elat) + 
                          np.cos(slat)*np.cos(elat)*np.cos(slon.values - elon))
