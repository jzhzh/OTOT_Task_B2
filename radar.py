import pandas as pd

df = pd.read_csv('./stats_dataset/charcters_stats.csv')
print(df.sort_values(by=['Total'],ascending=False))

# A list of the names of the characters that we want to select from the dataframe.
select_list = ['Iron Man', 'Thor', 'Wolverine', 'Captain America', 'Deadpool', 'Doctor Strange', 'Hulk', 'Black Panther', 'Black Widow']
res = df[df['Name'] == 'Spider-Man']

# Looping through the select_list and concatenating the dataframe with the rows that match the name in the select_list.
for i in select_list:
    res = pd.concat([res, df[df['Name'] == i]], ignore_index=True)

# Saving the dataframe to a csv file.
res.to_csv('./stats_dataset/marvel_stats.csv', index=False)