# """Part 1: Building my Classifier"""

from model import Classifier, connect_to_db, db
from server import app 
import nltk
import random # to shuffle data set we have
from nltk.corpus import movie_reviews

connect_to_db(app)
#app lives in server
# connect to db lives model
#db lives in model


#Query my training tweets (as a list) from the classifier table in db
train_tweets_u = db.session.query(Classifier.tweet_content, Classifier.sentiment_id).filter(Classifier.test_or_train=='train').all()


for tweet in train_tweets_u:
    token_tuples = (nltk.word_tokenize(tweet[0]), tweet[1])


# neg_train_tweets = db.session.query(Classifier.tweet_content).filter(Classifier.test_or_train=='train', Classifier.sentiment_id==2).all()


# """

# # # making tuples. in each tuple is a list of words (which are features), and then the sentiment. this will be part of our bag of words
# # documents = [(movie_reviews.words(fileid), category) 
# #             for category in movie_reviews.categories() 
# #             for fileid in movie_reviews.fileids(category)] 

# # random.shuffle(documents)

# # # print documents[1]


# # #then take all words in bag, then find most popular words. then of those most
# # #popular words, which appear in positive texts, and which in negative texts

# # all_words = []
# # for w in movie_reviews.words():
# #     all_words.append(w.lower()) #normalize all words by making lowercase

# # # find most common words
# # all_words = nltk.FreqDist(all_words)
# # print (all_words.most_common(15))
# # print all_words["stupid"]

# """

