# inspirer-web-app (i.e. Sparrö)

Project:
Sparrö is a web app that serves as a means to personal empathy, self-understanding, and daily inspiration. Sparrö draws on natural language processing to conduct sentiment analysis of a user’s Twitter feed. Based on the analysis of the user’s current mood, the user receives an inspirational quote or poem suited to their attitude. The app can track the user’s attitude over time, visualize this information, and let the user set reminders via text message.

Tech Stack:
Python, JavaScript, Flask, Postgresql, SQLAlchemy, SQL, NLTK, Cron, D3.js, Typed.js, Charts.js,  jQuery, AJAX, JSON, Bootstrap

APIs:
Twitter API, Twilio API



Features:
After building my data model and seeding my PostgreSQL database,  I trained the Naïve Bayes Classifier from Python's NLTK library to understand positive and negative lablels through my supervised training data set of 600 tweets. 
