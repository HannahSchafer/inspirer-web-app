"""The Inspirer flask app server file."""


from jinja2 import StrictUndefined
from flask import (Flask, jsonify, render_template, redirect, request,
                    flash, session)
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db, User, Quote, Analyses, Sentiment, Classifier
# from classifier import ####

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
        new_user = User(user_name=user_name, email=email, twitter_handle=twitter_handle, password=given_password, phone=phone)
        user_id = new_user.user_id

        # Add new_user to the database session so it can be stored
        db.session.add(new_user)

        # Commiting to the database
        db.session.commit()

        # flash message for the user
        flash("Welcome to Inspirador!")

        # User is now in a session
        session["user_id"] = user_id

        return redirect("/inspire")


@app.route("/log-in")
def log_in():
    """Shows login form."""

    return render_template("login.html")


# @app.route("/inspire")
# def inspire_me():
#     """Shows page where user clicks to get daily inspiration."""

#     # User is still in a session
#     session["user_id"] = user_id

#     return render_template('inspire.html')



# @app.route("/inspire-process")
# def inspire_me():
#     """Shows page where user clicks to get daily inspiration."""





@app.route("/logged-out")
def log_out():
    """User log out."""

    # deleting user from the current session.
    del session["user_id"] 

    # flash message for user.
    flash("Have a wonderful day. Visit again soon.")

    return redirect("/")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    
    app.run(port=5000, host='0.0.0.0')










