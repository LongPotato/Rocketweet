import oauth2 as oauth
import json
import random
import sys
import tokens as TOKEN

def get_tweets(keyword):
	c_key = TOKEN.CONSUMER_KEY
	c_secret = TOKEN.CONSUMER_SECRET
	a_key = TOKEN.ACCESS_KEY
	a_secret = TOKEN.ACCESS_SECRET

	user = oauth.Consumer(key=c_key, secret=c_secret)
	access_token = oauth.Token(key=a_key, secret=a_secret)
	client = oauth.Client(user, access_token)

	url = "https://api.twitter.com/1.1/search/tweets.json?q=%" + keyword + "&include_entities=true&count=20"
	response, content = client.request(url)

	# Decode the data and parse to json object
	tweets = json.loads(content.decode('utf8'))
	
	return tweets

	
def get_random_tweet(tweets):
	index = random.randrange(0, len(tweets))
	return tweets['statuses'][index]


def get_media(tweet):
	media_urls = []
	# Check if the tweet contain any media urls
	if 'media' in tweet['entities']:
		for media in tweet['entities']['media']:
			media_urls.append(media['media_url'])	

	return media_urls


def main(argv):
	tweets = get_tweets(argv)

	if (len(tweets['statuses']) != 0):
		tweet = get_random_tweet(tweets)
		media = get_media(tweet)
	
		print("\nKeyword: " +  argv)
		print("@" + tweet['user']['name'] + " tweeted: " + tweet['text'])
		print("Media: " + ", ".join(media) + "\n")
	else:
		print("\nNo tweet found :(\n")
	

if __name__ == "__main__":
	# Only accept the first argument as keyword
	main(sys.argv[1])



