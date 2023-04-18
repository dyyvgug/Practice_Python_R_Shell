from sklearn.datasets import make_classification
from matplotlib import pyplot as plt

X, y = make_classification(n_features=2, n_redundant=0, n_informative=2, random_state=3)
print(X)
print(y)

# n_informative means showing how many elements each line 

i,j = make_classification (n_features =3, n_redundant =0, random_state =5, n_informative =2)
print (i)
print (j)

plt.scatter(X[y==0][:, 0], X[y==0][:, 1], s=100, edgecolors='k')
plt.scatter(X[y==1][:, 0], X[y==1][:, 1], s=100, edgecolors='k', marker='^')
plt.show()
