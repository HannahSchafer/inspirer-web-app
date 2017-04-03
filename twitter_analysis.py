
from __future__ import unicode_literals
from model import connect_to_db, db, Quote, Sentiment
from server import app 
import nltk
from nltk.corpus import stopwords
import pickle
from train_classifier import extract_features
import twitter
import tweepy
import os
from datetime import datetime, timedelta
from random import choice

connect_to_db(app)


# load trained classifier from pickle file
classifier = pickle.load(open("naivebayes.pickle"))

# connect to Twitter API
consumer_key=os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"]
access_token_key=os.environ["TWITTER_ACCESS_TOKEN_KEY"]
access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"]


#using tweepy library to authenticate with OAuth
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

api = tweepy.API(auth)

user = api.get_user('chrissyteigen')
# print user.screen_name
# print user.followers_count

# reference: http://stackoverflow.com/questions/7582333/python-get-datetime-of-last-hour
last24Hours = datetime.now() - timedelta(hours = 24)
# print last24Hours.strftime('%Y-%m-%d %H:%M:%S')

# get user tweets, parameters: screen_name, # tweets, include re-tweets (T/F)
# Reference: https://www.quora.com/How-can-I-retrieve-from-given-users-home_timeline-with-Tweepy
user_tweets = api.user_timeline(screen_name = 'YaraShahidi', include_rts = True, count=5)

fresh_tweets = []
day_old_tweets = []
current_sentiments = []

# getting most current tweets, or last 5 tweets user posted if not in last 24hrs
for status in user_tweets:
    if status.created_at > last24Hours:
        fresh_tweets.append(status.text)
    else:
        day_old_tweets.append(status.text)

# running tweet(s) through the trained classifier
if len(fresh_tweets) > 0:
    for tweet in fresh_tweets:
        sentiment = classifier.classify(extract_features(nltk.word_tokenize(tweet)))
        current_sentiments.append(sentiment)
        
else:
    for tweet in day_old_tweets:
        sentiment = classifier.classify(extract_features(nltk.word_tokenize(tweet)))
        current_sentiments.append(sentiment)
    
avg_sentiment = sum(current_sentiments) / len(current_sentiments)


if int(round(avg_sentiment)) == 1:
    pos_quotes = db.session.query(Quote.content).filter(Quote.sentiment_id=='1').all()
    print choice(pos_quotes)
else:
    neg_quotes = db.session.query(Quote.content).filter(Quote.sentiment_id=='2').all()
    print choice(neg_quotes)





# based on classifier's output (1 or 2), query database for quotes matching that output, and where user_id 
# has not had that quote. 

# from those quotes, randomly select a quote. Send quote to browser, and update database that user was given that quote_id

