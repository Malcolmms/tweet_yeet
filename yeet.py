# welcome to tweet-yeet – lets yeet those tweets!
from datetime import datetime, timedelta
import tweepy

class YeetObject:
    def __init__(self, consumer_key, consumer_secret, access_token, access_token_secret):
        self.consumer_key = consumer_key


    # api info
    # consumer_key = 'XXXXXXXX'
    # consumer_secret = 'XXXXXXXX'
    # access_token = 'XXXXXXXX'
    # access_token_secret = 'XXXXXXXX'
    def authenticate(self, consumer_key, consumer_secret, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

    # set cutoff date
    cutoff_date = datetime.utcnow() - timedelta(days=days_to_keep)

    # delete tweets
    def delete_tweets(self, delete_tweets):
        if delete_tweets:
            timeline = tweepy.Cursor(api.user_timeline).items()
            deletion_count = 0
            for tweet in timeline:
                if tweet.created_at < cutoff_date:
                    api.destroy_status(tweet.id)
                    deletion_count += 1
            print(deletion_count, "tweets have been deleted.")

    # delete favorites / retweets
    def delete_favs(self, delete_favs):
        if delete_favs:
            favorites = tweepy.Cursor(api.favorites).items()
            deletion_count = 0
            for tweet in favorites:
                if tweet.created_at < cutoff_date:
                    api.destroy_status(tweet.id)
                    deletion_count += 1
            print(deletion_count, "favorites have been deleted.")

    def censor(self, censor):
        if censor:
            favorites = tweepy.Cursor(api.favorites).items()
            timeline = tweepy.Cursor(api.user_timeline).items()
            censor_word = input("Input the word you would like to censor here and hit enter: ")
            for favorite in favorites:
                if censor_word in favorite:
                    api.destroy_status(favorite.id)
            for tweet in timeline:
                if censor_word in tweet:
                    api.destroy_status(tweet.id)
            print(censor_word, "is a bad word")