import requests
import dotenv

hf_bearer_token = dotenv.get_key(dotenv.find_dotenv(), "HF_BEARER_TOKEN")

headers = {"Authorization": hf_bearer_token}

# API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis" --> less robust model, doesn't accept long reviews

# more robust model
API_URL = "https://api-inference.huggingface.co/models/distilbert/distilbert-base-uncased-finetuned-sst-2-english" 

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


array = [
	"Switching to CNG has been one of the best decisions I’ve made for my vehicle. The cost savings are immediately noticeable, with my fuel expenses dropping significantly compared to traditional gasoline. I also love how eco-friendly it is, knowing that I’m contributing to a cleaner environment by using a fuel source with lower emissions. Refueling is straightforward, and the increasing number of CNG stations means I’ve never had to worry about running out of gas. My car’s performance has remained steady, and I haven’t noticed any loss in power, even during long highway drives. The trunk space taken up by the CNG tank is a small sacrifice for the benefits I’m getting. I also appreciate the quieter engine operation when using CNG. Overall, I’m very satisfied with the switch and highly recommend it to anyone looking for an affordable and sustainable fuel option. It’s an investment in both the planet and my wallet!"
]

	

output = query({
	"inputs": array[0],
})


# output for more robust model
label = output[0][0]['label']

print(label)




























# import requests
# from bs4 import BeautifulSoup

# url = 'https://api.x.com/1.1/search/tweets.json?q=nasa&result_type=popular&count=3'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')

# for post in soup.find_all('div', class_='post'):
#     content = post.find('p').text
#     print(content)





























# import tweepy

# # Authenticate with the Twitter API
# bearer_token = "YOUR_BEARER_TOKEN"
# client = tweepy.Client(bearer_token="riP0pAiohpMXxMBeI9ZoF9ZWM")

# # Define your search query
# query = 'CNG'

# # Make a request with a limit of 10 tweets
# response = client.search_recent_tweets(query=query, max_results=10)

# # Print the tweets
# for tweet in response.data:
#     print(tweet.text)
























# import tweepy
# import pandas as pd

# consumer_key = "5fIO2xdnHeOo8CXrnYggCG5I2" #Your API/Consumer key 
# consumer_secret = "IfNqMyzVRDoFYEkPigp6N5QMA5p57751zS8f2UeM9DP0NCDW5Z" #Your API/Consumer Secret Key
# access_token = "1274846586699501568-3pcsUWF9Tr4vlAmNqw1OHsmVybtgF9"    #Your Access token key
# access_token_secret = "k1S8TXYlCSX2OYm55MSMsNiWZSmdyfKCqvDC32yXIVwG1" #Your Access token Secret key

# #Pass in our twitter API authentication key
# auth = tweepy.OAuth1UserHandler(
#     consumer_key, consumer_secret,
#     access_token, access_token_secret
# )

# #Instantiate the tweepy API
# api = tweepy.API(auth, wait_on_rate_limit=True)


# search_query = "'ref''world cup'-filter:retweets AND -filter:replies AND -filter:links"
# no_of_tweets = 10

# try:
#     #The number of tweets we want to retrieved from the search
#     tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode ='extended')
    
#     #Pulling Some attributes from the tweet
#     attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

#     #Creation of column list to rename the columns in the dataframe
#     columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
#     #Creation of Dataframe
#     tweets_df = pd.DataFrame(attributes_container, columns=columns)
# except BaseException as e:
#     print('Status Failed On,',str(e))

# import requests
# import pandas as pd

# twitter_data = []

# payload = {
# 	'api_key': '71ead23e5d5d950767e343fe02ab4118',
# 	'query': 'CNG',
# 	'num': '3',
# }

# response = requests.get(
# 	'https://api.scraperapi.com/structured/twitter/search', params=payload
# )

# data = response.json()


# import requests
# from bs4 import BeautifulSoup

# # URL of the Twitter page or specific tweet
# url = "https://twitter.com/PCNGInitiative/status/1844663570375553492"

# r = requests.get(url)

# soup =  BeautifulSoup(r.text, "lxml")
# tag = soup.span

# print(tag)



# # Loop through the 'organic_results' list to access each dictionary
# for result in data['organic_results']:
#     # Print the 'snippet' field of each dictionary
#     print({"Snippet:": result['snippet'],
# 	"Link to full tweet:": result['link']})
