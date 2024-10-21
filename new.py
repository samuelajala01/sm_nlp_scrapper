
import praw
import dotenv
import requests
import pandas as pd

hf_bearer_token = dotenv.get_key(dotenv.find_dotenv(), "HF_BEARER_TOKEN")


API_URL = "https://api-inference.huggingface.co/models/dipawidia/xlnet-base-cased-product-review-sentiment-analysis" #bigger and best model
headers = {"Authorization": hf_bearer_token}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


# List to store dictionaries of comments and labels
comments_list = pd.read_excel("model_input.xlsx")

# # Loop through the comments (you can change the range to suit your use case)
# for comment in comments[:3]:
#     output = query({
#         "inputs": comment.body,
#     })

# for comment in comments[:3]:
#     comments_list.append(comment.body)

# Create a DataFrame with a single column 'Comments'
# df = pd.DataFrame(comments_list, columns=['Comments'])

# # Print the DataFrame
# print(df)

# # Save the DataFrame to an Excel file
# df.to_excel("model_input.xlsx", index=False)

for comment in comments_list['Comments'][5:11]:
  
  output = query({
        "inputs": comment,
    })
  print({"comment": comment, "sentiment": output[0][0]['label'], "score": output[0][0]['score']})
  


# print(comments_list[:3])