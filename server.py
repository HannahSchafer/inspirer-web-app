# encoding=utf8  
"""The Inspirer flask app server file."""


# python modules/ standard libraries, then jinja, flask, and then my code
from datetime import datetime, time, date
from jinja2 import StrictUndefined
from flask import (Flask, jsonify, render_template, redirect, request,
                    flash, session)
from flask_debugtoolbar import DebugToolbarExtension
import re

from model import connect_to_db, db, User, Quote, Analyses, Sentiment, Classifier
from helper_functions import get_timestamp
from twitter_analysis import (get_quote, get_average_sentiment, get_user_sentiment, 
                              connect_twitter_api, load_classifier)
from send_sms import send_message



app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "782387409lhjsbdys762984sdliclu6"

# Jinja2 should fail loudly, so I can hear it.
app.jinja_env.undefined = StrictUndefined




@app.route('/')
def splashpage():
    """Homepage."""

    return render_template("homepage.html")


@app.route('/register')
def show_registration():
    """Show registration form."""

    return render_template("reg_form.html")


@app.route('/process-registration', methods=['POST'])
def process_registration():
    """Check the given twitter_handle and password against the database."""

    twitter_handle= request.form.get("twitter_handle")
    given_password = request.form.get("password")
    phone = request.form.get("phone")
    email = request.form.get("email")
    name = request.form.get("user_name")
    
    # phone_re =  


    existing_user = (User.query.filter((User.twitter_handle==twitter_handle) & 
                                       (User.password==given_password)).first())

    if existing_user:
        flash("Welcome back! You already have an account. Please log in with your twitter handle and password.")
        return redirect("/")

    else:
        # class object 'new user'
        new_user = (User(user_name=name, email=email, twitter_handle=twitter_handle, 
                        password=given_password, phone=phone))
        

        # Add new_user to the database session so it can be stored
        db.session.add(new_user)

        # Commiting to the database
        db.session.commit()

        # flash message for the user
        flash(u"Welcome to Sparrö!")

        # after commited to db, now new_user has a user_id
        user_id = new_user.user_id

        # User is now in a session
        session["twitter_handle"] = twitter_handle
        session["user_id"] = user_id
        session["user_name"] = name


        return redirect("/inspire")



@app.route("/login-validation")
def check_login():
    """Compares login info to db info."""

    twitter_handle = request.args.get("twitter_handle")
    password = request.args.get("password")

    valid_user = User.query.filter((User.twitter_handle==twitter_handle) & 
                 (User.password==password)).first()

    if valid_user:
        session["twitter_handle"] = valid_user.twitter_handle
        session["user_id"] = valid_user.user_id
        session["user_name"] = valid_user.user_name
        flash("Welcome back! You are logged in.") 
        return redirect("/inspire")
    else:
        flash("Twitter handle and password do not match. Please try again.")
        return redirect("/")


@app.route("/logged-out")
def log_out():
    """User log out."""

    # deleting user from the current session.
    del session["twitter_handle"] 
    del session["user_id"]
    del session["user_name"]

    # flash message for user.
    flash("You are now logged out. Have a wonderful day!")

    return redirect("/")


@app.route("/inspire")
def display_inspire():
    """Shows page where user clicks to get daily inspiration."""

    return render_template('inspire.html')



@app.route("/show-tweets.json", methods=['POST'])
def show_tweets():
    """Responds to ajax request for tweets, sentiments being analyzed."""

    twitter_handle = session["twitter_handle"] 
    classifier = load_classifier()
    user_tweets = connect_twitter_api(twitter_handle)
    tweet_sents =  get_user_sentiment(user_tweets, classifier)

    tweets_to_print = {}
    num=0

    for tweet, sent in tweet_sents:
        if sent == 1:
            tweets_to_print[num] = tweet, 'positive'
            num += 1
        else:
            tweets_to_print[num] = tweet, 'negative'
            num += 1

    return jsonify(tweets_to_print)



@app.route("/show-avg-sent.json", methods=['POST'])
def show_average():
    """Show average sentiment percentage."""

    twitter_handle = session["twitter_handle"] 
    classifier = load_classifier()
    user_tweets = connect_twitter_api(twitter_handle)
    tweet_and_sentiment = get_user_sentiment(user_tweets, classifier)
    number = get_average_sentiment(tweet_and_sentiment)
    percent_num = (number * 100)
    
    average_sentiment = {}
    average_sentiment["average"] = percent_num

    return jsonify(average_sentiment)


