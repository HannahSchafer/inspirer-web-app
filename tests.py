# encoding=utf8  
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

from selenium import webdriver
from unittest import TestCase
import pickle

import twitter_analysis
from server import app
from model import connect_to_db, db, example_data, Sentiment, User, Quote





class FlaskTestsDatabase(TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

        # Connect to test database
        connect_to_db(app, "postgresql:///fake_db")
        

        # Create tables
        db.create_all()

        # seed sample data
        example_data()


    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_reg_form(self):
        """Tests registration form in case when it is a valid new user."""

        result = (self.client.post('/process-registration', data={'user_name': 
                      'Mary', 'password' : 'wonderland', 'twitter_handle' : 'Mary33', 
                      'email': 'Mary@wonderland.com', 'phone': '243-545-9898', 'reminder_time': 'evening' }, follow_redirects=True))


        self.assertIn(u'Welcome to Sparrö!', result.data)

    def test_reg_form_2(self):
        """Tests registration form in case when it is already an existing user."""

        result = (self.client.post('/process-registration', data={'user_name': 
                      'Aimee', 'password' : 'art', 'twitter_handle' : 'Artist', 
                      'email' : 'Aimee@gmail.com', 'phone': '555-555-9999', 'reminder_time' :'morning' }, follow_redirects=True))
        self.assertIn('Welcome back! You already have an account. Please log in with your twitter handle and password.', result.data)


    def test_login_form_1(self):
        """Tests login form in case when it is a valid existing user."""

        result = self.client.get('/login-validation', query_string={'twitter_handle' : 'NuBaby', 'password' : 'clown eyes'}, follow_redirects=True)
        self.assertIn('Welcome back! You are logged in.', result.data)


    def test_login_form_2(self):
        """Tests login form in case when it is not a valid existing user."""

        result = self.client.get('/login-validation', query_string={'twitter_handle' : 'HannahSchafer18', 'password' : 'hello'}, follow_redirects=True)
        self.assertIn('Twitter handle and password do not match. Please try again.', result.data)

    def test_login_form_3(self):
        """Tests login form in case when it is not a valid existing user."""

        result = (self.client.get('/login-validation', data={'twitter_handle' : 'Mary33', 
                               'password' : 'password'}, follow_redirects=True))
        self.assertIn('Twitter handle and password do not match. Please try again.', result.data)

    







class MyAppUnitTestCase(TestCase):
    """Unit tests"""

    def setUp(self):
        print "(setUp ran)"
        self.client = app.test_client()
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'



    def test_homepage(self):
        """Tests home page rendering."""

        result = self.client.get('/')
        self.assertIn(u'<title>Sparrö</title>', result.data)

    def test_register(self):
        """Tests registration page rendering."""

        result = self.client.get('/register')
        self.assertIn(u'<h1>Register for Sparrö</h1>', result.data)

    def test_inspire(self):
        """Tests inspire page rendering."""

        # for session:
        with self.client as c:
          with c.session_transaction() as sess:
              sess['twitter_handle'] = 'NuBaby'

        result = self.client.get('/inspire')
        self.assertIn('Inspire Me', result.data)
        self.assertEqual(result.status_code, 200) 

    def test_moods(self):
        """Tests charts.js page rendering."""

        # for session:
        with self.client as c:
          with c.session_transaction() as sess:
              sess['twitter_handle'] = 'NuBaby'

        result = self.client.get('/moods')
        self.assertEqual(result.status_code, 200) 

    def test_logged_out(self):
        """Tests log out route."""

        with self.client as c:
          with c.session_transaction() as sess:
              sess['twitter_handle'] = 'NuBaby'
              sess['user_name'] = 'Favinn'
              sess['user_id'] = 1


        result = self.client.get('/logged-out', follow_redirects=True)
        self.assertIn("You are now logged out. Have a wonderful day!", result.data)

    
    



class TwitterTests(TestCase):
    """Tests that require a mock API call to Twitter API."""
    
    def setUp(self):
        print "(setUp ran)"

        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'key'
        self.client = app.test_client()

        with self.client as c:
          with c.session_transaction() as sess:
              sess['user_id'] = 1
              sess['twitter_handle'] = 'NuBaby'

         # Connect to test database
        connect_to_db(app, "postgresql:///fake_db")

        # Create tables
        db.create_all()

         # seed sample data
        example_data()


        def _test_connect_twitter_api(twitter_handle):
            """Mocking out Twitter API."""

            connect_twitter_response = pickle.load(open("twitter_data.pickle", "rb"))

            return connect_twitter_response

        twitter_analysis.connect_twitter_api = _test_connect_twitter_api 


    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()


    def test_inspire_process(self):
        """Tests inspire_process route and multiple functions from twitter_analysis.
        """

        result = (self.client.post('/inspire-process.json', data={'user_id' : '1',
                                   'timestamp' : "2017-04-29 01:42:00", 
                                   'tweet_sent_id': '1', "quote_id": '600'}, follow_redirects=True))
        self.assertIn("I am a positive quote!", result.data)

   



class TestUserLogIn(TestCase):
    """Selenium tests that test user experience on browser."""

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        
        app.config['TESTING'] = True

    def tearDown(self):
        self.browser.quit()  

    def test_view_log_in_button(self):
        self.browser.get('http://localhost:5000/')
        assert u"Sparrö" in self.browser.title
        assert "Log in" in self.browser.page_source
        
    def test_sign_in(self):
        self.browser.get('http://localhost:5000/')
        self.browser.find_element_by_id('login').click()
        twitter_handle = self.find_element_by_id("twitter_handle")
        twitter_handle.send_keys('NuBaby')
        password = self.browser.find_element_by_id('pw')
        password.send_keys("clown eyes")



if __name__ == "__main__":
#
    import unittest

    unittest.main()



