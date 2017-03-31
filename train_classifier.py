# """Part 1: Building my Classifier"""

from model import Classifier, connect_to_db, db
from server import app 
import nltk
import random # to shuffle data set we have
from nltk.corpus import stopwords

connect_to_db(app)
#app lives in server
# connect to db lives model
#db lives in model


#Query my training tweets (as a list) from the classifier table in db
train_tweets = db.session.query(Classifier.tweet_content, Classifier.sentiment_id).filter(Classifier.test_or_train=='train').all()

# defining stop_words to remove from corpus
stop_words = set(stopwords.words('english'))


# Reference Laurent Luce (http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)
tweets= []
for sentence, sentiment in train_tweets:
    words_filtered = [word.lower() for word in sentence.split() if word not in stop_words]
    tweets.append((words_filtered, sentiment))



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

