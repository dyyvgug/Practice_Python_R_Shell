import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression

cancer_data = load_breast_cancer()
#print(cancer_data)
#print(type(cancer_data))
#print(cancer_data.keys())
#print(cancer_data['DESCR']) #another write way: print(cancer_data.DESCR)
print(cancer_data['data'].shape) # or print(cancer_data.data.shape)

df = pd.DataFrame(cancer_data['data'], columns=cancer_data['feature_names'])
df['target'] = cancer_data['target']  # 0 means malignant and 1 means benign
print(df.head())

#print(cancer_data.feature_names)
#print(df[cancer_data.feature_names])
X = df[cancer_data.feature_names].values
y = df['target'].values

# build LR model
model = LogisticRegression(solver='liblinear')
model.fit(X,y)
print("prediction for datapoint 500th :", model.predict([X[500]]))
print("the true situation is :", y[500])
print("the accuracy of the model is :",model.score(X,y))