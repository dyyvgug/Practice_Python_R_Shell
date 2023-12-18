import pandas as pd
from sklearn.decomposition import PCA
import numpy as np

# Simulating a dataframe with 1024 columns and 10000 rows
np.random.seed(0)  # For reproducible results
data = np.random.rand(10000, 1024)
df = pd.DataFrame(data)

# Applying PCA to reduce to 100 columns
pca = PCA(n_components=100)
reduced_df = pca.fit_transform(df)

# Creating a new DataFrame from the reduced data
reduced_df = pd.DataFrame(reduced_df)

# The reduced_df now has 100 columns and the same 10000 rows
print(reduced_df.shape)
