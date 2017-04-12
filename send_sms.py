
# -*- coding: utf-8 -*-

import os
from twilio.rest import Client

ACCOUNT_SID = os.environ["TWILIO_Account_SID"]
AUTH_TOKEN = os.environ["TWILIO_Auth_Token"]
my_cell = "+16107421594"
my_twilio="+13024837183"
my_msg="Sparrö is ready to deliver your daily inspiration!"

def send_message():
    """Send reminder message to user with Twilio."""
    # instantiating object
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(from_=my_twilio,
                           to=my_cell,
                           body=my_msg)
    # print(message.sid)


send_message()



# look through database to see who has opted in for morning reminders
# look through database to see who has opted for evening reminders
# get their phone numbers. pass their phone numbers to the send_message function
# set up 2 cron jobs, one to run the script in the morning, one to run it in the evening.