# import sys  
# reload(sys)  
# sys.setdefaultencoding('utf8')
# from __future__ import unicode_literals

import os
from twilio.rest import Client

ACCOUNT_SID = os.environ["TWILIO_Account_SID"]
AUTH_TOKEN = os.environ["TWILIO_Auth_Token"]
my_cell = "+16107421594"
my_twilio="+13024837183"
my_msg="Sparro is ready to deliver your daily inspiration!"


# instantiating object
client =Client(ACCOUNT_SID, AUTH_TOKEN)


client.messages.create(from_=my_twilio,
                       to=my_cell,
                       body=my_msg)