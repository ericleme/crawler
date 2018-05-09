import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

access_token = "xxx"
access_secret =  "xxx"
consumer_key =  "xxx"
consumer_secret =  "xxx"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

timeline_tweets = api.home_timeline()

class StdOutListener(StreamListener):
    def on_data(self, status):
        print(status)
    def on_error(self, status):
        print (status)

l = StdOutListener()
stream = Stream(auth, l)
stream = tweepy.Stream(auth = api.auth, listener=StdOutListener())
stream.filter(track=['Honda Fit'], async=True)
