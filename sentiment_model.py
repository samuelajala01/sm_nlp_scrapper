import dotenv
import requests
import pandas as pd

hf_bearer_token = dotenv.get_key(dotenv.find_dotenv(), "HF_BEARER_TOKEN")


API_URL = "https://api-inference.huggingface.co/models/dipawidia/xlnet-base-cased-product-review-sentiment-analysis" #bigger and best model
headers = {"Authorization": hf_bearer_token}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

comments_list = pd.read_excel("model_input.xlsx")  # Loading the scraped comments/posts

# Lists to store categorized comments
positive_comments = []
neutral_comments = []
negative_comments = []

# Perform sentiment analysis with error handling
for comment in comments_list['Comments'][3:7]:
    try:
        output = query({
            "inputs": comment,  # Pass each comment to the model
        })

        # Try to access the sentiment label
        sentiment = output[0][0]['label']
        print({"comment": comment, "sentiment": sentiment})

        # Append to the correct list based on sentiment
        if sentiment == 'POSITIVE' or sentiment == 'Positive':
            positive_comments.append({'comment': comment, 'sentiment': 'positive'})
        elif sentiment == 'NEUTRAL' or sentiment == 'Neutral':
            neutral_comments.append({'comment': comment, 'sentiment': 'neutral'})
        elif sentiment == 'NEGATIVE' or sentiment =='Negative':
            negative_comments.append({'comment': comment, 'sentiment': 'negative'})

    except (KeyError, IndexError) as e:
        print(f"Error processing comment: {comment}. Error: {e}")
        continue  # Skip to the next comment

# Limit the number of comments per category to 100
positive_comments = positive_comments[:100]
neutral_comments = neutral_comments[:100]
negative_comments = negative_comments[:100]

# Combine all comments into one DataFrame
combined_comments = pd.DataFrame(positive_comments + neutral_comments + negative_comments)

# Output the results to an Excel file
combined_comments.to_excel("sentiment_analysis_results.xlsx", index=False)

print("Sentiment analysis completed and saved to 'sentiment_analysis_results.xlsx'.")
