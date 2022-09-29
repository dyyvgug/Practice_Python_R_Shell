import pandas as pd

pd.options.display.max_columns = 6
df = pd.read_csv('random1000pairs.csv')
print(df.head())
#print(df.describe())
#check size
#print(df.shape)

# choose one column
col = df['di']
#print(col)

# select multiple columns
sub_df = df[['corr', 'di']]
#print(sub_df)

# one column of df to array, for numpy calculating
di_array_oneDIM = df['di'].values
#print(df['di'].values)

# whole df to array
di_array_twoDIM = df[['corr', 'di']].values
#print(di_array_twoDIM)
#print(di_array_twoDIM.shape)