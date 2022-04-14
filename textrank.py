import pandas as pd
import spacy
import pytextrank
import random

def get_textrank(sentence, nlp):
    """
    1. Use the TextRank algorithm to extract keywords from the sentence.
    2. If the number of keywords is greater than 0, then randomly select a keyword from the list of
    keywords.
    3. If the number of keywords is 0, then randomly select a word from the sentence
    
    :param sentence: the sentence you want to extract keywords from
    :param nlp: the spacy model
    :return: A list of keywords.
    """

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
