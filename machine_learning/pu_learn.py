'''
Elkan & Noto Learning classifiers from only positive and unlabeled data"
This learning note is from Alon Agmon
'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import xgboost as xgb

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
data = pd.read_csv(url,header=None)
print(data.shape)
print(data.head(5))
# the first 4 columns are the features of Wavelet Transformed image.
# the 5th column is the tag that genuine money is 1, others(genuine + fake) are 0
# check the counts of positive and negative
print(data.iloc[:,-1].value_counts()) # through index get value

# ==============================================================
# train a baseline classifier
# ==============================================================
x_data = data.iloc[:,:-1]
y_data = data.iloc[:,-1]
# 20% training set, 75% is default
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=7)
# use boost, randomly generate trees
model = xgb.XGBClassifier()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
