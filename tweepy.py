import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key = 'WAHM8zyTCjHLyrFmdJ1BRBOFc'        #consumerkey string located in twitter apps
consumer_secret = 'Mqzu3XRWFYpTLxcLURidTXOQSTfJrADt5YyI9LTqYfF85GwBUx'    # consumer secret string located in twitter apps

access_token = '2388991603-1y8M2Aihmvsfvpou72EGuG1pb18uGoQhYbqXH0h'       # access token genrated in twitter apps
access_token_secret = 'IsldJ4CPVZINPxzzv5h23DuBGruxuayffVrbDmWtW655Y'    #access token secret genrated in twitter apps

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets

public_tweets = api.search('anabelle',count=1000)

#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself

count=0

for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
    count=count+1


print (count)