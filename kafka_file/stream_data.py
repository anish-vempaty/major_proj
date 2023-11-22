

#from tweepy.streaming import StreamListener
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import StreamingClient
from kafka import SimpleProducer, KafkaClient, KafkaProducer
import json
import time

access_token = "1337389163360866309-SrRo24ETqqD9MZ0N2YGiLwe7nsfeXq"
access_token_secret =  "7YR6j2X7TCiUSe0B61DNboI0Xyab1Rt41plPVHJWbgdf1"
consumer_key =  "bCxG7qQNMx2NAnHFbIQrnBNWA"
consumer_secret =  "6C73JOkn7FaXcWGKHpsQdJmTiCmplOyZybsq7Am7BINShFH9CO"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAD2omAEAAAAARu1i5QTP%2BcMyRx9dZj00esmPlgs%3Diz4lNyT3KDPh8XuRYYD8U7ths0Gm7rJqd19Ql1OrXYsE1Wn7IV"

client = tweepy.Client(bearer_token, consumer_key,consumer_secret,access_token,access_token_secret)
auth = tweepy.OAuth1UserHandler(consumer_key,consumer_secret,access_token,access_token_secret)
api=tweepy.API(auth)
class StdOutListener(StreamingClient):
        def on_data(self, data):
                producer.send("twitterstream", data)
                a_data=json.loads(data)
                try:
                        print (a_data['data']['text'])
                except:
                        print(a_data['data']['text'])
                time.sleep(0.5)
                return True
        def on_error(self, status):
                print(status)
              
  
if __name__ =="__main__":
        query = ['RailMinIndia','rail minister','suresh prabhu','northern railways']
        kafka = KafkaClient("localhost:9092")
        producer = KafkaProducer(bootstrap_servers='localhost:9092')
        l = StdOutListener(bearer_token=bearer_token)
        for term in query:
                l.add_rules(tweepy.StreamRule("(@RailwaySeva) lang:en -is:retweet", None, None))
    #    auth = OAuthHandler(consumer_key, consumer_secret)
     #   auth.set_access_token(access_token, access_token_secret)
     #   api=tweepy.API(auth,wait_on_rate_limit=True)
        #stream = Stream(auth, l)
        #tweets = client.search_recent_tweets(query=query, max_results=10)
        l.filter(tweet_fields=["referenced_tweets"])

