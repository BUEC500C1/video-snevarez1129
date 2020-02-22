import queue
import twitter as t

def userInfo():
    while(True):
        handle = input("Please enter your twitter handle: ")
        if handle == '':
            print("Please enter a valid twitter handle")
        else:
            return handle

if __name__ == '__main__':
    
    print("Let's begin")
    #requests = queue.Queue(maxsize=4) #create a queue for image creation requests

    t = t.twitter_scraper("keys") #get twitter keys from keys file in root directory
    print(t)

    twitt_hand = userInfo() #get the user info to start getting their tweets
    los_tweets = t.tweets(twitt_hand) #get the tweets
    print(los_tweets)
