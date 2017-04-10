
# -*- coding: utf-8 -*-

import os
from twilio.rest import Client

ACCOUNT_SID = os.environ["TWILIO_Account_SID"]
AUTH_TOKEN = os.environ["TWILIO_Auth_Token"]
my_cell = "+16107421594"
my_twilio="+13024837183"
my_msg="Sparrö is ready to deliver your daily inspiration!"

def send_message(from_, to, body):
    """Send reminder message to user with Twilio."""
    # instantiating object
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    client.messages.create(from_=my_twilio,
                           to=my_cell,
                           body=my_msg)
    # print(message.sid)


# send_message(my_twilio, my_cell, my_msg)