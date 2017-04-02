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

#appending all words to a single list
def get_words_in_tweets(tweets):
    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words

# getting keys of dictionary, where key is the word, and value is the # of times found in all tweets
def get_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    # print wordlist['friend']
    word_features = wordlist.keys()
    return word_features

# extract_features takes an input, and it returns a dictionary, where the key is
# the 'contain's + word in trained feature set' and the value is True/False
# depending on whether the input tweet matches that word in the trained feature set
def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in tweet_words)
    return features



#Query my training tweets (as a list) from the classifier table in db
train_tweets = db.session.query(Classifier.tweet_content, \
               Classifier.sentiment_id).filter(Classifier.test_or_train=='train').all()

# defining stop_words to remove from corpus
stop_words = set(stopwords.words('english'))


# Reference Laurent Luce (http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/)

# normalizing words in tweets through .lower(), exclusing all meaningless words via stop_words. 
# word_tokenizing sentences, to split all meaningful text. Better than .split() method. 
#appending all itemized/split tweets to a single list along with their sentiment 
tweets = []
for sentence, sentiment in train_tweets:
    words_filtered = [word.lower() for word in nltk.word_tokenize(sentence) if \
    word not in stop_words] 
    tweets.append((words_filtered, sentiment))

# calls get_features function on function: get_words_in_tweets, which takes the tweets as
# an argument. This returns the keys of the features dictionary, which are all the UNIQUE words that
# contain meaning 
word_features = get_features(get_words_in_tweets(tweets))


# using apply_features method 
training_tweets = nltk.classify.apply_features(extract_features, tweets)


# feeding the Naive Bayes Classifier my training set, and storing in variable 'classifier'
classifier = nltk.NaiveBayesClassifier.train(training_tweets)

print classifier.show_most_informative_features(150)

# This is what will run a new tweet through the trained classifier 
# Must give it a tweet as argument
# print classifier.classify(extract_features(nltk.word_tokenize(tweet)))












