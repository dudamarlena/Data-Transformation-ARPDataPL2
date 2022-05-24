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

# print(data.select_dtypes(object).describe())
# Usuwanie nan
# print(data[data['Make'].isna()])
# print(data[(data['Model'] == "MODEL S (70 kWh battery)") | (data['Model'] == 'MODEL S (85/90 kWh battery)')])
data.fillna("TESLA", inplace=True)

# standaryzacja danych
# print(data['Make'].unique())
# data.replace("NISAN", "NISSAN", inplace=True)
# print(data['Make'].unique())

# print(data['TIME (h)'].unique())
data['TIME (h)'] = data['TIME (h)'].apply(lambda x: 4 if x == 'four' else int(x))
# print(data['TIME (h)'].unique())

# print(data.select_dtypes(object).describe())

# float_data = data.select_dtypes(float)
# print(float_data.describe())
#
# int_data = data.select_dtypes(int)
# print(int_data.describe())

# duplikaty
# duplicated_records
# print(any(data.duplicated()))
# data_with_duplicates = data.append(data.iloc[:1])
# print(any(data_with_duplicates.duplicated()))
# data_without_duplicates = data_with_duplicates.drop_duplicates()
# print(any(data_without_duplicates.duplicated()))

# dyskretyzacja
# print(sorted(data['(kW)'].unique()))
bins = [34, 130, 300, 3860]
data['(kW) bins'] = pd.cut(data['(kW)'], bins=bins, labels=["Low", "Medium", "High"])
# print(data['(kW) bins'])

# one hot encoding
# print(pd.get_dummies(data['(kW) bins']))
data = pd.concat([data, pd.get_dummies(data['(kW) bins'])], axis=1)

del data['(kW) bins']
# print(data.info())

# usuwanie szumów

# praca z datami

# nornalizacja, standaryzacja

# transformacja logarytmiczna
dummy_list = pd.Series([0, 0, 1, 3, 2, 2, 1, 2, 1, 2, 2, 2, 3, 4, 7, 8, 5, 4, 10, 9, 11, 14])

