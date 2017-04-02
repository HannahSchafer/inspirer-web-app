
from model import connect_to_db, db
from server import app 
import nltk
from nltk.corpus import stopwords
import pickle
from train_classifier import extract_features
connect_to_db(app)

classifier = pickle.load(open("naivebayes.pickle"))


tweet = "I love python-twitter!"

print classifier.classify(extract_features(nltk.word_tokenize(tweet)))