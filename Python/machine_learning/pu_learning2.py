from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC
from sklearn.utils import shuffle

import numpy as np

# Generate some random data for demonstration purposes
X, y = make_classification(n_samples=1000, n_features=10, n_classes=2, weights=[0.9, 0.1], random_state=42)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Identify the positive examples in the training set
positive_indices = np.where(y_train == 1)[0]

# Shuffle the training data
X_train_shuffled, y_train_shuffled = shuffle(X_train, y_train, random_state=42)

# Set the labels for the shuffled data
y_train_shuffled[:len(positive_indices)] = 1
y_train_shuffled[len(positive_indices):] = -1

# Train the model on the shuffled data
model = SVC(kernel='linear', probability=True, random_state=42)
model.fit(X_train_shuffled, y_train_shuffled)

# Predict the class labels for the testing data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")
