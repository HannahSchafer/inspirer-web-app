"""Helper Functions"""

from datetime import datetime
from train_classifier import unique_training_words

def get_timestamp():
    """Get current timestamp."""

    current_time = datetime.now()
    return current_time.strftime('%Y-%m-%d %H:%M:%S')



def extract_features(tweet):
    tweet_words = set(tweet)
    features = {}
    for word in unique_training_words :
        features['contains(%s)' % word] = (word in tweet_words)
    return features

