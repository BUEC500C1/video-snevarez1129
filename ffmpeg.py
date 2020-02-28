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

    def createImage(self, twitter_handle, profile_pic, tweet, count):

        txt = tweet.text #get the text from the tweet

        background = Image.new('RGBA', (1024, 768), (255, 75, 75, 255)) #create the background, a nice red color
        font = ImageFont.truetype(r'font/Comic Sans MS.ttf', 16) #create the font for the text

        response = requests.get(profile_pic) #get the profile picture info
        img = Image.open(BytesIO(response.content)) #create the image

        draw = ImageDraw.Draw(background)
        background.paste(img, (50, 150)) #paste the profile picture image on the background

        #create twitter tweet text wrapped
        lines = textwrap.wrap(txt, width=120)
        x, y = 50, 225
        for line in lines:
            draw.text(((x), y), line, font=font, fill="white")
            y += 25
        draw.text((120, 170), twitter_handle, font=font, fill="white")
        
        #draw final image with tweet and user profile, etc
        background.save('./processed_imgs/' + str(twitter_handle) + str(count) + '.png')

    def createVideo(self, twitter_handle):
        return
