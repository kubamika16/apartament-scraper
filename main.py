import json
import requests
from bs4 import BeautifulSoup

# URL for the specific apartment listings in Kraków that you're scraping
url = 'https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/malopolskie/krakow/krakow/krakow/stare-miasto?ownerTypeSingleSelect=ALL&distanceRadius=5&priceMin=2500&priceMax=2500&areaMin=40&areaMax=40&viewType=listing'

# Headers to make the request appear as if it's coming from a legitimate browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Send an HTTP GET request to the server to fetch the page content
response = requests.get(url, headers=headers)

# Parse the HTML content of the page with BeautifulSoup using lxml parser
soup = BeautifulSoup(response.text, 'lxml')

# Attempt to find JSON-like data stored within <script> tags of type application/json
json_data = soup.find('script', type='application/json')

# Convert the found JSON string into a Python dictionary for further processing
data = json.loads(json_data.string)

print(data['props']['pageProps']['data']['searchAds']['items'])

# Base URL for the listings
base_url = 'https://www.otodom.pl/pl/oferta/'

# Loop through each listing and extract the required details
for listing in data['props']['pageProps']['data']['searchAds']['items']:
    print("Regular listings:")
    title = listing.get('title','N/A')
    price = listing.get('totalPrice', {}).get('value', 'N/A')
    currency = listing.get('totalPrice', {}).get('currency', 'N/A')
    location = listing['location']['address']['city']['name'] + ', ' + listing['location']['address']['province']['name']
    images = listing.get('images', [])

    # Extract the slug and construct the URL
    slug = listing.get('slug', '')
    full_url = base_url + slug

    print(f"title: {title}")
    print(f"price: {price} {currency}")
    print(f"location: {location}")
    print(f"URL: {full_url}")
    print(f"Image URL: {images[0]['large']}")
    print('-'*40)