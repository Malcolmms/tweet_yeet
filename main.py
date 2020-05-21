# welcome to tweet-yeet – lets yeet those tweets!
from datetime import datetime, timedelta
import tweepy
from yeet import YeetObject

if __name__ == "__main__":

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

    key = input()

    yeet = YeetObject(key, )
    yeet.delete_tweets()