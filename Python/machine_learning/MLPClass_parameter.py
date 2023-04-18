from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_features=2, n_redundant=0, n_informative=2, random_state=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3)
mlp = MLPClassifier(max_iter=1000, hidden_layer_sizes=(100, 50), alpha=0.0001, solver='adam', random_state=3)
mlp.fit(X_train, y_train)
print("accuracy:", mlp.score(X_test, y_test))

mlp2 = MLPClassifier (max_iter =1500, hidden_layer_sizes =(100, 50), alpha = 0.01, solver ='sgd', random_state =3)
mlp2.fit(X_train, y_train)
print ("accuracy2:", mlp2.score(X_test, y_test ))
