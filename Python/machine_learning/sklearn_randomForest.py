import time
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression


cancer_data = load_breast_cancer()
print(cancer_data['data'].shape) # or print(cancer_data.data.shape)

df = pd.DataFrame(cancer_data['data'], columns=cancer_data['feature_names'])
df['target'] = cancer_data['target']  # 0 means malignant and 1 means benign
#print(df.head())
#print(cancer_data.feature_names)
#print(df[cancer_data.feature_names])
X = df[cancer_data.feature_names].values
y = df['target'].values

x_train, x_test, y_train, y_test = train_test_split(X,y,random_state=101)
rf = RandomForestClassifier()
rf.fit(x_train, y_train)

first_row = x_test[0]
print("prediction:", rf.predict([first_row]))
print("true value:", y_test[0])
print("Random forest accuracy:", rf.score(x_test,y_test))

dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)
print("Decision tree accuracy:", dt.score(x_test,y_test))

lr = LogisticRegression(solver='liblinear')
lr.fit(x_train,y_train)
print("Logistic Regression accuracy:",lr.score(x_test,y_test))

# -------------------------------------------------------------
# Tuning a random forest
# -------------------------------------------------------------
# limit the number of features to consider at each split, default is the square root of p
rf_mf = RandomForestClassifier(max_features=5)
# change the number of trees, the default is 10
rf_ne = RandomForestClassifier(n_estimators=15)

# -------------------------------------------------------------
# Grid Search, find the optimal choice of parameters
# -------------------------------------------------------------

para_grid = {
    'n_estimators':[10,25,50,75,100],
}
rf_gs = RandomForestClassifier(random_state=123)
gs = GridSearchCV(rf_gs, param_grid=para_grid, scoring='f1',cv=5)
gs.fit(X, y)
print("best parameters:", gs.best_params_)

# -------------------------------------------------------------------------
# Elbow Graph, optimizes performance without adding unnecessary complexity
# -------------------------------------------------------------------------

time_st = time.time()
n_estimators = list(range(1,101))
para_grid2 = {
    'n_estimators':n_estimators,
}
gs2 = GridSearchCV(rf_gs, param_grid=para_grid2,cv=5)
gs2.fit(X,y)
scores = gs2.cv_results_['mean_test_score']
plt.plot(n_estimators,scores)
plt.xlabel("n_estimators")
plt.ylabel("accuracy")
plt.xlim(0,100)
plt.ylim(0.9,1)
plt.savefig('./elbow_estimators.jpg')
plt.show()
time_ed = time.time()
print("time cost for 100 times diffent estimators and elbow graph:", time_ed-time_st,'s')
# We want the minimum number of estimators that still yield maximum performance
# Thus, the optimal number of trees is 10
#rf = RandomForestClassifier(n_estimators=10)
# --------------------------------------------------------------
# Feature importances
# --------------------------------------------------------------
rf = RandomForestClassifier(n_estimators=10,random_state=123)
rf.fit(x_train,y_train)
# decrease impurity
ft_imp = pd.Series(rf.feature_importances_,index=cancer_data.feature_names).sort_values(ascending=False)
print(ft_imp.head(10))
# only use "worst" features to build a new model
a = rf.score(x_test,y_test)
print("model accuracy with all features:", a)
worst_cols = [col for col in df.columns if 'worst' in col]
print(worst_cols)
x_worst = df[worst_cols]
x_train,x_test,y_train,y_test = train_test_split(x_worst,y,random_state=123)
rf.fit(x_train,y_train)
b = rf.score(x_test,y_test)
print("model accuracy with \'critical\' features:", b)
