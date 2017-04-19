# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import unittest
import twitter_analysis
import server
from model import connect_to_db, db, example_data
import pickle




class FlaskTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

        # Connect to test database
        connect_to_db(server.app, "postgresql:///fake_db")

        # Create tables
        db.create_all()

        # seed sample data
        example_data()

        server.app.config['TESTING'] = True
        self.client = server.app.test_client()

        
    def tearDown(self):
        """Do at end of every test."""

        db.session.close()
        db.drop_all()

    def test_reg_form(self):
        """Tests registration form in case when it is a valid new user."""

        result = (self.client.post('/process-registration', data={'user_name': 
                      'Mary', 'password' : 'wonderland', 'twitter_handle' : 'Mary33', 
                      'email': 'Mary@wonderland.com', 'phone': '243-545-9898' }, follow_redirects=True))
        self.assertIn(u'Welcome to Sparrö!', result.data)

    def test_reg_form_2(self):
        """Tests registration form in case when it is already an existing user."""

        result = (self.client.post('/process-registration', data={'user_name': 
                      'Aimee', 'password' : 'art', 'twitter_handle' : 'Artist', 
                      'email' : 'Aimee@gmail.com', 'phone': '555-555-9999' }, follow_redirects=True))
        self.assertIn('Welcome back! You already have an account. Please log in with your twitter handle and password.', result.data)


    def test_login_form_1(self):
        """Tests registration form in case when it is a valid existing user."""

        result = (self.client.post('/login-validation', data={'twitter_handle' : 'HannahSchafer18', 
                                  'password' : 'password'}, follow_redirects=True))
        self.assertIn('Welcome back! You are logged in.', result.data)


    def test_login_form_2(self):
        """Tests registration form in case when it is not a valid existing user."""

        result = (self.client.get('/login-validation', data={'twitter_handle' : 'HannahSchafer18', 
                               'password' : 'hello'}, follow_redirects=True))
        self.assertIn('Twitter handle and password do not match. Please try again.', result.data)

    def test_login_form_3(self):
        """Tests registration form in case when it is not a valid existing user."""

        result = (self.client.get('/login-validation', data={'twitter_handle' : 'Mary33', 
                               'password' : 'password'}, follow_redirects=True))
        self.assertIn('Twitter handle and password do not match. Please try again.', result.data)



class MyAppUnitTestCase(unittest.TestCase):
    """Unit tests"""

    def setUp(self):
        print "(setUp ran)"
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get('/')
        self.assertIn(u'<h1>Sparrö</h1>', result.data)


    def test_inspire(self):
        result = self.client.get('/inspire')
        self.assertIn('Inspire Me', result.data)
        self.assertEqual(result.status_code, 200) 

    def test_moods(self):
        result = self.client.get('/moods')
        self.assertEqual(result.status_code, 200) 



class TwitterTests(unittest.TestCase):
    """Tests that require a mock API call to Twitter API."""
    
    def setUp(self):
        print "(setUp ran)"

        server.app.config['TESTING'] = True
        server.app.config['SECRET_KEY'] = 'key'
        self.client = server.app.test_client()

        with self.client as c:
          with c.session_transaction() as sess:
              sess['user_id'] = 1
              sess['twitter_handle'] = 'HannahSchafer18'

         # Connect to test database
        connect_to_db(server.app, "postgresql:///fake_db")

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
        self.assertIn('"So excited for the next episode of my new favorite show: Black-ish!!!"', result.data)
        self.assertIn("I am a positive quote!", result.data)
        self.assertIn(80, result.data)





if __name__ == "__main__":
    unittest.main()



