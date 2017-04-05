import unittest
import twitter_analysis
import server

# Testing my routes in my server
class MyAppIntegrationTestCase(unittest.TestCase):
    """Examples of unit tests: discrete code testing."""

    def setUp(self):
        print "(setUp ran)"
        self.client = server.app.test_client()
        server.app.config['TESTING'] = True

    def test_homepage(self):
        client = server.app.test_client()

        result = client.get('/')
        self.assertIn('<h1>Inspiratören</h1>', result.data)

    def test_register(self):
        client = server.app.test_client()

        result = client.get('/register')
        self.assertIn('<h1>Register for Inspiratören</h1>', result.data)

    def test_login(self):
        client = server.app.test_client()

        result = client.get('/log-in')
        self.assertIn('<h1>Log in</h1>', result.data)

    # def test_registration_form(self):
    #     client = server.app.test_client()
    #     result = client.post('/process-registration', data={'user_name': 'hannah'})
    #     self.assertIn('hannah', result.data)















if __name__ == "__main__":
    unittest.main()