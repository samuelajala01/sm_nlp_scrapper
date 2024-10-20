import requests
from bs4 import BeautifulSoup

# URL to scrape data from
url = "https://web.facebook.com/search/posts/?q=CNG"  # Replace with the actual URL

# Send a GET request to the URL
response = requests.get(url)
print(response)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content
#     soup = BeautifulSoup(response.content, "html.parser")
    
#     # Find all div elements with dir="auto"
#     divs_with_auto_dir = soup.find_all("div", attrs={"dir": "auto"})
    
#     # Limit the number of divs to display, e.g., the first 5 divs
#     limit = 5
#     divs_with_auto_dir_limited = divs_with_auto_dir[:limit]
    
#     # Loop through the limited divs and extract their text content
#     for div in divs_with_auto_dir_limited:
#         print(div.get_text(strip=True))
# else:
#     print(f"Failed to retrieve content from the URL. Status code: {response.status_code}")
