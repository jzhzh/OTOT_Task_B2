from textrank import get_textrank
import pandas as pd
import spacy
import pytextrank



# Loading the spacy model.
nlp = spacy.load('en_core_web_sm')
# Adding a pipeline to the spacy model.
nlp.add_pipe("textrank")

# Reading the csv file and setting the first column as the index.
df = pd.read_csv('./text_dataset/mcu_subset.csv', index_col= 0)
# Selecting the rows where the character is Tony Stark.
select_df = df[df['character'] == 'TONY STARK']
# Resetting the index of the dataframe.
select_df = select_df.reset_index(drop=True)

# df = df[:20000]
# Creating a dataframe with two columns, 'character' and 'line'.
df_extracted = pd.DataFrame(columns=['character', 'line'])

df_extracted['character'] = select_df['character']

# Iterating through the dataframe and adding the result of the get_textrank function to the dataframe.
for index, row in select_df.iterrows():
    print('Processing: {}/{}'.format(index, select_df.shape[0]))
    result = get_textrank(str(row['line']), nlp)
    df_extracted.loc[index]['line'] = result


# Saving the dataframe to a csv file.
df_extracted.to_csv('./text_dataset/keywords.csv', index=False)


