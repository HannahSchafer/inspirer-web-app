# -*- coding: utf-8 -*-
"""This file will be run as a cron job every morning at 9am."""



import os
from twilio.rest import Client

from model import connect_to_db, db, Quote, Sentiment, User, Analyses
from flask import Flask

app = Flask(__name__)
connect_to_db(app)


ACCOUNT_SID = os.environ["TWILIO_Account_SID"]
AUTH_TOKEN = os.environ["TWILIO_Auth_Token"]
my_twilio="+13024837183"
my_msg="Sparrö is ready to deliver your daily inspiration!"

def send_message(send_number):
    """Send reminder message to user with Twilio."""
    # instantiating object
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(from_=my_twilio,
                           to=send_number,
                           body=my_msg)
    # print(message.sid)


# look through database to see who has opted in for morning and both reminders.
# get their phone numbers. 
morning_objects = db.session.query(User.phone).filter((User.reminder_time=='morning') | (User.reminder_time=='morning and evening')).all()

# pass their phone numbers to the send_message function
morning_birds = []
for item in morning_objects:
    morning_birds.append(item[0])
    

# pass their phone numbers to the send_message function
for phone in morning_birds:
    send_number = phone
    send_message(send_number)










