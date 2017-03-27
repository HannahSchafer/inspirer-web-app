"""Models for Inspirer project"""

from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

##############################################################################
# Model definitions

class User(db.Model)
    """User of Inspirer web app."""

    __tablename__ = "users"

    def __repr__ (self):
        """Represents Users class objects."""

        return "<Meet the user: user_id={}, name={}, password={}, twitter_handle={},\
                email={}, phone={}>".format(self.user_id, self.user_name, self.password, self.twitter_handle, self.email, self.phone)

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    twitter_handle = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.Integer, nullable=False)


class Quote(db.Model)
    """Quotes information."""

    __tablename__ = "quotes"

    def __repr__ (self):
        """Represents Quotes class objects."""

        return "<Quotes information: quote_id={}, content={}, img_url={}, author={},\
                sentiment_id={}>".format(self.quote_id, self.content, self.img_url, self.author, self.sentiment_id)

    quote_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.String, nullable=True)
    img_url = db.Column(db.String, nullable=True)
    author = db.Column(db.String(50), nullable=True)
    sentiment_id = db.Column(db.Integer, db.ForeignKey('sentiments.sentiment_id'), nullable=False)


    q_sentiments = db.relationship("Sentiment", backref=db.backref("quotes"))


class Analyses(db.Model)
    """Information about the analyses (when user clicks button to start program)."""

    __tablename__ = "analyses"

    def __repr__ (self):
    """Represents Analyses class objects."""

        return "<Analyses information: analyses_id={}, user_id={}, timestamp={}, \
                tweet_sent_id={}, quote_id={}>".format(self.analyses_id, self.user_id, self.timestamp, self.tweet_sent_id, self.quote_id)

    analyses_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    tweet_sent_id = db.Column(db.String, db.ForeignKey('sentiments.sentiment_id'), nullable=False)
    quote_id = db.Column(db.Integer, db.ForeignKey('quotes.quote_id'), nullable=False)


    users = db.relationship("User", backref=db.backref("analyses"))
    a_sentiments = db.relationship("Sentiment", backref=db.backref("analyses"))
    quotes = db.relationship("Quote", backref=db.backref("analyses"))


class Sentiment(db.Model)
    """Information about the sentiments"""

    __tablename__ = "sentiments"

    def __repr__ (self):
    """Represents Sentiments class objects."""

        return "<Sentiments information: sentiment_id={}, sentiment={}>".format(self.sentiment_id, self.sentiment)

    sentiment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sentiment = db.Column(db.String(15), nullable=False)



class Classifier(db.Model)
    """Information about the sentiments"""

    __tablename__ = "classifier"

    def __repr__ (self):
    """Represents Classifier class objects."""

        return "<Classifier information: classifier_id={}, tweet_content={}, test_or_train={}, sentiment_id={}>".format(self.classifier_id, self.tweet_content, self.test_or_train, self.sentiment_id)

    classifier_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tweet_content = db.Column(db.String(150), nullable=False)
    test_or_train = db.Column(db.String(10), nullable=False)
    sentiment_id = db.Column(db.Integer, db.ForeignKey('sentiments.sentiment_id'), nullable=False)


    c_sentiments = db.relationship("Sentiment", backref=db.backref("classifier"))

################################################################################

def init_app():
    # So that we can use Flask-SQLAlchemy, we'll make a Flask app.
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///ratings'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":

    from server import app
    from flask import Flask

    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."

    db.create_all() 



