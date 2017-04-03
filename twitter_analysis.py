
from __future__ import unicode_literals
from model import connect_to_db, db
from server import app 
import nltk
from nltk.corpus import stopwords
import pickle
from train_classifier import extract_features
import twitter
import tweepy
import os
from datetime import datetime, timedelta
connect_to_db(app)

classifier = pickle.load(open("naivebayes.pickle"))


# Run new tweet(s) through trained classifier
# tweet = "I love python-twitter!"
# print classifier.classify(extract_features(nltk.word_tokenize(tweet)))


# connect to Twitter API! eeks! YCDI!

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
# >>> 2017-04-02 20:06:44


# getting user tweets, parameters: screen_name, # tweets, include re-tweets (T/F)
# Reference: https://www.quora.com/How-can-I-retrieve-from-given-users-home_timeline-with-Tweepy
user_tweets = api.user_timeline(screen_name = 'chrissyteigen', include_rts = True, count=5)
for status in user_tweets:
    if status.created_at > last24Hours:
        print status.text
        print status.created_at
    else:
        print status.text
# >>> 2017-03-29 17:54:43




# logic to import user's tweets - if tweet is from last 24 hours, only use that one tweet,
#otherwise take last 5 tweets and take average of the sentiment. 

# run their tweet(s) through classifier

# based on classifier's output (1 or 2), query database for quotes matching that output, and where user_id 
# has not had that quote. 

# from those quotes, randomly select a quote. Send quote to browser, and update database that user was given that quote_id

