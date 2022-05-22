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
    "col3": ['A', "B", "C"]
}
df = pd.DataFrame(data=data)
print(df)

# Wyswietlanie danych

# Dodawanie kolumn

# Usuwanie kolumn

# Filtrowanie danych

# Operacje na Series i DataFrames

# Łączenie DataFrames
