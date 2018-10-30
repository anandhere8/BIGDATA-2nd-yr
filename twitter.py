from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from kafka import SimpleProducer, KafkaClient

access_token = "1056489607385280512-Mxz6q9MQ3lTd4qqSiHtfuHZ1Zq7DD8"
access_token_secret =  "UmVU6mPV3MSHlo8MoIAp2JXIYqc8Rxc0U55n0N3bKcqnT"
consumer_key =  "Ae5SNnc0Ar6hPrvRdBtXIbSy4"
consumer_secret =  "Fb5ucvcockEIFNCwB5VpHDdTulGF9XrMqj02txewkV1yUivgiq"

class StdOutListener(StreamListener):
    def on_data(self, data):
        producer.send_messages("trump", data.encode('utf-8'))
        print (data)
        return True
    def on_error(self, status):
        print (status)

kafka = KafkaClient("localhost:9092")
producer = SimpleProducer(kafka)
l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
stream.filter(track="trump")