@app.route("/inspire-process.json", methods=['POST'])
def process_inspire():
    """Returns a quote of correct sentiment and store analyses info in db."""

    #getting twitter_handle & user_id from session
    twitter_handle = session["twitter_handle"] 
    user_id = session["user_id"]

    # get timestamp for storing to db when user clicks button
    timestamp = get_timestamp()

    quote_to_send = {}
    # calling get_quote function from twitter_analysis, passing in the twitter_handle
    # saving it to the quote_to_send dictionary as a value with the key "quote"
    quote_info = get_quote(twitter_handle, user_id)

    if len(quote_info) > 1:
        #adding the actual quote itself to a dictionary to send via JSON
        quote_to_send["quote"] = quote_info[0]

        # getting quote_id, sentiment to add to db
        quote_id = quote_info[1]
        sentiment = quote_info[2]

        #Part 2: send data to store in analyses in db
        # Store: user_id(y), timestamp(y), tweet_sent_id(y), quote_id(y)

        # adding analysis instance to the database
        analysis = Analyses(user_id=user_id, timestamp=timestamp, 
                            tweet_sent_id=sentiment, quote_id=quote_id)
        db.session.add(analysis)
        db.session.commit()

    else:
        quote_to_send["quote"] = quote_info[0]

    return jsonify(quote_to_send)


@app.route('/moods')
def show_moods_page():
    """Show page with data visualization of mood over time.
    """

    return render_template("moods.html")


@app.route('/mood-donut.json')
def make_donut_chart():
    """Sends dictionary data of mood over time to render DONUT chart."""

    user_id = session["user_id"]
    #query database for info in analyses table: sentiment, timestamp
    user_mood_data = (db.session.query(Analyses.timestamp, Analyses.tweet_sent_id)
                      .filter(Analyses.user_id==user_id).all())
    
    happy_feelings =[]
    sad_feelings =[]
    for timestamp, sentiment in user_mood_data:
        if sentiment==1:
            happy_feelings.append(sentiment)
        else:
            sad_feelings.append(sentiment)


    total_feelings = (len(happy_feelings) + len(sad_feelings))
    decimal_happy = float(len(happy_feelings)) / float(total_feelings)
    decimal_sad = float(len(sad_feelings)) / float(total_feelings)
    percent_happy = round((decimal_happy * 100), 0)
    percent_sad = round((decimal_sad * 100), 0)
   
    
    mood_data = { "labels": [
                    "Positive Mood",
                    "Negative Mood"],
                
                   "datasets": [
                       {
                        "data": [percent_happy, percent_sad],
                        "backgroundColor": [
                            "#00FFFF",
                            "#7000e0"
                            ],
                        "hoverBackgroundColor": [
                            "#FF6384",
                            "#36A2EB",]   }]
                        }

    return jsonify(mood_data)


@app.route('/mood-line.json')
def make_line_chart():
    """Sends dictionary data of mood over time to render LINE chart."""

    user_id = session["user_id"]
    #query database for info in analyses table: sentiment, timestamp
    user_mood_data = (db.session.query(Analyses.timestamp, Analyses.tweet_sent_id)
                      .filter(Analyses.user_id==user_id).order_by(Analyses.timestamp)
                      .all())
    
    timestamps = []
    sentiments = []
    for timestamp, sentiment in user_mood_data:
        timestamps.append(timestamp)
        sentiments.append(sentiment)
        

    date_labels =[]
    for time in timestamps:
        date = "{:%b %d, %Y}".format(time)
        date_labels.append(date)

    
    # will display better on line chart if negative feeling is -1 and positive feeling is 1
    for n, i in enumerate(sentiments):
        if i==2:
            sentiments[n] = -1


# labels will be the timestamps
#data will be 1s and 2s based on sentiment at time stamps

    mood_data = {
        "labels": date_labels,
        "datasets": [
            {
                "label": "Your Mood Over Time",
                "fontFamily": "'Helvetica Neue",
                "fontStyle": "bold",
                "fill": True,
                "lineTension": 0.5,  
                "backgroundColor": "rgba(135, 252, 255, 0.8)",
                "borderColor": "rgba(135, 252, 255, 0.9)",
                "borderCapStyle": 'butt',
                "borderDash": [],
                "borderWidth": 0,
                "borderDashOffset": 0.0,
                "borderJoinStyle": 'miter',
                "pointBorderColor": "rgba(110,207,255,1)",
                "pointBackgroundColor": "rgba(31,189,255,1)",
                "pointBorderWidth": 1,
                "pointHoverRadius": 5,
                "pointHoverBackgroundColor": "#fff",
                "pointHoverBorderColor": "rgba(220,220,220,1)",
                "pointHoverBorderWidth": 2,
                "pointRadius": 3,
                "pointHitRadius": 10,
                "data": sentiments,
                "spanGaps": False}
        ]
    }

    return jsonify(mood_data)



