
from __future__ import unicode_literals
from model import connect_to_db, db, Quote, Sentiment, User, Analyses
import nltk
from nltk.corpus import stopwords
import pickle
from train_classifier import extract_features
import twitter
import tweepy
import os
from datetime import datetime, timedelta
from flask import Flask
from random import choice

app = Flask(__name__)
connect_to_db(app)

def load_classifier():
    """Load pickle file with trained classifier."""

    # load trained classifier from pickle file
    classifier = pickle.load(open("naivebayes.pickle"))
    return classifier

# twitter service connection is an object - so make an object
# put stuff below into __init__
# test of this will be another class??

def connect_twitter_api(twitter_handle):
    """Connect to Twitter API and authenticate."""
    # connect to Twitter API
    consumer_key=os.environ["TWITTER_CONSUMER_KEY"]
    consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"]
    access_token_key=os.environ["TWITTER_ACCESS_TOKEN_KEY"]
    access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

    #using tweepy library to authenticate with OAuth
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    # get user tweets, parameters: screen_name, # tweets, include re-tweets (T/F)
    # Reference: https://www.quora.com/How-can-I-retrieve-from-given-users-home_timeline-with-Tweepy
    user_tweets = api.user_timeline(screen_name = twitter_handle, include_rts = True, count=5)
    return user_tweets



def get_user_sentiment(user_tweets, classifier):
    """Returns user's average sentiment."""

    # reference: http://stackoverflow.com/questions/7582333/python-get-datetime-of-last-hour
    last24Hours = datetime.now() - timedelta(hours = 24)
    # print last24Hours.strftime('%Y-%m-%d %H:%M:%S')



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
    return avg_sentiment


def get_quote(twitter_handle, user_id):
    """Randomly selecting pos/neg quote from db, based on user's avg sentiment"""

    classifier = load_classifier()
    user_tweets = connect_twitter_api(twitter_handle)
    avg_sentiment = get_user_sentiment(user_tweets, classifier)


    old_pos_quotes = db.session.query(Analyses.quote_id).filter(Analyses.user_id==user_id, Analyses.tweet_sent_id==1).all()
    old_neg_quotes = db.session.query(Analyses.quote_id).filter(Analyses.user_id==user_id, Analyses.tweet_sent_id==2).all()
    

    if int(round(avg_sentiment)) == 1:
        all_pos_quotes_info = db.session.query(Quote.content, Quote.quote_id, Quote.sentiment_id).filter(Quote.sentiment_id=='1', Quote.quote_id.notin_(old_pos_quotes)).all()
        if len(old_pos_quotes) < len(all_pos_quotes_info):
            pos_quote_info = choice(all_pos_quotes_info)
            return pos_quote_info
        else:
            return ["We're writing more poems and quotes. Check in later!"]
    else:
        all_neg_quotes_info = db.session.query(Quote.content, Quote.quote_id, Quote.sentiment_id).filter(Quote.sentiment_id=='2', Quote.quote_id.notin_(old_neg_quotes)).all()
        if len(old_neg_quotes) < len(all_neg_quotes_info):
            neg_quote_info = choice(all_neg_quotes_info)
            return neg_quote_info
        else:
            return ["We're writing more poems and quotes. Check in later!"]








