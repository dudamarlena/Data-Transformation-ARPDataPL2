# import
import pandas as pd
import numpy as np

# # Tworzenie Series
# l1 = [1, 2, 3, 4]
# l2 = list((1, 2, 3, 4))
# l3 = (1, 2, 3, 4)
# l4 = np.random.random(size=4)
# s1 = pd.Series(l4, index=['A', 'B', 'C', 'D'], name='numbers', dtype=int)
#
# # Tworzenie DataFrame
# data = {
#     "col1": [1, 2, 3],
#     "col2": [4.1, 5.2, 6.3],
#     "col3": ["A", "B", "C"],
# }
# data2 = np.array([[1, 2], [1, 2]])
#
# df = pd.DataFrame(data=data)
# df2 = pd.DataFrame(data=data2, columns=['col1', 'col2'])
#
# series_1 = df['col1']
# dataframe_1 = df[['col1']]
# print(f'Series: {type(series_1)}, DataFrame: {type(type(dataframe_1))}')
#
# # Wyswietlanie danych
# print(df)
# print('-------------------')
# # by names
# print(df.loc[1, 'col1'])
# print(df.loc[:, ['col1', 'col2']])
#
# # by index
# print(df.iloc[1, 0:1])
# print(df.iloc[:, :-1])
# print(f'base shape: ', df.shape)
#
# # Dodawanie kolumn
# df['new_col'] = 'v'
# df['new_col_list'] = ['v1', 'v2', 'v3']
# df['new_col_series'] = pd.Series(['v1', 'v2', 'v3'])
# print(f'shape with new columns: ', df.shape)
#
# # Usuwanie kolumn
# del df['new_col_series']
# df = df.drop(labels=['col1'], axis=1)
# df = df.drop(columns=['col2', 'col3'])
# print(f'shape after del columns: ', df.shape)
#
# # Filtrowanie danych
# new_data = {
#     "col1": [1, 2, 3, 4] * 2,
#     "col2": [4.1, 5.2, 6.3, 2.1] * 2,
#     "col3": ["A", "B", "C", "A"] * 2,
# }
# new_df = pd.DataFrame(new_data)
# a_values = new_df[new_df['col3'] == "A"]
# print(new_df['col3'] == "A")
# print(a_values)
#
# a_4_values = new_df[(new_df['col3'] == "A") & (new_df['col1'] > 3)]
#
# a_values['col2'][a_values['col2'] > 3] = 0
#
# print(f'Mean: {new_df["col1"].mean()}, Std: {new_df["col1"].std()}, Min: {new_df["col1"].min()}, '
#       f'Count: {new_df["col1"].count()} or {len(new_df["col1"])}')
#
# print(new_df.mean())

# Operacje na Series i DataFrames
# new_data2 = pd.DataFrame({
#     "col1": [1, 2, 3, 4],
#     "col2": [4.1, 5.2, 6.3, 2.1]
# })
#
# new_data3 = pd.DataFrame({
#     "col1": [1, 2, 3, 4, 0],
#     "col2": [4.1, 5.2, 6.3, 2.1, 2.1]
# })
#
# added_df = new_data2 + new_data3
# added_df_2 = new_data2 + 0.5
# added_df_3 = new_data2 + 5
#
#
# def add_values(x):
#     return x + 2 + 4 + 9
#
#
# new_data2['col3'] = new_data2['col1'].apply(add_values)

# new_data2['col4'] = new_data2['col1'].apply(lambda x: x + 2 + 4 + 9)
# print(new_data2)
#
# """
# new_data4 = pd.DataFrame({
#     "col1": [1, 2, 3, 4] + [0]*5,
#     "col2": [4.1, 5.2, 6.3, 2.1] + [0]*5
# }) """

# Łączenie DataFrames

# data = pd.DataFrame({
#     "Age_id": [1, 2, 3, 4],
#     "Age": [4, 52, 63, 21]
# })
#
# data2 = pd.DataFrame({
#     "Age_id": [1, 2, 3, 4],
#     "Name": ['A', 'B', 'C', 'D']
# })
#
# merge_1 = data.merge(data2)
# print(merge_1)
# merge_2 = data.merge(data2, left_on="Age_id")  # jesli nazwa kolumny jest taka sama w obu DFs
# merge_3 = data.merge(data2, how="right", left_on="Age_id", right_on="age_id")
# merge_4 = data.merge(data2, how="outer", left_on="Age_id", right_on="age_id")
# print(merge_4)

# join_1 = data.join(data2, on="Age_id", lsuffix="_l", rsuffix="_r", how="inner")
# print(join_1)


data = pd.DataFrame({
    "Age_id": [1, 2, 3, 4],
    "Age": [4, 52, 63, 21]
})

data2 = pd.DataFrame({
    "Age_id": [1, 2, 3, 4],
    "Age": [4, 52, 63, 21]
})

append_df = data.append(data2)
append_df = append_df.set_index('Age_id')
append_df = append_df.reset_index()
print(append_df)

concat_df = pd.concat([data, data2], axis=1)
# print(concat_df)

# data = pd.DataFrame(data, columns=['age_id', "Name", "Age_id", "Age"]) # zmiana kolejnosci kolumn
