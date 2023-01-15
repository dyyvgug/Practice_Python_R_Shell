from sklearn.datasets import make_classification
X, y = make_classification(n_features=2, n_redundant=0, n_informative=2, random_state=3)
print(X)
print(y)

# n_informative means showing how many elements each line 

i,j = make_classification (n_features =3, n_redundant =0, random_state =5, n_informative =2)
print (i)
print (j)
