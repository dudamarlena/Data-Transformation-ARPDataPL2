# import
import pandas as pd
import numpy as np

# Tworzenie Series
l1 = [1, 2, 3, 4]
l2 = list((1, 2, 3, 4))
l3 = (1, 2, 3, 4)
l4 = np.random.random(size=4)
s1 = pd.Series(l4, index=['A', 'B', 'C', 'D'], name='numbers', dtype=int)

# Tworzenie DataFrame
data = {
    "col1": [1, 2, 3],
    "col2": [4.1, 5.2, 6.3],
    "col3": ["A", "B", "C"],
}
data2 = np.array([[1, 2], [1, 2]])

df = pd.DataFrame(data=data)
df2 = pd.DataFrame(data=data2, columns=['col1', 'col2'])

series_1 = df['col1']
dataframe_1 = df[['col1']]
print(f'Series: {type(series_1)}, DataFrame: {type(type(dataframe_1))}')

# Wyswietlanie danych
print(df)
print('-------------------')
# by names
print(df.loc[1, 'col1'])
print(df.loc[:, ['col1', 'col2']])

# by index
print(df.iloc[1, 0:1])
print(df.iloc[:, :-1])
print(f'base shape: ', df.shape)

# Dodawanie kolumn
df['new_col'] = 'v'
df['new_col_list'] = ['v1', 'v2', 'v3']
df['new_col_series'] = pd.Series(['v1', 'v2', 'v3'])
print(f'shape with new columns: ', df.shape)

# Usuwanie kolumn
del df['new_col_series']
df = df.drop(labels=['col1'], axis=1)
df = df.drop(columns=['col2', 'col3'])
print(f'shape after del columns: ', df.shape)

# Filtrowanie danych
new_data = {
    "col1": [1, 2, 3, 4] * 2,
    "col2": [4.1, 5.2, 6.3, 2.1] * 2,
    "col3": ["A", "B", "C", "A"] * 2,
}
new_df = pd.DataFrame(new_data)
a_values = new_df[new_df['col3'] == "A"]
print(new_df['col3'] == "A")
print(a_values)

a_4_values = new_df[(new_df['col3'] == "A") & (new_df['col1'] > 3)]

a_values['col2'][a_values['col2'] > 3] = 0

print(f'Mean: {new_df["col1"].mean()}, Std: {new_df["col1"].std()}, Min: {new_df["col1"].min()}, '
      f'Count: {new_df["col1"].count()} or {len(new_df["col1"])}')



# Operacje na Series i DataFrames

# Łączenie DataFrames
