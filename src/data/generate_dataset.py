import json
import pandas as pd
import numpy as np
import re


def read_txt(path):
    '''returns list of strings loaded from txt file'''
    with open(path,encoding="utf8") as f:
        return f.readlines()


def label_parser(txt):
    '''takes full txt as input and parsers text to return a dataframe with postures(target label) and doc id '''
    # df initializations
    outer_df = pd.DataFrame()
    inner_df = pd.DataFrame()
    # appending rows
    for data in txt:
        data = json.loads(data)
        if len(data['postures']) == 0: #to handle missing postures
            inner_df = pd.DataFrame(["None"],columns= ['postures'])
        else:
            inner_df = pd.DataFrame(data['postures'],columns= ['postures'])
        inner_df['documentId'] = data['documentId']
        outer_df = outer_df.append(inner_df,ignore_index=True)
    return outer_df


def get_cumsum_distribution(df,col):
    '''return cumsum distrbution by specifed col'''
    df=pd.DataFrame(df[col].value_counts())
    df['Cum sum']=df[col].cumsum()
    df['Cum sum %'] = df['Cum sum']/df[col].sum()
    return df


def paragraph_parser(txt):
    '''parsing fn that returns paragraph text and paragrpah counts per documentid'''
    parser_df = []
    for data in txt:
        data = json.loads(data)
        para_counter = 0
        para_string = ''
        for section in data['sections']:
            for paragraph in section['paragraphs']:
                #print(paragraph)
                para_counter=para_counter+1
                para_string+=paragraph
        num_words = len(re.findall('\w+', para_string.lower())) ##regex to find num_words
        parser_df.append([data['documentId'],para_counter,para_string,num_words])
    parser_df = pd.DataFrame(parser_df,columns=['documentId','para_num','para_text','raw_word_counts'])
    return parser_df