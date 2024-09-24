import requests
from bs4 import BeautifulSoup
import json

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Function to get page content
def fetch_page_content(url):
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        # print(response.text)
        return response.text
    else:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    
# Function to extract JSON data from the page
def extract_json_data(page_content):
    soup = BeautifulSoup(page_content, 'lxml')
    json_data = soup.find('script', type='application/json')
    # print(json.loads(json_data.string))
    return json.loads(json_data.string)

