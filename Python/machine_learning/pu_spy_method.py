import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, precision_recall_curve, auc


# ---------------------------------------------------------------------------------------
# Generate Data (Simulating Fraud Scenario)
# ---------------------------------------------------------------------------------------
X, y = make_classification(n_samples=1000, n_features=10, weights=[0.95], random_state=42)
y[y == 0] = -1  # Simulate unlabeled data (-1), some could be positive
# Mark a Subset as Positive
y_labeled = y.copy()
positive_idx = np.random.choice(np.where(y == 1)[0], size=50, replace=False)  # Take 50 positive samples
y_labeled[positive_idx] = 1
y_labeled[np.where(y_labeled != 1)[0]] = 0  # Mark the rest as unlabeled (0)
# Split into Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y_labeled, test_size=0.3, random_state=42)
# ----------------------------------------------------------------------------------------
# Step 1: Reliable Negative Identification (Spy Technique as example)
# ----------------------------------------------------------------------------------------
spy_size = 20
spy_idx = np.random.choice(positive_idx, size=spy_size, replace=False)
X_unlabeled = np.concatenate((X[y == -1], X[spy_idx]))
y_unlabeled = np.array([-1] * len(X[y == -1]) + [1] * spy_size)

basic_classifier = SVC(kernel='linear', probability=True)
basic_classifier.fit(X_train, y_train)
reliable_negative_idx = np.where(basic_classifier.predict_proba(X_unlabeled)[:, 0] >= 0.95)[0]
num_reliable_negatives = len(reliable_negative_idx)  # Calculate the count
print(f"Number of reliable negative samples found: {num_reliable_negatives}")
# ----------------------------------------------------------------------------------------
# Step 2: Learning with Reliable Negatives
# ----------------------------------------------------------------------------------------
X_train_pn = np.concatenate((X[positive_idx], X_unlabeled[reliable_negative_idx]))
y_train_pn = np.concatenate((np.ones(len(positive_idx)), -np.ones(len(reliable_negative_idx))))

final_classifier = LogisticRegression()
final_classifier.fit(X_train_pn, y_train_pn)

# ----------------------------------------------------------------------------------------
# Evaluation
# ----------------------------------------------------------------------------------------
y_predicted = final_classifier.predict(X_test)

# Confusion Matrix (with special focus)
cm = confusion_matrix(y_test, y_predicted)
print(cm)

# Precision, Recall, AUC-PR
precision, recall, _ = precision_recall_curve(y_test, final_classifier.predict_proba(X_test)[:, 1])
auc_pr = auc(recall, precision)

print(f"Precision: {precision[1]:.3f} (Ideally close to 1)")
print(f"Recall: {recall[1]:.3f} (Higher is often desired in PU scenarios)")
print(f"AUC-PR: {auc_pr:.3f}")


