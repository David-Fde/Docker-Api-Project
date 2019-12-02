import json
import pandas as pd
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def sentiment(data_json):
    sentiment_json = {}
    sid = SentimentIntensityAnalyzer() 
    new_df = pd.DataFrame(eval(data_json))
    
    for e in range(len(new_df)):
        sentiment_json[new_df['userName'][e]] = sid.polarity_scores(new_df['text'][e])
    return sentiment_json
