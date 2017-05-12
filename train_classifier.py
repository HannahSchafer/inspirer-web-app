# """Part 1: Building my Classifier"""

from model import Classifier, connect_to_db, db
import nltk
from nltk.corpus import stopwords
import pickle
from flask import Flask

# Reference Laurent Luce (see references.txt)
def get_words_in_tweets(tweets):
    """Append all words from tweets to a single list."""

    all_words = []
    for (words, sentiment) in tweets:
        all_words.extend(words)
    return all_words


def get_features(wordlist):
    """Get keys of dictionary, where key is the word, and value is the # of 
       times found in all tweets"""

    wordlist = nltk.FreqDist(wordlist)

    unique_training_words = wordlist.keys()
    return unique_training_words 


def extract_features(tweet):
    """Takes in a tweet, returns a dictionary indicating whether words from the 
    new tweet are contained in the training tweets."""

    tweet_words = set(tweet)
    features = {}
    for word in unique_training_words :
        features['contains(%s)' % word] = (word in tweet_words)
    return features


def train_classifier():
    """Trains the classifier with the supervised trained data set of tweets."""

    # create an irrelevant app instance, to connect with db, as required by flask_sqlalchemy
    app = Flask(__name__)
    connect_to_db(app)

    #Query my training tweets (as a list) from the classifier table in db
    train_tweets = (db.session.query(Classifier.tweet_content, 
                                     Classifier.sentiment_id)
                              .filter(Classifier.test_or_train=='train')
                              .all())

    # defining stop_words to remove from corpus
    stop_words = set(stopwords.words('english'))


    # normalizing words in tweets through .lower(), exclusing all meaningless words via stop_words. 
    # word_tokenizing sentences, to split all meaningful text. Better than .split() method. 
    # appending all itemized/split tweets to a single list along with their sentiment 
    tweets = []
    for sentence, sentiment in train_tweets:
        words_filtered = [word.lower() for word in nltk.word_tokenize(sentence) 
                                       if word not in stop_words] 
        tweets.append((words_filtered, sentiment))

    # calls get_features function on get_words_in_tweets, which takes tweets as
    # an argument. Returns keys of the features dictionary: all the UNIQUE words 
    unique_training_words = get_features(get_words_in_tweets(tweets))

    # using apply_features method from NLTK
    training_tweets = nltk.classify.apply_features(extract_features, tweets)


    # feeding the Naive Bayes Classifier my training set, and storing in variable 'classifier'
    classifier = nltk.NaiveBayesClassifier.train(training_tweets)


    classifier.unique_training_words = unique_training_words
    # This is what will run a new tweet through the trained classifier 

    # saving trained classifier part 1:
    # trained classifier will be saved to the naivebayes.pickle file. 
    # wb = write in bytes
    save_classifier = open("naivebayes.pickle", "wb")

    # dump the trained classifier. 'save_classifier' is where we are dumping it.
    pickle.dump(classifier, save_classifier)
    save_classifier.close()



# part 2 to saving the trained classifier. 
classifier_f = open("naivebayes.pickle", "rb")
classifier = pickle.load(classifier_f)
unique_training_words = classifier.unique_training_words
classifier_f.close()







