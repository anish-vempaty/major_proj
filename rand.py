# Importing Tweepy and time
import tweepy
import time
from kafka import SimpleProducer, KafkaClient
import json
from tweepy import Stream
# Credentials (INSERT YOUR KEYS AND TOKENS IN THE STRINGS BELOW)

access_token = "1337389163360866309-FnZf6KOziF12KfmXujKe4s9TxswEGX"
access_token_secret =  "OGyMG4WDCDHsijcu6A9pKNjzqepIC9NITBUU0rgvWy2dL"
api_key =  "L62BZ0OoGklQEdFWELOCEodYw"
api_secret =  "zLBtBsQluvvVOyL3gAI4jXdwX3SLraAdPXdkqTalC5f5sBDyoK"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAMs%2BgwEAAAAAS70koT9pbjaVIwtsJjXN%2B2lLfFQ%3DSk1YvgmTzBHn1rTNnUf3YqoYYMwY7lEogsbV5nIu66cHIMfD1Z"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

search_terms = ["RailMinIndia","rail minister","suresh prabhu","northern railways"]

# Bot searches for tweets containing certain keywords
class MyStream(tweepy.StreamingClient):

    # This function gets called when the stream is working
    def on_connect(self):

        print("Connected")


    # This function gets called when a tweet passes the stream
    def on_tweet(self, tweet):

        # Displaying tweet in console
        if tweet.referenced_tweets == None:
            print(tweet.text)
            client.like(tweet.id)

            # Delay between tweets
            time.sleep(0.5)
        

# Creating Stream object
stream = MyStream(bearer_token=bearer_token)
class StdOutListener(Stream):
    def on_data(self, data):
        producer.send_messages("twitterstream", data.encode('utf-8','ignore'))
        data=json.loads(data)
        try:
                print (data["text"])
        except:
                print(data["text"])
        return True
    

# Adding terms to search rules
# It's important to know that these rules don't get deleted when you stop the
# program, so you'd need to use stream.get_rules() and stream.delete_rules()
# to change them, or you can use the optional parameter to stream.add_rules()
# called dry_run (set it to True, and the rules will get deleted after the bot
# stopped running).
for term in search_terms:
    stream.add_rules(tweepy.StreamRule(term))

# Starting stream
stream.filter(tweet_fields=["referenced_tweets"])
kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track=['RailMinIndia','rail minister','suresh prabhu','northern railways'], stall_warnings=True, languages = ['en'])
