import pandas as pd

data = pd.read_csv(r"Datasets/cars.csv", sep=";")
print(data.info())
print(data.describe())
# print(data.head(n=10))
# print(data.tail(n=10))
# print(data.sample(n=10))

objects_data = data.select_dtypes(object)
print(objects_data.describe())

float_data = data.select_dtypes(float)
print(float_data.describe())

int_data = data.select_dtypes(int)
print(int_data.describe())
