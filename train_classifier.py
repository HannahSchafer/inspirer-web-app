"""Part 1: Building my Classifier"""

import nltk
import random # to shuffle data set we have
from nltk.corpus import movie_reviews
# from nltk.probablity import FreqDist
# from ntlk.classify.util import apply_features.accuracy

# making tuples. in each tuple is a list of words (which are features), and then the sentiment. this will be part of our bag of words
documents = [(movie_reviews.words(fileid), category) 
            for category in movie_reviews.categories() 
            for fileid in movie_reviews.fileids(category)] 

random.shuffle(documents)

print documents[1]


#then take all words in bag, then find most popular words. then of those most
#popular words, which appear in positive texts, and which in negative texts

all_word = []


#Query my training tweets from the classifier table in db

#Pull out features from training tweets

#Feed training set to my Naive Bayes Classifier

#Use test tweets to test the classifier

#import the classifier in the server for /inspire-process route

"""
Notes from tutorial:
2 categories, tagged: positive or negative. spam or not spam. (inbox or spam)
-document with some words, labeled with one of 2 labels. - this wil work
-
1.) import nltk
2.) import random
3.) from nltk.corpus import movie_reviews- 1000 pos/1000neg (I will import my tweet)


"""