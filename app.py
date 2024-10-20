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
  "CNG is an excellent alternative to petrol and diesel, much cheaper!",
  "The mileage of my CNG car is fantastic, I save so much on fuel costs.",
  "CNG stations are hard to find in my area, which makes it inconvenient.",
#   "I had to convert my vehicle to run on CNG, and it's been worth every penny.",
#   "It’s cleaner than gasoline, so I feel like I'm doing my part for the environment.",
#   "CNG takes up too much space in the trunk with the cylinder.",
#   "Refueling my car with CNG takes longer than filling up with petrol.",
#   "I noticed a slight reduction in engine power after switching to CNG.",
#   "It's much better for the environment, fewer carbon emissions.",
#   "The cost of CNG conversion is quite high, but the savings over time make up for it.",
#   "CNG vehicles tend to have lower maintenance costs.",
#   "I’ve had issues with my engine since switching to CNG, more frequent repairs.",
#   "The availability of CNG refueling stations is improving, which is a relief.",
#   "I like that CNG is a domestic energy source, reducing reliance on imports.",
#   "The range on a full CNG tank is much lower than gasoline.",
#   "CNG burns cleaner, so my engine components last longer.",
#   "Switching to CNG is great for short city commutes but not practical for long-distance travel.",
#   "CNG prices have been quite stable compared to gasoline.",
#   "The initial investment to convert my car to CNG was too high.",
#   "My vehicle’s performance hasn’t changed much since converting to CNG.",
#   "CNG is a much cleaner alternative, reducing pollution levels in urban areas.",
#   "I had a hard time finding a certified mechanic for CNG vehicle maintenance.",
#   "The fuel economy of CNG is amazing, my car runs more efficiently.",
#   "I wish there were more CNG stations on highways, it's inconvenient for road trips.",
#   "CNG is safer in terms of explosion risk compared to petrol.",
#   "The tank takes up too much trunk space, limiting luggage room.",
#   "CNG cars produce less noise compared to diesel vehicles, which is a plus.",
#   "I’ve experienced cold-start problems with my CNG vehicle in the winter.",
#   "My city has introduced more CNG buses, and they emit much less smoke.",
#   "The government should invest more in CNG infrastructure.",
#   "Converting to CNG has reduced my fuel bills significantly.",
#   "There’s no noticeable performance difference when driving with CNG in the city.",
#   "The cylinder inspection requirements for CNG vehicles are a hassle.",
#   "I feel safer driving a CNG car, knowing it has a lower risk of fire in accidents.",
#   "I had to wait a long time to refuel because there were only a few CNG pumps available.",
#   "CNG vehicles are eco-friendly, I hope more people switch to them.",
#   "Refueling with CNG feels slower than with conventional fuels.",
#   "I love how CNG is a more sustainable option for the future.",
#   "CNG tanks make the car heavier, which I don’t like.",
#   "My engine runs quieter on CNG, which I find pleasant.",
#   "The conversion process for CNG was confusing, not enough information available.",
#   "I'm happy with the lower running costs after switching to CNG.",
#   "It’s not easy finding CNG stations in rural areas.",
#   "CNG doesn’t smell as bad as gasoline when refueling, which is nice.",
#   "The loss of power when switching to CNG is minimal, almost unnoticeable.",
#   "I feel good about reducing my carbon footprint with a CNG vehicle.",
#   "CNG cylinders take too long to get inspected and certified.",
#   "The environmental benefits of CNG are huge, less air pollution.",
#   "I had to install a larger gas tank, and now my car’s weight distribution feels off.",
#   "CNG vehicles should have more government incentives to encourage their use.",
#   "The fuel cost savings are significant, but the lack of stations is frustrating.",
#   "It’s a hassle to switch between CNG and gasoline on my bi-fuel vehicle.",
#   "I’ve never had to deal with engine knocking since converting to CNG.",
#   "There’s always a long line at the CNG refueling stations in my area.",
#   "I hope CNG becomes more accessible nationwide.",
#   "The government should regulate CNG prices better to make it more affordable.",
#   "My CNG vehicle is quieter and smoother than it was on gasoline.",
#   "The storage space in my car is now limited because of the CNG tank.",
#   "I’m satisfied with the lower emissions from CNG.",
#   "The conversion kit installation was expensive but worth it in the long run.",
#   "I don’t think CNG is the future, electric vehicles will take over.",
#   "I love how my CNG car is contributing to cleaner air.",
#   "I find the performance slightly reduced when running on CNG compared to petrol.",
#   "There are hardly any CNG stations in rural areas, making it impractical for long trips.",
#   "It’s much cheaper to run a CNG vehicle on a daily basis.",
#   "CNG infrastructure needs to improve, but the benefits are undeniable.",
#   "My car’s acceleration feels a bit sluggish on CNG.",
#   "CNG technology should be more widely adopted by commercial fleets.",
#   "I switched to CNG because it’s the cleaner, greener option.",
#   "I’m still getting used to the refueling process for CNG.",
#   "CNG prices are much more stable than gasoline prices, which helps with budgeting.",
#   "The safety features on CNG tanks are great, I feel confident driving with it.",
#   "The lack of refueling stations in suburban areas is a big problem for CNG users.",
#   "My vehicle’s emissions have dropped significantly since I started using CNG.",
#   "The conversion process was straightforward, no issues so far.",
#   "It’s annoying how long it takes to find a CNG refueling station.",
#   "I love the quiet ride with CNG, it’s much smoother than gasoline.",
#   "CNG cylinders take up too much space in smaller cars.",
#   "The switch to CNG has made my car feel slightly underpowered.",
#   "I don’t have to worry about fuel price fluctuations as much with CNG.",
#   "There are too few CNG stations to make it viable for everyone.",
#   "The reduced emissions from CNG make it worth the switch.",
#   "My car’s performance hasn’t been affected negatively by using CNG.",
#   "The range on CNG isn’t as high as I expected, so I need to refuel more often.",
#   "CNG is a great option for city driving, but not so much for long highway trips.",
#   "The gas station lines for CNG are too long in my area.",
#   "It’s amazing how much cleaner CNG is compared to traditional fuels.",
#   "I’ve had fewer engine problems since I started using CNG.",
#   "The government should provide more subsidies for CNG vehicles.",
#   "It’s a bit inconvenient to plan long trips with a CNG vehicle due to the limited stations.",
#   "CNG is a stepping stone towards a cleaner transportation future.",
#   "The fuel cost savings are incredible with CNG.",
#   "I miss the trunk space I had before the CNG cylinder was installed.",
#   "CNG is good for the environment, but not ideal for every situation.",
#   "My car’s engine runs cooler on CNG, which could extend its life.",
#   "CNG is much cheaper than gasoline, saving me money every month.",
#   "I find it inconvenient that there aren’t enough CNG stations around.",
#   "The environmental benefits of CNG make it a great option.",
#   "CNG conversion for my vehicle was too expensive.",
#   "I love how clean my engine runs after switching to CNG.",
#   "CNG stations need to be more accessible in rural areas.",
#   "My car's performance feels just as good with CNG as with gasoline.",
#   "I had to wait 20 minutes at a CNG station because there were only two pumps.",
#   "CNG provides great mileage for short city drives.",
#   "The CNG tank takes up too much space in my trunk.",
#   "I feel better about my carbon footprint since switching to CNG.",
#   "Refueling with CNG takes too long compared to gasoline.",
#   "The price of CNG has been stable in my area, unlike gasoline.",
#   "There are not enough mechanics that service CNG cars near me.",
#   "I appreciate how quiet my car is after converting to CNG.",
#   "Converting my vehicle to CNG was a waste of money.",
#   "CNG is much better for the environment compared to diesel.",
#   "I’m tired of driving around looking for a CNG station.",
#   "The upfront cost of converting to CNG was high, but it's paying off in fuel savings.",
#   "I haven't noticed any loss in power since switching to CNG.",
#   "The CNG cylinder takes up way too much space in my small car.",
#   "I love how much I save on fuel with CNG.",
#   "There are very few CNG refueling stations in my area.",
#   "CNG reduces emissions, which is why I switched.",
#   "CNG conversion wasn’t worth it because the stations are so far apart.",
#   "It’s great that CNG is both affordable and eco-friendly.",
#   "The maintenance costs for my CNG car are higher than expected.",
#   "My car is quieter and smoother on CNG.",
#   "I wish there were more CNG stations available in rural areas.",
#   "CNG vehicles should have more government incentives.",
#   "CNG is less efficient in the winter, which is annoying.",
#   "I haven’t had any engine issues since converting to CNG.",
#   "It’s a hassle finding CNG stations outside the city.",
#   "I feel safer driving a CNG vehicle because of the reduced explosion risk.",
#   "CNG refueling stations are too far apart in my region.",
#   "The low emissions from CNG make it ideal for city driving.",
#   "I miss the convenience of gasoline because CNG stations are so rare.",
#   "Converting to CNG was the best decision I made for my car.",
#   "The availability of CNG stations has increased in the past year.",
#   "CNG prices are stable, unlike the fluctuating gasoline prices.",
#   "I had a hard time finding a reliable mechanic for my CNG car.",
#   "The fuel economy of CNG is much better than gasoline.",
#   "I don’t notice any difference in performance with CNG.",
#   "There should be more infrastructure for CNG vehicles.",
#   "Refueling with CNG takes longer than gasoline, which is inconvenient.",
#   "CNG is a great fuel option for daily commuting.",
#   "My car's acceleration feels slightly reduced on CNG.",
#   "I feel like I'm doing my part for the environment by using CNG.",
#   "The tank size of CNG cars is frustratingly small.",
#   "CNG stations are popping up more frequently in my area.",
#   "I had to pay too much to convert my car to CNG.",
#   "The range of my car on CNG is shorter than I expected.",
#   "My car has been more reliable since switching to CNG.",
#   "The limited availability of CNG stations makes it hard to rely on.",
#   "CNG refueling stations are finally becoming more common.",
#   "I enjoy the quieter ride that comes with CNG.",
#   "The initial investment in CNG conversion was a bit steep.",
#   "CNG is a reliable alternative to traditional fuels.",
#   "I can’t find a CNG station anywhere near me when I travel.",
#   "It’s nice that CNG reduces harmful emissions.",
#   "CNG is a great option for anyone looking to save on fuel costs.",
#   "The storage capacity for CNG is too small for long road trips.",
#   "I haven’t experienced any performance drop since switching to CNG.",
#   "I wish the government offered more incentives for CNG vehicles.",
#   "CNG is perfect for my short daily commutes around the city.",
#   "I’ve been saving a lot on fuel ever since I converted my car to CNG.",
#   "Refueling with CNG takes longer, but the savings are worth it.",
#   "The cylinder inspection requirements for CNG are annoying.",
#   "I wish there were more CNG stations on highways.",
#   "CNG is much safer than gasoline in case of an accident.",
#   "The maintenance for my CNG car is lower compared to when I used gasoline.",
#   "It’s inconvenient to switch between gasoline and CNG on a bi-fuel car.",
#   "The initial cost of converting to CNG was higher than I expected.",
#   "CNG cars are ideal for reducing urban pollution.",
#   "I’ve had issues with cold starts in the winter with my CNG vehicle.",
#   "CNG is the future of affordable, clean transportation.",
#   "The CNG stations in my area are too crowded.",
#   "I enjoy the peace of mind that comes with using CNG.",
#   "My engine runs cleaner on CNG, which is great for its longevity.",
#   "I don’t like how long it takes to refuel with CNG.",
#   "CNG is available at more gas stations than before.",
#   "I have saved a significant amount of money using CNG.",
#   "The fuel savings with CNG make it worth the initial investment.",
#   "The lack of trunk space in CNG vehicles is a big downside.",
#   "CNG stations should be more widespread.",
#   "I haven’t seen any significant performance issues with CNG.",
#   "I’m happy to reduce my carbon footprint with a CNG car.",
#   "CNG tanks take up too much space in the car.",
#   "The range of a CNG car is smaller than I thought.",
#   "I don’t mind refueling with CNG because it's much cheaper.",
#   "I had trouble finding a station when traveling out of town.",
#   "CNG prices have been stable compared to gasoline.",
#   "The space taken up by the CNG tank in my trunk is too much.",
#   "CNG refueling stations are too far apart for long road trips.",
#   "I’m happy with the environmental benefits of using CNG.",
#   "There should be more CNG refueling stations in the suburbs.",
#   "CNG has made my car quieter and smoother to drive.",
#   "I’m glad I switched to CNG, the fuel savings are significant.",
#   "I don’t like how much space the CNG tank takes up in my car.",
#   "I’m disappointed by how few CNG stations there are.",
#   "CNG helps me save a lot of money on fuel.",
#   "The conversion to CNG wasn’t as expensive as I thought.",
#   "The limited CNG refueling options make it tough to plan trips.",
#   "I haven’t had any engine trouble since switching to CNG.",
#   "CNG is great for city driving but not practical for long trips.",
#   "The government needs to offer more support for CNG infrastructure.",
#   "I’ve saved a lot on fuel costs by switching to CNG.",
#   "CNG is a cleaner alternative to gasoline.",
#   "The lack of CNG stations in rural areas is frustrating.",
#   "I love that CNG is both affordable and eco-friendly.",
#   "I have to refuel more often with CNG, which is annoying.",
#   "CNG makes my engine run quieter, which I enjoy.",
#   "It’s great that CNG is reducing my emissions footprint.",
#   "There are too few CNG stations on highways.",
#   "CNG is a reliable fuel option for my daily commute.",
#   "The storage capacity of CNG tanks is too small.",
#   "CNG refueling takes a bit longer, but the cost savings are worth it.",
#   "CNG should be available in more rural areas.",
#   "The performance of my car hasn't changed much since I switched to CNG.",
#   "CNG prices are much more stable than gasoline prices.",
#   "I can’t find CNG stations easily when I leave the city.",
#   "I’m happy with the fuel savings since converting to CNG.",
#   "CNG makes my engine run more efficiently.",
#   "The infrastructure for CNG needs to improve, but it’s getting better.",
#   "I’ve been able to save a lot on fuel by using CNG.",
#   "CNG stations are still too scarce in rural regions.",
#   "I like how much cleaner CNG is compared to traditional fuels.",
#   "I miss the convenience of gasoline stations on long trips.",
#   "The cost of CNG conversion was high, but it’s paying off.",
#   "It’s harder to plan long trips with a CNG vehicle.",
#   "CNG is great for reducing urban pollution."
]


	
for i in array:
    output = query({
	"inputs": i,
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
