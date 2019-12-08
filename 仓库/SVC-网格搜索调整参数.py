from sklearn.model_selection import StratifiedShuffleSplit#用于支持带交叉验证的网格搜索
from sklearn.model_selection import GridSearchCV#带交叉验证的网格搜索
 
time0 = time()
 
gamma_range = np.logspace(-10,1,20)
coef0_range = np.linspace(0,5,10)
 
param_grid = dict(gamma = gamma_range
                  ,coef0 = coef0_range)
cv = StratifiedShuffleSplit(n_splits=5, test_size=0.3, random_state=420)#将数据分为5份，5份数据中测试集占30%
grid = GridSearchCV(SVC(kernel = "poly",degree=1,cache_size=5000
                        ,param_grid=param_grid
                        ,cv=cv)
grid.fit(X, y)
 
print("The best parameters are %s with a score of %0.5f" % (grid.best_params_, grid.best_score_))
print(time()-time0)
