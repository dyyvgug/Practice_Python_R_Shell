import pandas as pd

pd.options.display.max_columns = 6
df = pd.read_csv('random1000pairs.csv')
#print(df.head())
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
# index of array
'''print(di_array_twoDIM)
print(di_array_twoDIM.shape) #size

print(di_array_twoDIM[0,1])   # get a single element
print(di_array_twoDIM[0])   #get single row, another express method : di_array_twoDIM[0,:]
print(di_array_twoDIM[:,1]) #get single column '''
# set conditions
mask = di_array_twoDIM[:,1] > 0.12   #mask is a boolean array
co = di_array_twoDIM[mask]
#print(co)
# write the above in a single line
co = di_array_twoDIM[di_array_twoDIM[:, 1] > 0.12]
print(co)
print(mask.sum())   # get count, 
print((di_array_twoDIM[:,1] > 0.12).sum()) #needn't define mask
