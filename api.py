from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

import ffmpeg as ff
import twitter as twi

import glob
import os
import os.path
import queue
import requests
import time

app = Flask(__name__)
api = Api(app)

def videoProcessor(hndls, ffm):
    return

def imageProcessor(reqs, ffm):
    count = 0
    while(count < 5):
        count = count + 1
        currReq = reqs.get() #get the next image request
        if currReq is not None:
            #only do this if the request grabbed is not empty
            #0 = handle, 1 = profile pic, 2 = tweet, 3 = count
            ffm.createImage(currReq[0], currReq[1], currReq[2], currReq[3])
        #reqs.task_done() #decrement the count of incompleted requests
        #time.sleep(0.001) #sleep for 0.001 seconds
    return

def createRequest(reqs, item):
    for count, tweet in enumerate(item[2]): #create an image conversion request for each tweet
        reqs.put([item[0], item[1], tweet, count])
    #reqs.join() #block until all items in the queue have been gotten and processed

class Video(Resource):

    def get(self, twitter_handle):

        print("Let's begin")
        t = twi.twitter_api("keys") #get twitter keys from keys file
        f = ff.ffmpeg_api() #create an ffmpeg object

        handles = queue.Queue() #queue to hold twitter handles in the order the handle called the api
        tweets_to_convert = queue.Queue() #queue to hold tweets that need to be converted to an image

        handles.put(twitter_handle) #add twitter handle to queue
        profilePic = t.get_profilePic(twitter_handle) #get the users profile picture
        profileTweets = t.get_tweets(twitter_handle) #get the users tweets

        qItem = [twitter_handle, profilePic, profileTweets] #group twitter_handle, profile picture, and tweets together
        createRequest(tweets_to_convert, qItem) #create image requests for each tweet and store them in the queue
        imageProcessor(tweets_to_convert, f) #convert tweets to images
        videoProcessor(handles, f) #convert the images to a video
        return {'hello': 'world'}

#Resources
api.add_resource(Video, '/<twitter_handle>')

if __name__ == '__main__':
    app.run()
