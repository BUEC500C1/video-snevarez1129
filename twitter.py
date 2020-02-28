import configparser
import tweepy

class twitter_api():

    def __init__(self, path):
        config = configparser.ConfigParser()
        config.read(path)
        auth = tweepy.OAuthHandler(config.get('auth', 'consumer_key').strip(), config.get('auth', 'consumer_secret').strip())
        auth.set_access_token(config.get('auth', 'access_token').strip(), config.get('auth', 'access_token_secret').strip())
        self.api = tweepy.API(auth)

    def get_profilePic(self, handle):
        try:
            profile = self.api.get_user(handle)
            return profile.profile_image_url_https
        except tweepy.error.TweepError as e:
            print(e)
            return ""

    def get_tweets(self, handle):
        try:
            tweets = self.api.user_timeline(screen_name=handle, count=20)
            return tweets
        except tweepy.error.TweepError as e:
            print(e)
            return ""
