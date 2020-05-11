import tweepy
import time

#insert consumer key, consumer_secret, key, and secret from developer twitter account
consumer_key = '_'
consumer_secret = '_'
key = '_'
secret = '_'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)

file_name = 'last_seen.txt'

def read_last_seen(file_name):
    file_read = open(file_name, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(file_name, last_seen_id):
    file_write = open(file_name, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

def reply():
    tweets = api.mentions_timeline(read_last_seen(file_name), tweet_mode='extended')
    for tweet in reversed(tweets):
        if '#brogroup' in tweet.full_text.lower():
            print(str(tweet.id) + '-' + tweet.full_text)
            api.update_status("@" + tweet.user.screen_name + " Auto reply, like, and retweet work :)", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            store_last_seen(file_name, tweet.id)

while True:
    reply()
    time.sleep(15)






