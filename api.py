from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import ffmpeg as ff
import stubFunctions as stubs
import twitter as twi

import glob
import os
import os.path
import queue
import requests
import threading
import time

app = Flask(__name__)
api = Api(app)

def videoProcessor(handles, ffm):
    while(True):
        twitter_handle = handles.get() #get a twitter handle from the queue
        if twitter_handle is not None: #if there is a twitter handle in the queue
            png_count = len(glob.glob1(r"images/", twitter_handle + r"*.png")) #check how many images are in the folder
            if png_count < 20: #if there are less than 20 images, add the handle back to the queue
                handles.put(twitter_handle)
            else: #if there are enough images to create a video
                ffm.createVideo(twitter_handle) #create a video
        handles.task_done()
        time.sleep(0.5) #sleep for half a second

def tweetsToPics(tweets, f):
    while(True):
        nextTweet = tweets.get() #get the next tweet to convert to an image
        if nextTweet is not None: #if there is a tweet to convert
            f.createImage(nextTweet[0], nextTweet[1], nextTweet[2], nextTweet[3]) #convert tweet to an image
            #0 = handle, 1 = profile pic, 2 = tweet, 3 = count
        tweets.task_done()
        time.sleep(0.5) #sleep for half a second

def addTweets(tweetsQ, twitter_handle, profilePic, profileTweets):
    for count, tweet in enumerate(profileTweets): #create an image conversion request for each tweet
        tweetsQ.put([twitter_handle, profilePic, tweet, count]) #add the request to the queue
    tweetsQ.join() #block until all tweets have been turned into images

class Video(Resource):

    def get(self, twitter_handle):
        print("Let's begin")
        
        try:
            t = twi.twitter_api("keys") #get twitter keys from keys file
        except:
            print("No keys available!")
            s = stubs.stubFuncs() #create an object for stubs, these will be run if there are no keys available
            resp = s.noKeys()
            return resp

        f = ff.ffmpeg_api() #create an ffmpeg object

        handles = queue.Queue() #create queue to hold twitter handles in the order the handle called the api
        tweets = queue.Queue() #create queue to hold tweets in the order they were tweeted by each handle

        handles.put(twitter_handle) #add twitter handle to queue
        profilePic = t.get_profilePic(twitter_handle) #get the users profile picture
        profileTweets = t.get_tweets(twitter_handle) #get the users tweets

        #addTweets(tweets, twitter_handle, profilePic, profileTweets)
        #thread to add tweets to tweets queue to create images in chronological order of the tweets
        t = threading.Thread(name="producer", target=addTweets, args=(tweets, twitter_handle, profilePic, profileTweets))
        t.start()

        #tweetsToPics(tweets, f)
        #thread to convert tweets to images
        t = threading.Thread(name="imageConverter", target=tweetsToPics, args=(tweets, f))
        t.start()

        #videoProcessor(handles, f)
        #thread to convert the images to a video
        t = threading.Thread(name="videoCreator", target=videoProcessor, args=(handles, f))
        t.start()
        
        resp = {"file location": os.getcwd() + '/' + twitter_handle + '_' + r'twitter_feed.mp4'} #create json response for api call
        return resp

#Resources
api.add_resource(Video, '/<twitter_handle>')

if __name__ == '__main__':
    app.run()
