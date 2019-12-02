import json
import pandas as pd
import nltk 
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment(data_json):
  sentiment_json = {}
  sid = SentimentIntensityAnalyzer()
  for e in range(len(new_df)):
    sentiment_json[new_df['userName'][e]] = [y for x,y in sid.polarity_scores(new_df['text'][e]).items() if y != 0.0]    
  return sentiment_json
