'''
Elkan & Noto Learning classifiers from only positive and unlabeled data"
This learning note is from Alon Agmon
'''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, \
    precision_recall_fscore_support, roc_auc_score, roc_curve
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
# in y dataset, 1 is positive, 0 is negative
x_data = data.iloc[:,:-1]
y_data = data.iloc[:,-1]
# 20% training set, 75% is default
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.2, random_state=7)
# use boost, randomly generate trees
model = xgb.XGBClassifier()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

def evaluate_results(y_test, y_pred):
    print("the classifier results:")
    f1 = f1_score(y_test,y_pred)
    print("f1: {:.2f}".format(f1 * 100.0))
    roc = roc_auc_score(y_test,y_pred)
    print("roc: {:.2f}".format(roc * 100.0))
    rec = recall_score(y_test,y_pred,average='binary')
    print("recall: {:.2f}".format(rec * 100.0))
    prc = precision_score(y_test,y_pred,average='binary')
    print("precision: {:.2f}".format(prc * 100.0))

evaluate_results(y_test,y_pred)

# ===================================================
# Test the PU learning
# keep aside 25% of the positives
# ===================================================
mod_data = data.copy()
# get the index of the positives samples
pos_ind = np.where(mod_data.iloc[:,-1].values == 1)[0]
#print(pos_ind)
np.random.shuffle(pos_ind)

# leave just 25% of the positives marked
pos_sample_len = int(np.ceil(0.25 * len(pos_ind)))  # .ceil get int from up
#print(pos_sample_len)
#print(len(pos_ind))
print("Using {} as positives and unlabelling the rest".format(1-pos_sample_len/(len(pos_ind))))

pos_sample = pos_ind[:pos_sample_len]
# create 'class_test', 1 for positive and -1 for unlabelled
mod_data['class_test'] = -1
mod_data.loc[pos_sample,'class_test'] = 1
print('target variable:\n',mod_data.iloc[:,-1].value_counts())
# 153 positive and 1219 unlabelled
print(mod_data.head(10))
x_data = mod_data.iloc[:,:-2].values # just the X
y_labeled = mod_data.iloc[:,-1].values # new class (just the P & U)
y_positive = mod_data.iloc[:,-2].values # original class

def fit_pu_estimator(X,y,hold_out_ratio,estimator):
    # find the indices of the positive/labeled elements
    assert (type(y) == np.ndarray), "Must pass np.ndarray rather than list as y"
    positives = np.where(y == 1.)[0]
    # hold_out_size = the *number* of positives/labeled samples
    # that we will use later to estimate P(s=1|y=1)
    hold_out_size = int(np.ceil(len(positives) * hold_out_ratio))
    np.random.shuffle(positives)
    # hold_out = the *indices* of the positive elements
    hold_out = positives[:hold_out_size]
    # the actual positive *elements* that we will keep aside
    X_hold_out = X[hold_out]
    # remove the held out elements from X and y
    X = np.delete(X, hold_out, 0)
    y = np.delete(y, hold_out)
    # We fit the estimator on the unlabeled samples + (part of the) positive and labeled ones.
    # In order to estimate P(s=1|X) or  what is the probablity that an element is *labeled*
    estimator.fit(X, y)
    # We then use the estimator for prediction of the positive held-out set
    # in order to estimate P(s=1|y=1)
    hold_out_predictions = estimator.predict_proba(X_hold_out)
    # take the probability that it is 1
    hold_out_predictions = hold_out_predictions[:, 1]
    # save the mean probability
    c = np.mean(hold_out_predictions)
    return estimator, c
