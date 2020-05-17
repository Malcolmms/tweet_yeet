# welcome to tweet-yeet – lets yeet those tweets!
from datetime import datetime, timedelta
import tweepy


# sets options from command line using input functions
delete_tweets = input("would you like to delete tweets before a certain date? (Y/N)")
if delete_tweets.lower == "y":
    delete_tweets = True 
else: 
    delete_tweets = False

delete_favs = input("would you like to delete favorites before a certain date? (Y/N)")
if delete_favs.lower == "y":
    delete_favs = True 
else: 
    delete_favs = False

censor= input("Would you like to censor a certain word from tweets and favorites? (Y/N)")
if censor.lower == "y":
    censor = True 
else: 
    censor = False

# sets time limit 
if delete_tweets or delete_favs == True:
    days_to_keep = input("Input the number of days of tweets you would like to keep as a numeral (0, 7, 249 etc.). Tweets/favs older than this will be deleted ")

# api info
consumer_key = 'XXXXXXXX'
consumer_secret = 'XXXXXXXX'
access_token = 'XXXXXXXX'
access_token_secret = 'XXXXXXXX'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# set cutoff date
cutoff_date = datetime.utcnow() - timedelta(days=days_to_keep)

# delete tweets
if delete_tweets:
    timeline = tweepy.Cursor(api.user_timeline).items()
    deletion_count = 0
    for tweet in timeline:
        if tweet.created_at < cutoff_date:
            api.destroy_status(tweet.id)
            deletion_count += 1
    print(deletion_count, "tweets have been deleted.")

# delete favorites / retweets
if delete_favs:
    favorites = tweepy.Cursor(api.favorites).items()
    deletion_count = 0
    for tweet in favorites:
        if tweet.created_at < cutoff_date:
            api.destroy_status(tweet.id)
            deletion_count += 1
    print(deletion_count, "favorites have been deleted.")

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