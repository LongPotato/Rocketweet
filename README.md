# Rocketweet
Simple program that returns a random tweet based on a 'keyword' search.

## Setup
To get it running in your console, download this repo and do the following:

1. Get your credentials and access token from [dev.twitter.com](https://dev.twitter.com/oauth/overview/application-owner…)

2. Intall the dependencies: [`python-oauth2`](https://github.com/joestump/python-oauth2)

2. Create a new file named `tokens.py` in the same directory, enter your keys:

```
# Twitter API credentials
CONSUMER_KEY = "Your_Consumer_Key"
CONSUMER_SECRET = "Your_Consumer_Secret_Key"
ACCESS_KEY = "Your_Access_Key_Key"
ACCESS_SECRET = "Your_Access_Secret_Key"
```

## Run test

```
$ python3 test_connection.py -v

test_oauth (__main__.TestConnection) ... ok
test_tokens (__main__.TestConnection) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.334s

OK
```

## Sample output:

```
$ python3 rocketweet.py trump

Keyword: trump
@❂ jazmin ❂ tweeted: RT @chrissyteigen: "Donald Trump can't even spell the word 'politician'" is officially 
too literal of a joke https://t.co/t7vzf30ygk
Media: http://pbs.twimg.com/media/CdXlKGhUMAE7_8-.jpg

```



