"""The Inspirer flask app server file."""


from jinja2 import StrictUndefined
from flask import (Flask, jsonify, render_template, redirect, request,
                    flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Quote, Analyses, Sentiment, Classifier

from helper_functions import get_timestamp
from twitter_analysis import get_quote
from datetime import datetime



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


    existing_user = User.query.filter((User.twitter_handle==twitter_handle) & (User.password==given_password)).first()

    if existing_user:
        flash("Welcome back! You already have an account. Please log in with your twitter handle and password.")
        return redirect("/")

    else:
        # class object 'new user'
        new_user = User(user_name=name, email=email, twitter_handle=twitter_handle, password=given_password, phone=phone)
        

        # Add new_user to the database session so it can be stored
        db.session.add(new_user)

        # Commiting to the database
        db.session.commit()

        # flash message for the user
        flash("Welcome to Inspiratoren!")

        # after commited to db, now new_user has a user_id
        user_id = new_user.user_id

        # User is now in a session
        session["twitter_handle"] = twitter_handle
        session["user_id"] = user_id
        session["user_name"] = name


        return redirect("/inspire")


@app.route("/log-in")
def log_in():
    """Shows login form."""

    return render_template("login.html")


@app.route("/login-validation")
def check_login():
    """Compares login info to db info."""

    twitter_handle = request.args.get("twitter_handle")
    password = request.args.get("password")

    valid_user = User.query.filter((User.twitter_handle==twitter_handle) & \
                 (User.password==password)).first()

    if valid_user:
        session["twitter_handle"] = valid_user.twitter_handle
        session["user_id"] = valid_user.user_id
        session["user_name"] = valid_user.user_name
        flash("Welcome back! You are logged in.") 
        return redirect("/inspire")
    else:
        flash("Twitter handle and password do not match. Please try again.")
        return redirect("/log-in")


@app.route("/logged-out")
def log_out():
    """User log out."""

    # deleting user from the current session.
    del session["twitter_handle"] 
    del session["user_id"]
    del session["user_name"]

    # flash message for user.
    flash("You are now logged out. Have a wonderful day! ")

    return redirect("/")


@app.route("/inspire")
def display_inspire():
    """Shows page where user clicks to get daily inspiration."""

    return render_template('inspire.html')



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
        analysis = Analyses(user_id = user_id, timestamp = timestamp, tweet_sent_id = sentiment, quote_id = quote_id)
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
    user_mood_data = db.session.query(Analyses.timestamp, Analyses.tweet_sent_id).filter(Analyses.user_id==user_id).all()
    
    happy_feelings =[]
    sad_feelings =[]
    for timestamp, sentiment in user_mood_data:
        if sentiment==1:
            happy_feelings.append(sentiment)
        else:
            sad_feelings.append(sentiment)


    total_feelings = (len(happy_feelings) + len(sad_feelings))
    percent_happy = float(len(happy_feelings)) / float(total_feelings)
    percent_sad = float(len(sad_feelings)) / float(total_feelings)
   
    
    mood_data = { "labels": [
                    "Positive Mood",
                    "Negative Mood"],
                
                   "datasets": [
                       {
                        "data": [percent_happy, percent_sad],
                        "backgroundColor": [
                            "#00FFFF",
                            "#800080"
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
    user_mood_data = db.session.query(Analyses.timestamp, Analyses.tweet_sent_id).filter(Analyses.user_id==user_id).order_by(Analyses.timestamp).all()

    timestamps = []
    sentiments = []
    for timestamp, sentiment in user_mood_data:
        timestamps.append(timestamp)
        sentiments.append(sentiment)

    date_labels =[]
    for time in timestamps:
        date = "{:%B %d, %Y}".format(time)
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

# __main__ makes this stuff happen when i am running this file directly, not importing
if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    
    app.run(port=5000, host='0.0.0.0')










