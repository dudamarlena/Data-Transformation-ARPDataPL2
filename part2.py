import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv(r"Datasets/cars.csv", sep=";")
# print(data.info())
# print(data.describe())
# print(data.head(n=10))
# print(data.tail(n=10))
# print(data.sample(n=10))

# print(data.select_dtypes(object).describe())
# usuwanie danych
del data['Unnamed: 5']
del data['TYPE']

print(data.select_dtypes(object).describe())
# Usuwanie nan
print(data[data['Make'].isna()])
print(data[(data['Model'] == "MODEL S (70 kWh battery)") | (data['Model'] == 'MODEL S (85/90 kWh battery)')])
data.fillna("TESLA", inplace=True)

# standaryzacja danych
# print(data['Make'].unique())
# data.replace("NISAN", "NISSAN", inplace=True)
# print(data['Make'].unique())

print(data['TIME (h)'].unique())
data['TIME (h)'] = data['TIME (h)'].apply(lambda x: 4 if x == 'four' else int(x))
print(data['TIME (h)'].unique())

print(data.select_dtypes(object).describe())

# float_data = data.select_dtypes(float)
# print(float_data.describe())
#
# int_data = data.select_dtypes(int)
# print(int_data.describe())

# duplikaty

# dyskretyzacja

# one hot encoding

# usuwanie szumów

# praca z datami

# nornalizacja, standaryzacja

# transformacja logarytmiczna
dummy_list = pd.Series([0, 0, 1, 3, 2, 2, 1, 2, 1, 2, 2, 2, 3, 4, 7, 8, 5, 4, 10, 9, 11, 14])

