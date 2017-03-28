"""Utility file to seed Sentiment_Analysis database"""

from datetime import datetime
from sqlalchemy import func
from model import User
from model import Quote
from model import Analyses
from model import Sentiment
from model import Classifier

from model import connect_to_db, db
from server import app #####???


def load_users(): ### do I need this? No users initially?
    """Load users into database."""

    # Delete all rows in table, so if we need to run this a second time,
    # we won't be trying to add duplicate users
    User.query.delete()

    # Read users file and insert data
    for row in open(""):


        user = User(user_id=user_id, user_name=user_name, password=password, twitter_handle=twitter_handle, email=email, phone=phone)

        # Adding data to the session
        db.session.add(user)

    # Commiting data to database
    db.session.commit()


def load_quotes():
    """Load quote information into database."""

    Quote.query.delete()

    for row in open(""):


        quote = Quote(quote_id=quote_id, content=content, img_url=img_url, author=author, sentiment_id=sentiment_id)


        # Adding data to the session
        db.session.add(quote)

    # Commiting data to database
    db.session.commit()



def load_sentiments(): ## do i need this?
    """Load sentiments into database."""##

    Sentiment.query.delete()

    for row in open(""):

        sentiment = Sentiment(sentiment_id=sentiment_id, sentiment=sentiment)

        # Adding data to the session
        db.session.add(sentiment)

    # Commiting data to database
    db.session.commit()



def load_classifier():
    """Load classifier info into database."""

    Classifier.query.delete()

    for row in open(""):

        classifier = Classifier(classifier_id=classifier_id, tweet_content=tweet_content, test_or_train=test_or_train, sentiment_id=sentiment_id)


        # Adding data to the session
        db.session.add(classifier)

    # Commiting data to database
    db.session.commit()




def set_val_user_id():
    """Set value for the next user_id after seeding database"""

    # Get the Max user_id in the database
    result = db.session.query(func.max(User.user_id)).one()
    max_id = int(result[0])

    # Set the value for the next user_id to be max_id + 1
    query = "SELECT setval('users_user_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


def set_val_quote_id():
    """Set value for the next quote_id after seeding database"""

    # Get the Max quote_id in the database
    result = db.session.query(func.max(Quote.quote_id)).one()
    max_id = int(result[0])

    # Set the value for the next quote_id to be max_id + 1
    query = "SELECT setval('quotes_quote_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


def set_val_analyses_id(): ## Do I need this? Nothing to load. 
    """Set value for the next analyses_id after seeding database"""##

    # Get the Max analyses_id in the database
    result = db.session.query(func.max(Analyses.analyses_id)).one()
    max_id = int(result[0])

    # Set the value for the next quote_id to be max_id + 1
    query = "SELECT setval('analyses_analyses_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()


def set_val_sentiment_id():
    """Set value for the next sentiment_id after seeding database"""

    # Get the Max sentiment_id in the database
    result = db.session.query(func.max(Sentiment.sentiment_id)).one()
    max_id = int(result[0])

    # Set the value for the next sentiment_id to be max_id + 1
    query = "SELECT setval('sentiments_sentiment_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()



def set_val_classifier_id():
    """Set value for the next classifier_id after seeding database"""

    # Get the Max classifier_id in the database
    result = db.session.query(func.max(Classifier.classifier_id)).one()
    max_id = int(result[0])

    # Set the value for the next sentiment_id to be max_id + 1
    query = "SELECT setval('classifier_classifier_id_seq', :new_id)"
    db.session.execute(query, {'new_id': max_id + 1})
    db.session.commit()



if __name__ == "__main__":
    connect_to_db(app)

    # In case tables haven't been created, create them
    db.create_all()

    # Import different types of data
    load_users()
    load_quotes()
    load_analyses()
    load_sentiments()
    load_classifier()
    set_val_user_id()
    set_val_quote_id()
    set_val_analyses_id()
    set_val_sentiment_id()
    set_val_classifier_id()




