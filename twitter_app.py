# encoding: utf-8
import tweepy
import numpy as np
import re
from unidecode import unidecode
from textblob import TextBlob
import json


def clean_tweet(tweet):
    if type(tweet) == np.cfloat:
        return ""
    temp = tweet.lower()
    temp = re.sub("'", "", temp)  # to avoid removing contractions in english
    temp = re.sub("@[A-Za-z0-9_]+", "", temp)
    temp = re.sub("#[A-Za-z0-9_]+", "", temp)
    temp = re.sub(r'http\S+', '', temp)
    temp = re.sub('[()!?]', ' ', temp)
    temp = re.sub('\[.*?\]', ' ', temp)
    temp = re.sub("[^a-z0-9]", " ", temp)
    temp = temp.split()
    temp = [w for w in temp if not w in stopwords]
    temp = " ".join(word for word in temp)
    return temp


stopwords = ["for", "on", "an", "a", "of", "and", "in", "the", "to", "from", "rt"]
client = tweepy.Client(
    bearer_token='your key',
    consumer_key='your key',
    consumer_secret='your secret',
    access_token='your key',
    access_token_secret='your secret')

data = []
lst_lang = ['am', 'ar', 'bg', 'bn', 'bo', 'ca', 'ckb', 'cs', 'cy', 'da', 'de', ' dv', ' el', ' en', ' es', 'et', 'eu',
            'fa', 'fi', 'fr', 'gu', 'he', 'hi', 'ht', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'ka', 'km', 'kn', 'ko', 'lo',
            'lt', 'lv', 'ml', 'mr', 'my', 'ne', 'nl', 'no', 'or', 'pa', 'pl', 'ps', 'pt', 'qam', 'qct', 'qht', 'qme',
            'qst', 'ro', 'ru', 'sd', 'si', 'sl', 'sr', 'sv', 'ta', 'te', 'th', 'tl', 'tr', 'ug', 'uk', 'und', 'ur',
            'vi', 'zh', 'zxx']
with open(r"C:\Users\ste-v\Desktop\twitter_data.json", "a", encoding="utf-8") as f:
    for lang in lst_lang:
        query = 'worldcup lang:' + lang
        tweets = client.search_recent_tweets(query=query, max_results=100)
        print(len(tweets))
        if len(tweets) > 0:
            for tweet in tweets.data:
                text = TextBlob(clean_tweet(unidecode(tweet.text)))
                txt = text.string
                polarity = text.sentiment.polarity
                if polarity > 0.1:
                    tweet = {
                        "id": tweet.id,
                        "text": txt,
                        "language": lang,
                        "polarity": 'Positive'
                    }
                    data.append(tweet)
                elif polarity == 0:
                    tweet = {
                        "id": tweet.id,
                        "text": txt,
                        "language": lang,
                        "polarity": 'Neutral'
                    }
                    data.append(tweet)
                else:
                    tweet = {
                        "id": tweet.id,
                        "text": txt,
                        "language": lang,
                        "polarity": 'Negative'
                    }
                    data.append(tweet)
    json.dump(data, f)
