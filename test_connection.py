import unittest
import os.path
import oauth2 as oauth
import tokens as TOKEN

class TestConnection(unittest.TestCase):

	# Test for existing tokens file
	def test_tokens(self):
		if (os.path.isfile('tokens.py')):
			found = True
		else:
			found = False
		self.assertEqual(found, True, "tokens.py does not exist")
    	
    	
    	#Test for valid oauth connection	
	def test_oauth(self):
		c_key = TOKEN.CONSUMER_KEY
		c_secret = TOKEN.CONSUMER_SECRET
		a_key = TOKEN.ACCESS_KEY
		a_secret = TOKEN.ACCESS_SECRET

		user = oauth.Consumer(key=c_key, secret=c_secret)
		access_token = oauth.Token(key=a_key, secret=a_secret)
		client = oauth.Client(user, access_token)

		url = "https://api.twitter.com/1.1/statuses/home_timeline.json"
		response, content = client.request(url)
		
		self.assertEqual(response.status, 200, "connection failed")


if __name__ == '__main__':
	unittest.main(warnings='ignore')
