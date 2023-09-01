''' 
first install require libraries that with command in terminal 'pip install requests beautifulsoup4'
then proceed 
'''
import requests
from bs4 import BeautifulSoup

# The URL you want to fetch data from
URL = 'https://www.example-blog.com'

# Make an HTTP GET request
response = requests.get(URL)

# Check if the request was successful
if response.status_code == 200:
    # Parse the content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all article titles (assuming they are under <h2> tags)
    articles = soup.find_all('h2')
    
    # Print out all titles
    for article in articles:
        print(article.text)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

