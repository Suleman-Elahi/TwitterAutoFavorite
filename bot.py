#!/usr/bin/env python
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
twt = api.search("#Salvatore",result_type="mixed",count=5) 
 
for s in twt:
    api.create_favorite(s.id)
    print(s.id)
print("Done!!!")
