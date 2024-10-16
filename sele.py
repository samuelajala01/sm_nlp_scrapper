from selenium import webdriver
from bs4 import BeautifulSoup
import re
import time

# Initialize the Selenium WebDriver for Firefox (Geckodriver)
driver = webdriver.Chrome()

# Twitter URL to scrape
url = 'https://x.com/search?q=cng%20%22cng%20gas%22%20-filter%3Alinks%20filter%3Areplies&src=typed_query'  # Replace with the actual Twitter URL

# Open the URL with Selenium
driver.get(url)

# Give the page some time to load the dynamic content
time.sleep(5) 

# Once the page is fully loaded, grab the page source
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Use regex to find all divs with an id that starts with "id__"
divs = soup.find_all('div', id=re.compile('^id__'))

# Print out the matching divs
for div in divs:
    print(div)

# Close the Selenium WebDriver
driver.quit()

