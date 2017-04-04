"""Utility file to seed Sentiment_Analysis database"""

import csv
from datetime import datetime
from sqlalchemy import func
from model import User
from model import Quote
from model import Analyses
from model import Sentiment
from model import Classifier

from model import connect_to_db, db
from server import app #####???


def load_sentiments(): # load sentiments first because other tables depend on this data
    """Load sentiments into database."""

    sentiment1 = 'pos'
    sentiment2 = 'neg'
      
    #create instances of Sentiment class and pass table columns the data.   
    pos = Sentiment(sentiment=sentiment1)
    neg = Sentiment(sentiment=sentiment2) 

#         # Adding data to the session
    db.session.add(pos)
    db.session.add(neg)

#     # Commiting data to database
    db.session.commit()


def load_classifier():
    """Load classifier info into database."""


    data_file = open('seed_data/classifier.csv', 'rU')
    csv_file = csv.reader(data_file)

    for row in csv_file:
        tweet_content=row[0]
        test_or_train=row[1]
        sentiment_id=row[2]

        classifier = Classifier(tweet_content=tweet_content, test_or_train=test_or_train, sentiment_id=sentiment_id)


        # Adding data to the session
        db.session.add(classifier)

    # Commiting data to database
    db.session.commit()



def load_quotes():
    """Load quote information into database."""

    data_file = open('seed_data/quotes.csv', 'rU')
    csv_file = csv.reader(data_file)

    for row in csv_file:
        content = row[0]
        img_url = row[1]
        author = row[2]
        sentiment_id = row[3]
        

        quote = Quote(content=content, img_url=img_url, author=author, sentiment_id=sentiment_id)


        # Adding data to the session
        db.session.add(quote)

    # Commiting data to database
    db.session.commit()



def load_users(): ### do I need this? No users initially?
    """Load users into database."""

    # Read users file and insert data
    for text in open("seed_data/users.csv"):
        persons = text.split("\r")
    for person in persons:  
        item = person.split(",")
        user_name = item[0]
        password = item[1]
        twitter_handle = item[2]
        email = item[3]
        phone = item[4]

        user = User(user_name=user_name, password=password, twitter_handle=twitter_handle, email=email, phone=phone)

        # Adding data to the session
        db.session.add(user)

    # Commiting data to database
    db.session.commit()



def load_analyses(): # no real analyses, since don't have users who have used web app, but adding one record for testing
    """Load analyses into database."""

    # Read users file and insert data
    data_file = open('seed_data/analyses.csv', 'rU')
    csv_file = csv.reader(data_file)

    for row in csv_file:
        user_id = row[0]
        timestamp = row[1]
        tweet_sent_id = row[2]
        quote_id = row[3]


        analysis = Analyses(user_id=user_id, timestamp=timestamp, tweet_sent_id=tweet_sent_id, quote_id=quote_id)

        # Adding data to the session
        db.session.add(analysis)

    # Commiting data to database
    db.session.commit()


# def delete_all_ordered():
#     """Delete all rows in tables, so if we need to run this a second time,
#       we won't be trying to add duplicate users"""

#     Classifier.query.delete()
#     Analyses.query.delete()
#     User.query.delete()
#     Quote.query.delete()
#     Sentiment.query.delete()

#     # Commiting deletions to database
#     db.session.commit()


if __name__ == "__main__":
    connect_to_db(app)


#     # Delete any past info in tables to reload cleanly
#     delete_all_ordered()

#     # In case tables haven't been created, create them
#     db.create_all()

#     # Import different types of data
#     load_sentiments()
#     load_quotes()
#     load_users()
#     load_analyses()
#     load_classifier()
    





