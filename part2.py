import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# data = pd.read_csv(r"Datasets/cars.csv", sep=";")
# print(data.info())
# print(data.describe())
# print(data.head(n=10))
# print(data.tail(n=10))
# print(data.sample(n=10))

# print(data.select_dtypes(object).describe())
# usuwanie danych
# del data['Unnamed: 5']
# del data['TYPE']

# print(data.select_dtypes(object).describe())
# Usuwanie nan
# print(data[data['Make'].isna()])
# print(data[(data['Model'] == "MODEL S (70 kWh battery)") | (data['Model'] == 'MODEL S (85/90 kWh battery)')])
# data.fillna("TESLA", inplace=True)

# standaryzacja danych
# print(data['Make'].unique())
# data.replace("NISAN", "NISSAN", inplace=True)
# print(data['Make'].unique())

# print(data['TIME (h)'].unique())
# data['TIME (h)'] = data['TIME (h)'].apply(lambda x: 4 if x == 'four' else int(x))
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
# bins = [34, 130, 300, 3860]
# data['(kW) bins'] = pd.cut(data['(kW)'], bins=bins, labels=["Low", "Medium", "High"])
# print(data['(kW) bins'])

# one hot encoding
# print(pd.get_dummies(data['(kW) bins']))
# data = pd.concat([data, pd.get_dummies(data['(kW) bins'])], axis=1)

# del data['(kW) bins']
# print(data.info())

# usuwanie szumów - outliers
# print(sorted(data['(kW)'].unique()))

# data = data[data['(kW)'] < 600]

# factor = 3  # musi byc <2,4>

# upper_limit = data['(kW)'].mean() + data['(kW)'].std() * factor
# lower_limit = data['(kW)'].mean() - data['(kW)'].std() * factor
# print(f'Upper: {upper_limit}, Lower: {lower_limit}')
#
# data = data[(data['(kW)'] < upper_limit) & (data['(kW)'] > lower_limit)]
# print(sorted(data['(kW)'].unique()))

# upper_limit = data['(kW)'].quantile(0.95)
# lower_limit = data['(kW)'].quantile(0.05)
# print(f'Upper: {upper_limit}, Lower: {lower_limit}')
#
# data = data[(data['(kW)'] < upper_limit) & (data['(kW)'] >= lower_limit)]
# print(sorted(data['(kW)'].unique()))

# plt.scatter(data.index, data['(kW)'])
# plt.show()

# praca z datami
# data['date'] = '01/01/2000'
# data['date'] = pd.to_datetime(data['date'])
# data['new date'] = pd.date_range(start='01/01/2000', periods=len(data), freq="M")
# print(data['new date'])
# data['Year'] = data['new date'].dt.year
# data['Month'] = data['new date'].dt.month
# data['Year and month'] = data['new date'].dt.to_period("M")
# print(data['Year and month'])

# normalizacja, standaryzacja
# x_min = data['TIME (h)'].min()
# x_max = data['TIME (h)'].max()
# x = data['TIME (h)']
# data['TIME (h) normalized'] = (x - x_min) / (x_max - x_min)
#
# print("Initial data for Time: ", sorted(data['TIME (h)'].unique()))
# print("Normalized data for Time: ", sorted(data['TIME (h) normalized'].unique()))
#
# x_min_kw = data['(kW)'].min()
# x_max_kw = data['(kW)'].max()
# x_kw = data['(kW)']
# data['(kW) normalized'] = (x_kw-x_min_kw) / (x_max_kw-x_min_kw)
# print("Initial data for kW: ", sorted(data['(kW)'].unique()))
# print("Normalized data for kW: ", sorted(data['(kW) normalized'].unique()))
#
# # plt.plot(data['TIME (h)'])
# plt.plot(data['TIME (h) normalized'])
# # plt.plot(data['(kW)'])
# plt.plot(data['(kW) normalized'])
# plt.show()

# transformacja logarytmiczna
# dummy_list = pd.Series([0, 0, 1, 3, 2, 2, 1, 2, 1, 2, 2, 2, 3, 4, 7, 8, 5, 4, 10, 9, 11, 14])
# log_1 = (dummy_list + 1).transform(np.log)
# plt.hist(x=log_1, bins=11)
# plt.show()

from pandas_profiling import ProfileReport

data = pd.read_csv(r"Datasets/cars.csv", sep=";")
report = ProfileReport(data)
report.to_file("report.html")
