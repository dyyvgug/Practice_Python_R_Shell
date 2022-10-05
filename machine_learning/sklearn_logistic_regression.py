import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv('titanic_noNA.csv')
df['male'] = df['Sex'] == 'male'
X = df[['Pclass','male','Age','Siblings/Spouses','Parents/Children','Fare']].values
y = df['Survived'].values
#print(x)
#print(y)

model = LogisticRegression()
model.fit(X,y)
print(model.coef_,model.intercept_)
# [[-1.19324152e+00 -2.50691271e+00 -4.27099569e-02 -3.59677077e-01
#   -5.24958165e-02  2.38996454e-03]] [5.14869004]

print(model.predict([[3,True,22.0,1,0,7.25]]))
# 0, not survive
print(model.predict([[1,True,37,0,1,320]]))
# 1, survive
print(model.predict(X[:5]))
print(y[:5])
# all 5 correct


