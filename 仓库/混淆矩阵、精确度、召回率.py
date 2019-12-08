from sklearn.metrics import confusion_matrix as CM, precision_score as P, recall_score as R

clf_prob = svm.SVC(kernel="linear",C=1.0,probability=True).fit(X,y)
prob = clf_prob.predict_proba(X)

cm = CM(prob.loc[:,"y_true"],prob.loc[:,"pred"],labels=[1,0])
# 一般设少数类为1，多数类为0，精确度和召回率是关注少数类的指标

P(prob.loc[:,"y_true"],prob.loc[:,"pred"],labels=[1,0])

R(prob.loc[:,"y_true"],prob.loc[:,"pred"],labels=[1,0])


#00/all true 0 1-特异度
#FPR #被我们预测错误的0占所有真正为0的样本的比例
cm[1,0]/cm[1,:].sum()
#Recall
cm[0,0]/cm[0,:].sum()


