# video-snevarez1129

## Introduction

Using the twitter feed, construct a daily video summarizing a twitter handle day
* Convert text into an image in a frame
* Do a sequence of all texts and images in chronological order.
* Display each video frame for 3 seconds

## Assignment Questions

How many API calls you can handle simultaneously and why?
* Given that my machine has an 8-core processor, it should handle 8 simultaneous API calls.

For example, run different API calls at the same time?
* This API can run more than one API call at the same time.

Split the processing of an API into multiple threads?
* This API was split into 2 threads, one to create images and one to create videos.

## Using the API

(1) Set Up Python Virtual Environment

`python3 -m venv env`
`source env/bin/activate`

(2) Install Requirements

`pip3 install -r requirements.txt`

(3) Start the Server

`python3 api_dev.py`

(4) Run the API

`curl http://127.0.0.1:5000/<twitter_handle>`

# API Response
This API creates a video of a twitter handle and stores the video in the root directory. If no API keys are availabe, the API returns a saved tweet from one of four hard coded handles. The API response lets the user know whether a video was create - and where it was saved - or one of the saved tweets.
