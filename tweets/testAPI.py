from .twitterAPIRunner import getTweetsByUserName
import json,tweepy


tweetResponse = getTweetsByUserName("nytimes")['data']


for key in tweetResponse:
    print(key['text'])
    

  

