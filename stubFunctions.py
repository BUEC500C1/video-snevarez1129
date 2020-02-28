import random

def generateResponse(tweetInfo):
    response = {"twitter handle": tweetInfo[0], "tweet": tweetInfo[1], "date": tweetInfo[2], "likes": tweetInfo[3]} #format the api response
    return response

def getTweets(handle):

    #search for the twitter handle
    #get hard coded tweet info including the tweet, date, and the number of likes

    if handle == "busnowtm":
        tweet = "Are you all ready for a great season? Make sure you check out our table at Splash this Saturday to get information about the upcoming season! See you then!"
        date = "Sep 5, 2018"
        likes = 2
        tweetInfo = [handle, tweet, date, likes]
        return tweetInfo
    elif handle == "CNN":
        tweet = "Researchers have discovered a new type of lion, the size of a domestic cat, with powerful flesh-cutting teeth, which roamed the earth around 24 million years ago."
        date = "Feb 28, 2020"
        likes = 739
        tweetInfo = [handle, tweet, date, likes]
        return tweetInfo
    elif handle == "cnni":
        tweet = "A flat bed in economy? This airline wants to make it happen: https://cnn.it/2VsAqIg"
        date = "Feb 27, 2020"
        likes = 134
        tweetInfo = [handle, tweet, date, likes]
        return tweetInfo
    elif handle == "realDonaldTrump":
        tweet = "Big Rally in the Great State of South Carolina on Friday. See you there!"
        date = "Feb 26, 2020"
        likes = "89.9K"
        tweetInfo = [handle, tweet, date, likes]
        return tweetInfo

def getHandle():
    availableHandles = ["busnowtm", "CNN", "cnni", "realDonaldTrump"] #list of hard coded twitter handles
    idx = random.randrange(0, 3, 1) #pick one of the handles
    return availableHandles[idx] #return the chosen handle

class stubFuncs():

    def __init__(self):
        pass

    def noKeys(self):
        twitter_handle = getHandle() #get one of the save twitter handles
        tweets = getTweets(twitter_handle) #get tweets for the twitter handle
        resp = generateResponse(tweets) #generate hardcoded response
        return resp
