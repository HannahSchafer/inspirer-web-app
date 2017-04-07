"""Models for Inspirer project"""
## refactor near end of project to put each class in own file within a folder called Models = best practice - make note of this

# requires a flask app to connect to my db
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

##############################################################################
# Model definitions

class User(db.Model):
    """User of Inspirer web app."""

    __tablename__ = "users"

    def __repr__ (self):
        """Represents Users class objects."""

        return "<Meet the user: user_id={}, name={}, password={}, twitter_handle={},\
                email={}, phone={}>".format(self.user_id, self.user_name, self.password, self.twitter_handle, self.email, self.phone)

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_name = db.Column(db.Unicode(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    twitter_handle = db.Column(db.Unicode(50), nullable=False)
    email = db.Column(db.Unicode(50), nullable=False)
    phone = db.Column(db.String, nullable=True)

    quotes = db.relationship("Quote", secondary="analyses", backref="user")


class Quote(db.Model):
    """Quotes information."""

    __tablename__ = "quotes"

    def __repr__ (self):
        """Represents Quotes class objects."""

        return "<Quotes information: quote_id={}, content={}, img_url={}, author={},\
                sentiment_id={}>".format(self.quote_id, self.content, self.img_url, self.author, self.sentiment_id)

    quote_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    content = db.Column(db.UnicodeText, nullable=True)
    img_url = db.Column(db.UnicodeText, nullable=True)
    author = db.Column(db.Unicode(50), nullable=True)
    sentiment_id = db.Column(db.Integer, db.ForeignKey('sentiments.sentiment_id'), nullable=False)


    sentiment = db.relationship("Sentiment", backref=db.backref("quotes"))


class Analyses(db.Model):
    """Information about the analyses (when user clicks button to start program)."""

    __tablename__ = "analyses"

    def __repr__ (self):
        """Represents Analyses class objects."""

        return "<Analyses information: analyses_id={}, user_id={}, timestamp={}, \
                tweet_sent_id={}, quote_id={}>".format(self.analyses_id, self.user_id, self.timestamp, self.tweet_sent_id, self.quote_id)

    analyses_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    tweet_sent_id = db.Column(db.Integer, db.ForeignKey('sentiments.sentiment_id'), nullable=False)
    quote_id = db.Column(db.Integer, db.ForeignKey('quotes.quote_id'), nullable=False)


    user = db.relationship("User", backref=db.backref("analyses"))
    sentiment = db.relationship("Sentiment") #I have a particular analysis. Give me the sentiment object.
    quote = db.relationship("Quote") #I am on an analysis, give me a quote object. 


class Sentiment(db.Model):
    """Information about the sentiments"""

    __tablename__ = "sentiments"

    def __repr__ (self):
        """Represents Sentiments class objects."""

        return "<Sentiments information: sentiment_id={}, sentiment={}>".format(self.sentiment_id, self.sentiment)

    sentiment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sentiment = db.Column(db.String(15), nullable=False)



class Classifier(db.Model):
    """Information about the sentiments"""

    __tablename__ = "classifier"

    def __repr__ (self):
        """Represents Classifier class objects."""

        return "<Classifier information: classifier_id={}, tweet_content={}, test_or_train={}, sentiment_id={}>".format(self.classifier_id, self.tweet_content, self.test_or_train, self.sentiment_id)

    classifier_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    tweet_content = db.Column(db.Unicode(300), nullable=False)
    test_or_train = db.Column(db.String(10), nullable=False)
    sentiment_id = db.Column(db.Integer, db.ForeignKey('sentiments.sentiment_id'), nullable=False)


    sentiment = db.relationship("Sentiment") #I'm on classifier, give me the sentiment



def example_data():
    """Creating some sample data for fake_db in tests.py."""

    pos = Sentiment(sentiment='pos')
    neg = Sentiment(sentiment='neg')

    favinn = User(user_name='Favinn', password='clown eyes', twitter_handle='NuBaby', email="Favinn@gmail.com", phone='555-444-9999')
    aimee = User(user_name='Aimee', password='art', twitter_handle='Artist', email="Aimee@gmail.com", phone='555-555-9999')
    charlotte = User(user_name='Charlotte', password='house', twitter_handle='RedHead', email="Charlotte@gmail.com", phone='333-555-9999')

    positive_quote = Quote(content='I am a positive quote!', img_url='static/positivequote.jpg', author='me', sentiment_id='1')
    negative_quote = Quote(content='I am a negative quote!', img_url='static/negativequote.jpg', author='you', sentiment_id='2')

    db.session.add_all([pos, neg, favinn, aimee, charlotte, positive_quote, negative_quote])
    db.session.commit()



  


################################################################################


def connect_to_db(app, database_uri='postgresql:///sentiment_analysis'):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    from server import app
    
    connect_to_db(app)
    print "Connected to DB."

    db.create_all() 



