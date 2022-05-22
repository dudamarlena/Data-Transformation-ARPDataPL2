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
data2 = np.array([1, 2, 3, 4, 5])

df = pd.DataFrame(data=data)

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



# Dodawanie kolumn

# Usuwanie kolumn

# Filtrowanie danych

# Operacje na Series i DataFrames

# Łączenie DataFrames
