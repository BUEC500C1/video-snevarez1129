import queue
import twitter

if __name__ == '__main__':
    #requests = queue.Queue(maxsize=4) #create a queue for image creation requests
    twitter = twitter.twitter_scraper("keys")
    print(twitter)
