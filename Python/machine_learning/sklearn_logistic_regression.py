import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    precision_recall_fscore_support, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split, KFold

df = pd.read_csv('titanic_noNA.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values
# print(x)
# print(y)

# ========================================
# build logistic regression model
# ========================================
model = LogisticRegression()
model.fit(X, y)
# print(model.coef_,model.intercept_)
# [[-1.19324152e+00 -2.50691271e+00 -4.27099569e-02 -3.59677077e-01
#   -5.24958165e-02  2.38996454e-03]] [5.14869004]

# print(model.predict([[3,True,22.0,1,0,7.25]]))
# 0, not survive
# print(model.predict([[1,True,37,0,1,320]]))
# 1, survive
# print(model.predict(X[:5]))
# print(y[:5])
# all 5 correct

# Score the model, accuracy
y_pred = model.predict(X)
print((y == y_pred).sum())  # check how much prediction results are correct
print((y == y_pred).sum() / y.shape[0])  # percent
print(model.score(X, y))

# accuracy, precision, recall and F1 score
print("accuracy:", accuracy_score(y, y_pred))
print("precision:", precision_score(y, y_pred))
print("recall:", recall_score(y, y_pred))
print("f1 score:", f1_score(y, y_pred))
print(confusion_matrix(y, y_pred))

# ====================================================
#  modify how we build and evaluate the model
# ====================================================
# -----------get training set and test set -----------
x_train, x_test, y_train, y_test = train_test_split(X, y)
print("whole dataset: ", X.shape, y.shape)
print("training set: ", x_train.shape, y_train.shape)
print("test set :", x_test.shape, y_test.shape)
# -----------change the size of training set-----------
x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.6)  # 60% training set, 75% is default
# -------------training set to build model-------------
model = LogisticRegression()
model.fit(x_train, y_train)
# ----------evaluate the model using the test set -------------
print(model.score(x_test, y_test))
y_pred = model.predict(x_test)
print("accuracy_tt: ", accuracy_score(y_test, y_pred))
print("precision_tt: ", precision_score(y_test, y_pred))
print("recall_tt: ", recall_score(y_test, y_pred))
print("f1 score_tt: ", f1_score(y_test, y_pred))
# those values are very similar to the values when we used the entire dataset, this is a sign our model isn't overfit
# ----------set seed, get the same split every time -------------
# x_train, x_test, y_train, y_test = train_test_split(X,y,random_state=5)

# ============================================================
# ROC Curve
# ============================================================
# ----------sensitivity & specificity ------------------------
sensitivity_score = recall_score
print("sensitivity: ", sensitivity_score(y_test, y_pred))


# specificity is the recall of the negative class
# print(precision_recall_fscore_support(y,y_pred))
def specificity_score(y_true, y_pred):
    p, r, f, s = precision_recall_fscore_support(y_true, y_pred)
    return r[0]


print("specificity: ", specificity_score(y_test, y_pred))
# ----------adjusting the threshold ----------------------------
# print("predict proba: ",model.predict_proba(x_test))
y_pred = model.predict_proba(x_test)[:, 1] > 0.75
# this results in fewer positive predictions and more negative predictions
print("precision_thre75: ", precision_score(y_test, y_pred))
print("recall_thre75: ", recall_score(y_test, y_pred))
# setting the threshold to 0.5 that back to original model
# ----------build ROC Curve and calculate AUC ----------------------
model1 = LogisticRegression()
model1.fit(x_train, y_train)
y_pred_proba1 = model1.predict_proba(x_test)
print("model 1 AUC score: ", roc_auc_score(y_test, y_pred_proba1[:, 1]))

model2 = LogisticRegression()
model2.fit(x_train[:, 0:2], y_train)
y_pred_proba2 = model2.predict_proba(x_test[:, 0:2])
print("model 2 AUC score: ", roc_auc_score(y_test, y_pred_proba2[:, 1]))

fpr1, tpr1, thresholds1 = roc_curve(y_test, y_pred_proba1[:, 1])
fpr2, tpr2, thresholds2 = roc_curve(y_test, y_pred_proba2[:, 1])
plt.plot(fpr1, tpr1, c="blue")
plt.plot(fpr2, tpr2, c="orange")
plt.plot([0, 1], [0, 1], linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.xlabel('1 - specificity')
plt.ylabel('sensitivity')
plt.show()

# ===========================================================
#  k-fold cross validation
# ===========================================================
'''take the dataset with just 6 datapoints and 2 features and 3-fold cross validation
k_x = df[['Age','Fare']].values[:6]
k_y = df['Survived'].values[:6]

kf = KFold(n_splits=3, shuffle=True)
for train,test in kf.split(k_x):
    print(train,test)

splits = list(kf.split(k_x))
first_split = splits[0]
train_indices, test_indices = first_split
print("training set indices:", train_indices)
print("test set indices:", test_indices)
x_train = k_x[train_indices]
x_test = k_x[test_indices]
y_train = k_y[train_indices]
y_test = k_y[test_indices]
print("x_train")
print(x_train)
print("y_train", y_train)
print("x_test")
print(x_test)
print("y_test",y_test)'''

# the entire dataset
kf = KFold(n_splits=5, shuffle=True)
# get once
splits = list(kf.split(X))
train_indices, test_indices = splits[0]
x_train = X[train_indices]
x_test = X[test_indices]
y_train = y[train_indices]
y_test = y[test_indices]

model = LogisticRegression()
model.fit(x_train, y_train)
print("one of the 5 folds scores:", model.score(x_test, y_test))

# loop over all the folds
scores = []
kf = KFold(n_splits=5, shuffle=True)
for train_index, test_index in kf.split(X):
    x_train = X[train_indices]
    x_test = X[test_indices]
    y_train = y[train_indices]
    y_test = y[test_indices]
    model = LogisticRegression()
    model.fit(x_train, y_train)
    scores.append(model.score(x_test, y_test))
print("All 5-fold model scores: ", scores)
print("the mean of 5-fold:", np.mean(scores))
# ==========================================================
# Model comparison
# ==========================================================
# build 3 different models base on different features choice
x1 = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
x2 = df[['Pclass', 'male', 'Age']].values
x3 = df[['Fare', 'Age']].values
y = df['Survived'].values


def score_model(x, y, kf):
    accuracy_scores = []
    precision_scores = []
    recall_scores = []
    f1_scores = []
    for train_index, test_index in kf.split(x):
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model = LogisticRegression()
        model.fit(x_train, y_train)
        y_pred = model.predict(x_test)
        accuracy_scores.append(accuracy_score(y_test, y_pred))
        precision_scores.append(precision_score(y_test, y_pred))
        recall_scores.append(recall_score(y_test, y_pred))
        f1_scores.append(f1_score(y_test, y_pred))
    print("accuracy:", np.mean(accuracy_scores))
    print("precision:", np.mean(precision_scores))
    print("recall:", np.mean(recall_scores))
    print("f1 score:", np.mean(f1_scores))


print("Logistic Regression with all features: {} \n".format(score_model(x1, y, kf)))
print("Logistic Regression with Pcalss, sex and age features: {} \n".format(score_model(x2, y, kf)))
print("Logistic Regression with Fare and Age features: {} \n".format(score_model(x3, y, kf)))

