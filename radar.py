import pandas as pd

df = pd.read_csv('./stats_dataset/charcters_stats.csv')
print(df.sort_values(by=['Total'],ascending=False))

select_list = ['Iron Man', 'Thor', 'Wolverine', 'Captain America', 'Deadpool', 'Doctor Strange', 'Hulk', 'Black Panther', 'Black Widow']
res = df[df['Name'] == 'Spider-Man']
for i in select_list:
    res = pd.concat([res, df[df['Name'] == i]], ignore_index=True)

res.to_csv('./stats_dataset/marvel_stats.csv', index=False)