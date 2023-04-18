from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification

X, y = make_classification(n_features=3, n_redundant=0, n_informative=3, random_state=3)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=3)
mlp = MLPClassifier(max_iter=2000)
mlp.fit(X_train, y_train)
print("accuracy:", mlp.score(X_test, y_test))
