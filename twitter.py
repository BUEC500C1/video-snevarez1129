import tweepy
import configparser

class twitter_scraper():

    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path)
        auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
        auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_token_secret').strip())
        self.api = tweepy.API(auth)

    def tweets(self, handle):
        try:
            tweet = self.api.user_timeline(screen_name = handle, count = 5, include_rts = True, result_type = "recent", include_entities = True, tweet_mode = 'extended', lang = "en")
            return tweet
        except tweepy.error.TweepError as e:
            print(e)
            return ""
