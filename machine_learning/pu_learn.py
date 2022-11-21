'''
Elkan & Noto Learning classifiers from only positive and unlabeled data"
This learning note is from Alon Agmon 
'''
import pandas as pd
import numpy as np

url = "http://archive.ics.uci.edu/ml/machine-learning-databases/00267/data_banknote_authentication.txt"
data = pd.read_csv(url,header=None)
print(data.shape)
print(data.head(5))