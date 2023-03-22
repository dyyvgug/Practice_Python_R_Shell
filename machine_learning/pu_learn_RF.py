from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.semi_supervised import LabelPropagation
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Generate synthetic data
X, y = make_classification(n_samples=10000, n_features=10, n_informative=5, n_redundant=0, n_clusters_per_class=1, class_sep=0.5, random_state=42)

# randomly select 50% of the positive samples as labeled data
pos_idx = np.where(y == 1)[0]
pos_labeled_idx = np.random.choice(pos_idx, int(len(pos_idx) * 0.5), replace=False)
pos_unlabeled_idx = np.setdiff1d(pos_idx, pos_labeled_idx)

# define labels for labeled and unlabeled data
y_labeled = np.zeros(len(y))
y_labeled[pos_labeled_idx] = 1
y_unlabeled = -1 * np.ones(len(y))
y_unlabeled[pos_unlabeled_idx] = 0

# split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# encode the labels to be used with the LabelPropagation model
le = LabelEncoder()
y_labeled = le.fit_transform(y_labeled)
y_unlabeled = le.transform(y_unlabeled)

# create a random forest classifier to use for PU learning
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# fit the classifier to the labeled and unlabeled data using PU learning
lp_model = LabelPropagation(kernel='knn', n_neighbors=10)
lp_model.fit(X=np.vstack((X_train, X_test)), y=np.hstack((y_labeled, y_unlabeled)))
pos_mask = lp_model.transduction_[pos_unlabeled_idx] == 1
X_pos_unlabeled = X[pos_unlabeled_idx][pos_mask]
y_pos_unlabeled = np.ones(len(X_pos_unlabeled))
X_train_pu = np.vstack((X_train, X_pos_unlabeled))
y_train_pu = np.hstack((y_train, y_pos_unlabeled))
clf.fit(X_train_pu, y_train_pu)

# predict on the test set
y_pred = clf.predict(X_test)

# evaluate the performance of the classifier
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy: {acc}")