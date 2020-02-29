# video-snevarez1129

Introduction:

For this project, I created an API that would get a user's twitter feed and create a video of their timeline. To access twitter, I used tweepy api; I used pillow api to convert tweets into images; I used FFMPEG to combine the images into a video.

How to Run:

To create my API I used Flask framework, so to call the api first run the file, api.py on your machine. In a new terminal window, run the command
    curl http://127.0.0.1:5000/<twitter_handle>
The API uses a file called "keys" in the root directory of the project. This file contains the autentication keys to use Twitter to get tweets. If no keys are available, the program runs a series of stub functions that return hard coded data. For my stub functions, I selected 4 Twitter users that are selected at random each time an API call is made and returns a hard coded tweet made by that user.
