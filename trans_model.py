# Load model directly
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import praw
import dotenv

tokenizer = AutoTokenizer.from_pretrained("sbcBI/sentiment_analysis_model")
model = AutoModelForSequenceClassification.from_pretrained("sbcBI/sentiment_analysis_model")

client_id = dotenv.get_key(dotenv.find_dotenv(), "REDDIT_CLIENT_ID")
client_secret = dotenv.get_key(dotenv.find_dotenv(), "REDDIT_CLIENT_SECRET")


# Reddit API credentials
reddit = praw.Reddit(
    client_id=client_id,
    client_secret= client_secret,
    user_agent='my_reddit_scraper/0.1 by u/cx'
)

# Specify the URL of the Reddit page with comments
submission = reddit.submission(url='https://www.reddit.com/r/cng/comments/ir1d9q/worth_it_to_buy_cng_vehicles/')

# Fetch the top 20 comments
submission.comments.replace_more(limit=0)
comments = submission.comments.list()

# Iterate over the first 20 comments
for comment in comments[:20]:
    # Extract the comment body (text content)
    comment_text = comment.body
    
    # Send the comment text to the HuggingFace sentiment analysis model
    model.predict(comment_text)