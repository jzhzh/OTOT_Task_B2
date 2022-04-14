from textrank import get_textrank
import pandas as pd
# from line_profiler import LineProfiler
# import line_profiler
import spacy
import pytextrank


# def test1():
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe("textrank")

df = pd.read_csv('./text_dataset/mcu_subset.csv', index_col= 0)
select_df = df[df['character'] == 'TONY STARK']
select_df = select_df.reset_index(drop=True)

# df = df[:20000]
df_extracted = pd.DataFrame(columns=['character', 'line'])
df_extracted['character'] = select_df['character']
# i = 1
for index, row in select_df.iterrows():
    print('Processing: {}/{}'.format(index, select_df.shape[0]))
    result = get_textrank(str(row['line']), nlp)
    df_extracted.loc[index]['line'] = result
    # i += 1
    # if i > 50:
    #     break
# df_extracted.to_csv('keywords.csv', index=False, header=0)
df_extracted.to_csv('./text_dataset/keywords.csv', index=False)

# if __name__=='__main__':
#     lp=LineProfiler()
#     lp.add_function(get_textrank)
#     lp_wrap=lp(test1)
#     lp_wrap()
#     lp.print_stats()

