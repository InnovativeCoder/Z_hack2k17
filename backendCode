import tweepy
from textblob import TextBlob
import apiai
import json
import requests
APIAI_ACCESS_TOKEN = "65660d7b382b44a997f9d63986395fbb"

ai = apiai.ApiAI(APIAI_ACCESS_TOKEN)


# # Step 1 - Authenticate
consumer_key= 'c1brEaGQNc9zlNxvk5yeeyBWk'
consumer_secret= 'EDqnXIpPgtVTkdDFdigmyU6Rw1hpMVh43RpozCyGRsdjLwtpM4'


access_token='898281086941241344-CcVXFQuUMw7W4pK5g1vFbdsZcFb0GbQ'

access_token_secret='N1EP1DAOPB6vr99NvQUK6mUJotDHKIlwHvmAgS6Cg1k2R'


token='898281086941241344-CcVXFQuUMw7W4pK5g1vFbdsZcFb0GbQ'

token_secret='N1EP1DAOPB6vr99NvQUK6mUJotDHKIlwHvmAgS6Cg1k2R'




auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets

public_tweets = api.search('spider',count=5)

public_tweets = pd.Dataframe(public_tweets)
count=0

# for tweet in public_tweets:
#     textInside=tweet.text
#     print(tweet.user.screen_name)
#     print ('tweeted');
#     print(textInside);


		


def apiai_response(query, session_id):
	"""
	function to fetch api.ai response
	"""
	request = ai.text_request()
	request.lang='en'
	request.session_id=session_id
	request.query = query
	response = request.getresponse()
	return json.loads(response.read().decode('utf8'))


def parse_response(response):
	"""
	function to parse response and 
	return intent and its parameters
	"""
	result = response['result']
	params = result.get('parameters')
	intent = result['metadata'].get('intentName')
	return intent, params

	
def fetch_reply(query, session_id):
	"""
	main function to fetch reply for chatbot and 
	return a reply dict with reply 'type' and 'data'
	"""
	response = apiai_response(query, session_id)
	intent, params = parse_response(response)
	print (params)
	if (params['currency']!=''):
		print params['currency']
	if(params['geo-country']==''):
		print "COUNtry not found"
	reply = {}

	# if intent == None:
	#   reply['type'] = 'none'
	#   reply['data'] = "I didn't understand"


	if intent == "spider" or intent=="tarantula":
		print ("some thing found")
		
	return reply


print(fetch_reply('tarantula in sale USA rupees pm', 12))

# for tweet in public_tweets:
#     print(tweet.text)
#     ans = fetch_reply(tweet.text,12)
#     print(ans)
