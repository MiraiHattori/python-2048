import os, sys
import twitter

def tweet(string):
    consumer_key = os.getenv("TWITTER_CONSUMER_KEY", "")
    consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET", "")
    token = os.getenv("TWITTER_TOKEN", "")
    token_secret = os.getenv("TWITTER_TOKEN_SECRET", "")

    if not consumer_key or not consumer_secret or not token or not token_secret:
        print("twitter token is not set. pass")
        return

# auth = twitter.OAuth(token=token, token_secret=token_secret, consumer_key=consumer_key, consumer_secret=consumer_secret,)
    auth = twitter.OAuth(token, token_secret, consumer_key, consumer_secret)
    t = twitter.Twitter(auth=auth)
    t.statuses.update(status=string)
