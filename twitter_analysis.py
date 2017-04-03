
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
print user.screen_name
print user.followers_count


# getting user tweets, parameters: screen_name, # tweets, include re-tweets (T/F)
user_tweets = api.user_timeline(screen_name = 'chrissyteigen', count = 10, include_rts = True)

for status in user_tweets:
    print(status.text)


# logic to import user's tweets - if tweet is from last 24 hours, only use that one tweet,
#otherwise take last 5 tweets and take average of the sentiment. 

# run their tweet(s) through classifier

# based on classifier's output (1 or 2), query database for quotes matching that output, and where user_id 
# has not had that quote. 

# from those quotes, randomly select a quote. Send quote to browser, and update database that user was given that quote_id

