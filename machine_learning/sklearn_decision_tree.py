import numpy as np
import pandas as pd
import graphviz
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    precision_recall_fscore_support, roc_auc_score, roc_curve
from IPython.display import Image

df = pd.read_csv('titanic_noNA.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y = df['Survived'].values
x_train, x_test, y_train, y_test = train_test_split(X, y, random_state=22)

model = DecisionTreeClassifier()
model.fit(x_train, y_train)
# predict the person who is pcalss 3, Male, 22 years old, has 1 siblings, 0 children, fare is 7.25
print(model.predict([[3, True, 22, 1, 0, 7.25]]))
# it shows he didn't survive

# calculate accuracy, precision and recall
print("accuracy:", model.score(x_test, y_test))
y_pred = model.predict(x_test)
print("precision:", precision_score(y_test, y_pred))
print("recall:", recall_score(y_test, y_pred))

# check if it's a good split. k-fold, gini and entropy
kf = KFold(n_splits=5, shuffle=True)
for criterion in ['gini', 'entropy']:
    print("decision tree - {}".format(criterion))
    accuracy = []
    precision = []
    recall = []
    for train_index, test_index in kf.split(X):
        x_train, x_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        dt = DecisionTreeClassifier(criterion=criterion)
        dt.fit(x_train, y_train)
        y_pred = dt.predict(x_test)
        accuracy.append(accuracy_score(y_test,y_pred))
        precision.append(precision_score(y_test,y_pred))
        recall.append(recall_score(y_test,y_pred))
    print("accuracy:", np.mean(accuracy))
    print("precision:", np.mean(precision))
    print("recall:", np.mean(recall))

# visualizing the tree
feature_names = ['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']
x = df[feature_names].values
y = df['Survived'].values

dt2 = DecisionTreeClassifier()
dt2.fit(x, y)
dot_file = export_graphviz(model, feature_names=feature_names)
graph = graphviz.Source(dot_file)  # dot to img
graph.render(filename='decision_tree', format='png', cleanup=True)

# ----------------------- Pruning ---------------------------
# Pruning the decision tree to fix the overfitting
dt3 = DecisionTreeClassifier(max_depth=3, min_samples_leaf=2, max_leaf_nodes=10)
# Sklearn has Grid search class to do loop cross validation, then we can decide how pruning
param_grid = {
    'max_depth': [5, 15, 25],
    'min_samples_leaf': [1,3],
    'max_leaf_nodes': [10,20,35,50]
}
dt4 = DecisionTreeClassifier()
gs = GridSearchCV(dt4, param_grid, scoring='f1', cv=5)  # 5-fold cross validation
gs.fit(X,y)
print('best params:', gs.best_params_)
print('best score:', gs.best_score_)
