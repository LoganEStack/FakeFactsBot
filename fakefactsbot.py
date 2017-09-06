import praw
import tweepy
import time

#Create an instance of Reddit
reddit = praw.Reddit(user_agent='Comment Extraction (by /u/cyanitee)',
                     client_id='ZVYUyIJZF2hq6A', client_secret="9qD_rpx1rUZmY2jEGwf3js20hfo",
                     username='', password='')

#Obtain the submission ID of the /r/askreddit post                     
submission1 = reddit.submission(id='61jz5t')
submission2 = reddit.submission(id='1r6hwg')
submission3 = reddit.submission(id='5f30kk')

#Establish a twitter account connection
consumer_key = 'Pe5fNAYacrqF9leyFUkbRg44n'
consumer_secret = '1xCdoNdZHkbIXEBV71V9aufmcyUS3lq0rr9sGDTWLIUMKfrYCE'
access_token = '905167617509478400-kLDMQTUSfCXf1EEV0XMZ8XnFW8h6tMu'
access_token_secret = 'O8HjQ2H2abEblsi27dLlA2StUeM3Iomfm7RgamWS4Y7Pn'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Iterates through all parent comments in the post
submission1.comments.replace_more(limit=0)
for top_level_comment in submission1.comments:
    #if the comment does not exceed twitter's 140 char limit
    if len(top_level_comment.body) <= 140:
        #if the comment hasn't been deleted and doesn't start with 'I' or 'Edited'
        #   for filtering purposes
        if (top_level_comment.body not in ["[deleted]", "[removed]"] and 
            top_level_comment.body[:2] != "I " and top_level_comment.body[:2] != "Ed"):
            print(top_level_comment.body)
            
            #Update twitter status with a comment every x hours
            api.update_status(top_level_comment.body)
            #Post a new fake fact every hour
            time.sleep(3600)
            
submission2.comments.replace_more(limit=0)
for top_level_comment in submission2.comments:
    #if the comment does not exceed twitter's 140 char limit
    if len(top_level_comment.body) <= 140:
        #if the comment hasn't been deleted and doesn't start with 'I' or 'Edited'
        #   for filtering purposes
        if (top_level_comment.body not in ["[deleted]", "[removed]"] and 
            top_level_comment.body[:2] != "I " and top_level_comment.body[:2] != "Ed"):
            print(top_level_comment.body)
            
            #Update twitter status with a comment every x hours
            api.update_status(top_level_comment.body)
            #Post a new fake fact every hour
            time.sleep(3600)

submission3.comments.replace_more(limit=0)
for top_level_comment in submission3.comments:
    #if the comment does not exceed twitter's 140 char limit
    if len(top_level_comment.body) <= 140:
        #if the comment hasn't been deleted and doesn't start with 'I' or 'Edited'
        #   for filtering purposes
        if (top_level_comment.body not in ["[deleted]", "[removed]"] and 
            top_level_comment.body[:2] != "I " and top_level_comment.body[:2] != "Ed"):
            print(top_level_comment.body)
            
            #Update twitter status with a comment every x hours
            api.update_status(top_level_comment.body)
            #Post a new fake fact every hour
            time.sleep(3600)
