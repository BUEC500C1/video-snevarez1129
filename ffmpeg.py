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
        myBackground.paste(twitterImg, (475, 210)) #paste the profile picture image on the background

        #write twitter handle and tweet on the background
        draw = ImageDraw.Draw(myBackground)
        draw.text((425, 150), '@'+twitter_handle, font=handleFont, fill="white")
        lines = textwrap.wrap(txt, width=120)
        x = 50
        y = 300
        for line in lines:
            draw.text(((x), y), line, font=tweetFont, fill="white")
            y += 25
        
        #save the final image in the images folder
        myBackground.save('./images/' + str(twitter_handle) + str(count) + '.png')

    def createVideo(self, twitter_handle):
        currentDate = str(datetime.date.today()).replace('-', '_') #get the current date to add it to the output video name
        
        try:
            subprocess.call(['/usr/local/bin/ffmpeg', '-y', '-r', '1/3', '-i', './images/'+twitter_handle+'%d.png', '-pix_fmt', 'yuv420p', '-r',
            '25', '-loglevel', 'error', '-hide_banner', twitter_handle + '_twitter_feed_' + currentDate + '.mp4'],
            stdout=subprocess.DEVNULL, stdin=subprocess.DEVNULL) #launch a subprocess to create the video using the images created
            print("Finished creating video! File at " + os.getcwd() + '/' + twitter_handle + '_' + r'/twitter_feed_' + currentDate + '.mp4')
        except Exception as e:
            print("Uh oh, looks like there was an error creating the video")
            print(e)
        
        return
