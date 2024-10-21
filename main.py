import requests
import pandas as pd
import dotenv

hf_bearer_token = dotenv.get_key(dotenv.find_dotenv(), "HF_BEARER_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/finiteautomata/bertweet-base-sentiment-analysis"
headers = {"Authorization": hf_bearer_token}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()


array = [
  "CNG is an excellent alternative to petrol and diesel, much cheaper!",
  "The mileage of my CNG car is fantastic, I save so much on fuel costs.",
  "CNG stations are hard to find in my area, which makes it inconvenient.",
  "I had to convert my vehicle to run on CNG, and it's been worth every penny.",
  "It’s cleaner than gasoline, so I feel like I'm doing my part for the environment.",
  "CNG takes up too much space in the trunk with the cylinder.",
]

results = {}
	
actual_results = [
  "POS",
  "POS",   
  "NEG",
  "POS",
  "POS",  
  "NEG",
  "NEG",   
  "NEG",
  "POS",  
  "NEU",    
  "POS",   
  "NEG",   
  "POS",
]

for i in array:
    output = query({
        "inputs": i,
    })
    results[i] = output[0][0]['label']
    
print(results)

df = pd.DataFrame(list(results.items()), columns=['Comment', 'Sentiment'])

print(df)

# Save the DataFrame to an Excel file
df.to_excel("model_input.xlsx", index=False)











