import pandas as pd

# Example DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2']},
                   index=['K0', 'K1', 'K2'])
print(df1)

df2 = pd.DataFrame({'B': ['B0', 'B1', 'B2']},
                   index=['K0', 'K1', 'K2'])
print(df2)
# Merge using indices as join keys
result = pd.merge(df1, df2, left_index=True, right_index=True)

print(result)
