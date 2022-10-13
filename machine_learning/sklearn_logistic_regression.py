import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, precision_recall_fscore_support
from sklearn.model_selection import train_test_split

df = pd.read_csv('titanic_noNA.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y = df['Survived'].values
#print(x)
#print(y)

# ========================================
# build logistic regression model
# ========================================
model = LogisticRegression()
model.fit(X,y)
#print(model.coef_,model.intercept_)
# [[-1.19324152e+00 -2.50691271e+00 -4.27099569e-02 -3.59677077e-01
#   -5.24958165e-02  2.38996454e-03]] [5.14869004]

#print(model.predict([[3,True,22.0,1,0,7.25]]))
# 0, not survive
#print(model.predict([[1,True,37,0,1,320]]))
# 1, survive
#print(model.predict(X[:5]))
#print(y[:5])
# all 5 correct

# Score the model, accuracy
y_pred = model.predict(X)
print((y == y_pred).sum())  # check how much prediction results are correct
print((y == y_pred).sum() / y.shape[0])  #percent
print(model.score(X,y))

# accuracy, precision, recall and F1 score
print("accuracy:", accuracy_score(y,y_pred))
print("precision:",precision_score(y,y_pred))
print("recall:",recall_score(y,y_pred))
print("f1 score:",f1_score(y,y_pred))
print(confusion_matrix(y,y_pred))

# ====================================================
#  modify how we build and evaluate the model
# ====================================================
# -----------get training set and test set -----------
x_train, x_test, y_train, y_test = train_test_split(X,y) 
print("whole dataset: ",X.shape,y.shape)
print("training set: ", x_train.shape,y_train.shape)
print("test set :", x_test.shape,y_test.shape)
# -----------change the size of training set-----------
x_train, x_test, y_train, y_test = train_test_split(X,y,train_size=0.6) # 60% training set, 75% is default
# -------------training set to build model-------------
model = LogisticRegression()
model.fit(x_train,y_train)
# ----------evaluate the model using the test set -------------
print(model.score(x_test,y_test))
y_pred = model.predict(x_test)
print("accuracy_tt: ",accuracy_score(y_test,y_pred))
print("precision_tt: ",precision_score(y_test,y_pred))
print("recall_tt: ",recall_score(y_test,y_pred))
print("f1 score_tt: ",f1_score(y_test,y_pred))
# those values are very similar to the values when we used the entire dataset, this is a sign our model isn't overfit
# ----------set seed, get the same split every time -------------
#x_train, x_test, y_train, y_test = train_test_split(X,y,random_state=5)

# ============================================================
# ROC Curve
# ============================================================
# ----------sensitivity & specificity ------------------------
sensitivity_score = recall_score
print("sensitivity: ",sensitivity_score(y_test,y_pred))
# specificity is the recall of the negative class
#print(precision_recall_fscore_support(y,y_pred))
def specificity_score(y_true,y_pred):
    p,r,f,s = precision_recall_fscore_support(y_true, y_pred)
    return r[0]
print("specificity: ",specificity_score(y_test, y_pred))
# ----------adjusting the threshold ----------------------------
#print("predict proba: ",model.predict_proba(x_test))
y_pred = model.predict_proba(x_test)[:,1] > 0.75
# this results in fewer positive predictions and more negative predictions
print("precision_thre75: ",precision_score(y_test, y_pred))
print("recall_thre75: ",recall_score(y_test, y_pred))
# setting the threshold to 0.5 that back to original model
