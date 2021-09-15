import json,tweepy
from .wordsCalc import calcScoreForTweet 



#*********keys removed for public demo *****

# Save the credentials object to file
import requests
import os
import json 

# To set your enviornment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'


def auth():
    return bearer_token
    #return os.environ.get("BEARER_TOKEN")


def create_url(user):
    if user :
        query = "from:"+ user +" -is:retweet " #-is:reply
    else: 
        query = "from:"+ "nytimes" +" -is:retweet " #-is:reply

    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    tweet_fields = "tweet.fields=author_id"
    url = "https://api.twitter.com/2/tweets/search/recent?query={}&{}".format(
        query, tweet_fields
    )
    return url


def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers


def connect_to_endpoint(url, headers):
    response = requests.request("GET", url, headers=headers)
    print(response.status_code)
    if response.status_code != 200:
        #raise Exception(response.status_code, response.text)
        return "throwError"
    else:
        return response.json()


def main():
    getTrendTopics()

def extractTweetText(json_response):
    
    listOfTweets = []
    if json_response['meta']['result_count'] == 0 : 
        listOfTweets.append(["No Recent Tweets" , 0])
        return listOfTweets
    
    for i in json_response['data']:
        tweetText = i['text']
        score = calcScoreForTweet(tweetText)*10
        listOfTweets.append([tweetText , score])

    return listOfTweets

def getTrendTopics():
    bearer_token = auth()

    url = "https://api.twitter.com/1.1/trends/place.json?id=23424977"
    headers = create_headers(bearer_token)
    json_response = connect_to_endpoint(url, headers)
    trendArr = []
    length = len(json_response[0]['trends']);
    if length > 5:
        length = 5
    for i in range(length):

        trendArr.append(json_response[0]['trends'][i]['name'])
    trendArr.append("Trending Topics")
    for i in range(length):

        trendArr.append(json_response[0]['trends'][i]['name'])
    for i in trendArr:
        print(i)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    return (trendArr) 

    
def getTweetsByUserName(username):
        bearer_token = auth()
        
        url = create_url(username)

        headers = create_headers(bearer_token)
        json_response = connect_to_endpoint(url, headers)
        

        if json_response == "throwError":
            return "throwError"
            
        else: 
            return extractTweetText(json_response) 


if __name__ == "__main__":
    getTrendTopics()