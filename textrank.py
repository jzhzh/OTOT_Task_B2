import pandas as pd
import spacy
import pytextrank
import random

def get_textrank(sentence, nlp):
    # nlp = spacy.load('en_core_web_sm')

    # nlp.add_pipe("textrank")

    # df = pd.read_csv('lyrics_data.csv', names=['name', 'lyrics'])

    # if __name__ == "__main__":
    #     df_extracted = pd.DataFrame(columns=['name', 'lyrics'])
    #     df_extracted['name'] = df['name']
    #     for index, row in df.iterrows():
    #         doc = nlp(row['lyrics'])
    #         temp = []
    #         i = 1
    #         for phrase in doc._.phrases:
    #             temp.append(phrase.text)
    #             if i >= 5:
    #                 df_extracted.iloc[index]["lyrics"] = temp
    #                 print(df_extracted.iloc[index]["lyrics"])
    #                 break
    #             i += 1
    #     df_extracted.to_csv('keywords.csv', index=False)

    doc = nlp(sentence)
    pos_list = {}
    for tok in doc:
        pos_list[tok.text] = tok.pos_
    n = []
    v = []
    adj = []
    others = []
    if len(doc._.phrases) > 0:
        pos_list.clear()
        for top_phrases in doc._.phrases:
            if len(top_phrases.text) > 0:
                result_temp = top_phrases.text
                break
            else:
                continue
        re_doc = nlp(result_temp)
        for token in re_doc:
            pos_list[token.text] = token.pos_
    
    for key, value in pos_list.items():
        if value == 'NOUN':
            n.append(key)
        elif value == 'VERB':
            v.append(key)
        elif value == 'ADJ':
            adj.append(key)
        else:
            others.append(key)
    
    if len(n) > 0:
        result = random.choice(n)
    elif len(v) > 0:
        result = random.choice(v)
    elif len(adj) > 0:
        result = random.choice(adj)
    else:
        result = random.choice(others)
    
    keyword = result

    print(keyword)
    return keyword
    
        # if num <= len(sentence_split):
        #     result = random.sample(sentence_split, num)
        #     print(result)
        #     return result
        # else:
        #     print('The number of keywords exceeds the number of words in the sentence itself.')
    # else:
            # if num > len(doc._.phrases):
            #     print('The number of keywords exceeds the number of phrases contained in the sentence itself.')
            #     break
            # else:
            #     result.append(phrase.text)
            #     if i >= num:
            #         print(result)
            #         return result
            #     i += 1
