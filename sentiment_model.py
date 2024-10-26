import dotenv
import requests
import pandas as pd


# Load the Hugging Face API token from the .env file
hf_bearer_token = dotenv.get_key(dotenv.find_dotenv(), "HF_BEARER_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment-latest"
headers = {"Authorization": hf_bearer_token}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

comments_list = pd.read_excel("model_input.xlsx")

# Path to the output Excel file
file_path = "model_output.xlsx"


negative_comments = []
neutral_comments = []
positive_comments = []

for comment in comments_list['comments']:
    if len(negative_comments) >= 100 and len(neutral_comments) >= 100 and len(positive_comments) >= 100:
        break
        
    try:
        output = query({ "inputs": comment })
        sentiment = output[0][0]['label']
       
        if sentiment == 'negative' and len(negative_comments) < 100:
            negative_comments.append(comment)
            print(f"Negative sentiment appended, count:{len(negative_comments)}")
            if len(negative_comments) == 100:
                print("Reached 100 negative comments!")
               
        elif sentiment == 'neutral' and len(neutral_comments) < 100:
            neutral_comments.append(comment)
            print(f"Neutral sentiment appended, count:{len(neutral_comments)}")
            if len(neutral_comments) == 100:
                print("Reached 100 neutral comments!")
               
        elif sentiment == 'positive' and len(positive_comments) < 100:
            positive_comments.append(comment)
            print(f"Positive sentiment appended, count:{len(positive_comments)}")
            if len(positive_comments) == 100:
                print("Reached 100 positive comments!")
               
    except Exception as e:
        print(f"Error processing comment: {e}...moving to next comment.")
        continue



final_comments = []

# Add negative comments
for comment in negative_comments[:100]:
    final_comments.append({'comment': comment, 'sentiment': 'negative'})

# Add neutral comments
for comment in neutral_comments[:100]:
    final_comments.append({'comment': comment, 'sentiment': 'neutral'})

# Add positive comments
for comment in positive_comments[:100]:
    final_comments.append({'comment': comment, 'sentiment': 'positive'})
    
# Save to Excel
final_df = pd.DataFrame(final_comments)
final_df.to_excel(file_path, index=False)
print("\nAnalysis completed and saved to 'model_output.xlsx'.")