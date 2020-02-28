from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

import datetime
import os
import requests
import subprocess
import textwrap

class ffmpeg_api():

    def __init__(self):
        pass #do nothing, just create object

    def createImage(self, twitter_handle, profile_pic_url, tweet, count):

        txt = tweet.text #get the text from the tweet

        myBackground = Image.new('RGBA', (1024, 512), (255, 75, 75, 200)) #create a background for the image
        handleFont = ImageFont.truetype(r'font/Comic Sans MS.ttf', 30) #create the font for the handle
        tweetFont = ImageFont.truetype(r'font/Comic Sans MS.ttf', 16) #create the font for the tweet

        info = requests.get(profile_pic_url) #get the profile picture info
        twitterImg = Image.open(BytesIO(info.content)) #create the image
        myBackground.paste(twitterImg, (75, 150)) #paste the profile picture image on the background

        myDrawing = ImageDraw.Draw(myBackground) #create drawing
        myDrawing.text((150, 150), '@'+twitter_handle, font=handleFont, fill="white") #write twitter handle on the drawing
        lines = textwrap.wrap(txt, width=100) #define size of a line
        x = 75 #x coord for start of text
        y = 250 #y coord for start of text
        for line in lines:
            myDrawing.text(((x), y), line, font=tweetFont, fill="white") #write tweet on the drawing
            y += 30 #move to next line
        
        #save the final image in the images folder
        myBackground.save('./images/' + str(twitter_handle) + str(count) + '.png')

    def createVideo(self, twitter_handle):        
        try:
            #launch a subprocess to create the video using the images created
            subprocess.call(['/usr/local/bin/ffmpeg', '-y', '-r', '1/3', '-i', './images/'+twitter_handle+'%d.png', '-pix_fmt', 'yuv420p', '-r',
            '25', '-loglevel', 'error', '-hide_banner', twitter_handle + '_twitter_feed.mp4'],
            stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
            print("Video created!")
        except Exception as e:
            print("Uh oh, looks like there was an error creating the video")
            print(e)
        return
