import json
import pandas as pd
import requests
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as distance
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import numpy as np


def sentiment(data_json):
    sentiment_json = {}
    sid = SentimentIntensityAnalyzer() 
    new_df = pd.DataFrame(eval(data_json))
    
    for e in range(len(new_df)):
        sentiment_json[new_df['userName'][e]] = sid.polarity_scores(new_df['text'][e])
    return sentiment_json

def tokenization(text):
    tokens = nltk.word_tokenize(text)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text)
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))
    tokens_clean = [e for e in tokens if e not in stop_words]
    return tokens_clean

users = {'Danny Torrance' : [],
 'Danny Torrances Finger': [],
 'Ellen Ripley': [],
 'J. Jonah Jameson':[],
 'John Wick':[],
 'Leia Organa':[],
 'Mike Wazowski':[],
 'Tony Stark':[]}

def recommendation(user_id,all_json):
    users_dict=dict()
    for i in range(len(all_json)):
        if all_json[i]['userName'] not in users_dict:
            users_dict[all_json[i]['userName']]=all_json[i]['text']
        else:
            users_dict[all_json[i]['userName']]+=' ' +all_json[i]['text']
    count_vectorizer = CountVectorizer()
    sparse_matrix = count_vectorizer.fit_transform(users_dict.values())
    sparse_matrix
    doc_term_matrix = sparse_matrix.todense()
    df = pd.DataFrame(doc_term_matrix, 
                  columns=count_vectorizer.get_feature_names(), 
                  index=users_dict.keys())
    similarity_matrix = distance(df, df)
    sim_df = pd.DataFrame(similarity_matrix, columns=users_dict.keys(), index=users_dict.keys())
    np.fill_diagonal(sim_df.values, 0) 
    return sim_df.idxmax()