@app.route('/mood-bar.json')
def make_bar_chart():
    """Sends dictionary data of level of positivity of each day of the week."""

    user_id = session["user_id"]
    # query all positive timestamps of the user
    
    positive_timestamps = (db.session.query(Analyses.timestamp)
                            .filter(Analyses.user_id==user_id, 
                                    Analyses.tweet_sent_id==1)
                            .order_by(Analyses.timestamp)
                            .all())
    negative_timestamps = (db.session.query(Analyses.timestamp)
                            .filter(Analyses.user_id==user_id, 
                                    Analyses.tweet_sent_id==2)
                            .order_by(Analyses.timestamp)
                            .all())

    pos_day_numbers = []
    neg_day_numbers = []
    # get datetime object from query object result tuple and format for .isoweekday()
    # find out which day of the week each datetime is on
    for item in positive_timestamps:
        date_time = str(item[0])
        strip_date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        just_three = strip_date_time.date()
        weekday = just_three.isoweekday()
        pos_day_numbers.append(weekday)

    for item in negative_timestamps:
        date_time = str(item[0])
        strip_date_time = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
        just_three = strip_date_time.date()
        weekday = just_three.isoweekday()
        neg_day_numbers.append(weekday)

    pos_total_days = len(pos_day_numbers)
    neg_total_days = len(neg_day_numbers)

    pos_weekday_numbers ={1 : 0, 2 :0, 3 :0, 4:0, 5:0, 6:0, 7:0}
    for item in pos_day_numbers:
        pos_weekday_numbers[item] += 1
        

    neg_weekday_numbers ={1 : 0, 2 :0, 3 :0, 4:0, 5:0, 6:0, 7:0}
    for item in neg_day_numbers:
        neg_weekday_numbers[item] += 1
       
    # list comprehension of positive weekday info to pass to charts.js
    pos_data_to_send = [pos_weekday_numbers[key]/float(pos_total_days) for key 
                        in sorted(pos_weekday_numbers)]

    # list comprehension of negative weekday info to pass to charts.js
    neg_data_to_send = [neg_weekday_numbers[key]/float(neg_total_days) for key 
                        in sorted(neg_weekday_numbers)]

    
    bar_data = {
    "labels": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "datasets": [
        {
            "label": "Happiness by Day",
            "backgroundColor": [
                "#00FFFF",
                "#00FFFF",
                "#00FFFF",
                "#00FFFF",
                "#00FFFF",
                "#00FFFF",
                "#00FFFF"
            ], 
            "hoverBackgroundColor": [
                            "#ff69b4",
                            "#ff69b4",
                            "#ff69b4",
                            "#ff69b4",
                            "#ff69b4",
                            "#ff69b4",
                            "#ff69b4"],
            "data": pos_data_to_send,
        },

        {
         "label": "Unhappiness by Day",
            "backgroundColor": [
                '#7000e0',
                '#7000e0',
                '#7000e0',
                '#7000e0',
                '#7000e0',
                '#7000e0',
                '#7000e0'
            ], 
            "hoverBackgroundColor": [
                            "#00E000",
                            "#00E000",
                            "#00E000",
                            "#00E000",
                            "#00E000",
                            "#00E000",
                            "#00E000"],
            "data": neg_data_to_send,


        }
    ]
};
    return jsonify(bar_data)



@app.route('/set-reminder.json', methods=['POST'])
def set_reminder():
    """User selects time to receive reminder text. Stored in Database."""

    user_id= session.get("user_id")
    reminder_choice = request.form.get("reminder")
    telephone = request.form.get("remind-phone")
  
    user = User.query.filter_by(user_id=user_id).first()
    user.reminder_time = reminder_choice
    user.phone = telephone
    db.session.commit()

    # flash message for the user
    flash("You will receive your daily reminder every {}.".format(reminder_choice))

    return 'success'



# __main__ makes this stuff happen when i am running this file directly, not importing
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    # app.config['TESTING'] = True
    if app.config['TESTING'] is True:
        connect_to_db(app, "postgresql:///fake_db")
    else:
        connect_to_db(app)


    # Use the DebugToolbar
    DebugToolbarExtension(app)

    
    app.run(port=5000, host='0.0.0.0')










