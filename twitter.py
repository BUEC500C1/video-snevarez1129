import tweepy
import configparser

class twitter_scraper():

    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path)
        auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
        auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_token_secret').strip())
        self.api = tweepy.API(auth)
