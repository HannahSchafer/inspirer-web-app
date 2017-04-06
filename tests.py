# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import unittest
import twitter_analysis
import server
from model import connect_to_db, db

# docstrings!!!!


class FlaskTestsDatabase(unittest.TestCase):
    """Flask tests that use the database."""

    def setUp(self):
        """Stuff to do before every test."""

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

        result = self.client.post('/process-registration', data={'user_name': \
                      'Mary', 'password' : 'wonderland', 'twitter_handle' : 'Mary33', \
                      'email': 'Mary@wonderland.com', 'phone': '243-545-9898' }, follow_redirects=True)
        self.assertIn('Welcome to Inspiratoren!', result.data)

    def test_reg_form_2(self):
        """Tests registration form in case when it is already an existing user."""

        result = self.client.post('/process-registration', data={'user_name': \
                      'hannah', 'password' : 'password', 'twitter_handle' : 'HannahSchafer18', \
                      'email' : 'hannah@banana.com', 'phone': '5555555555' }, follow_redirects=True)
        self.assertIn('Welcome back! You already have an account. Please log in with your twitter handle and password.', result.data)

    def test_login_form_1(self):
        """Tests registration form in case when it is a valid existing user."""

        result = self.client.get('/login-validation', data={'twitter_handle' : 'HannahSchafer18', \
                               'password' : 'password'}, follow_redirects=True)
        self.assertIn('Welcome back! You are logged in.', result.data)

    def test_login_form_2(self):
        """Tests registration form in case when it is not a valid existing user."""

        result = self.client.get('/login-validation', data={'twitter_handle' : 'HannahSchafer18', \
                               'password' : 'hello'}, follow_redirects=True)
        self.assertIn('Twitter handle and password do not match. Please try again.', result.data)

    def test_login_form_3(self):
        """Tests registration form in case when it is not a valid existing user."""
        
        result = self.client.get('/login-validation', data={'twitter_handle' : 'Mary33', \
                               'password' : 'password'}, follow_redirects=True)
        self.assertIn('Twitter handle and password do not match. Please try again.', result.data)



class MyAppUnitTestCase(unittest.TestCase):
    """Unit tests"""

    def setUp(self):
        print "(setUp ran)"
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get('/')
        self.assertIn('<h1>Inspiratören</h1>', result.data)

    def test_register(self):
        result = self.client.get('/register')
        self.assertIn('<h1>Register for Inspiratören</h1>', result.data)

    def test_login(self):
        result = self.client.get('/log-in')
        self.assertIn('<h1>Log in</h1>', result.data)

    def test_inspire(self):
        result = self.client.get('/inspire')
        self.assertIn('Inspire Me', result.data)

    















if __name__ == "__main__":
    unittest.main()



