import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
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
print("random forest accuracy:", rf.score(x_test,y_test))

dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)
print("decision tree accuracy:", dt.score(x_test,y_test))

lr = LogisticRegression(solver='liblinear')
lr.fit(x_train,y_train)
print("Logistic Regression accuracy:",lr.score(x_test,y_test))
