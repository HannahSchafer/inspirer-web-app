"""The Inspirer flask app server file."""


from jinja2 import StrictUndefined
from flask import (Flask, jsonify, render_template, redirect, request,
                    flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Quote, Analyses, Sentiment, Classifier



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

    given_twitter = request.form.get("twitter_handle")
    given_password = request.form.get("password")

    print given_twitter

    existing_user = User.query.filter(User.twitter_handle==given_twitter).first()

    if existing_user:
        flash("Welcome back! You already have an account. Please log in with your twitter handle and password.")
        return redirect("/")

    else:
        new_user = User(user_name=user_name, email=email, twitter_handle='chrissyteigen', password=given_password, phone=phone)
        user_id = new_user.user_id

        # Add new_user to the database session so it can be stored
        db.session.add(new_user)

        # Commiting to the database
        db.session.commit()

        # flash message for the user
        flash("Welcome to Inspiratoren!")

        # User is now in a session
        session["twitter_handle"] = twitter_handle
        session["user_id"] = user_id
        session["user_name"] = valid_user.user_name

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
        print session
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
    """Returns a quote of correct sentiment"""


    #Part 1: send data to store in analyses in db

    #Part 2: return quote to user on same page
    quote_info = twitter_analysis.get_quote()

    return jsonify(quote_info)





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










