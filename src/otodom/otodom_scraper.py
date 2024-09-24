from src.utils import fetch_page_content, extract_json_data

# Constants
BASE_URL = 'https://www.otodom.pl/pl/oferta/'

# Function to process individual listings
def process_listing(listing):
    title = listing.get('title', 'N/A')
    price = listing.get('totalPrice', {}).get('value', 'N/A')
    currency = listing.get('totalPrice', {}).get('currency', 'N/A')
    location = f"{listing['location']['address']['city']['name']}, {listing['location']['address']['province']['name']}"
    images = listing.get('images', [])
    image_url = images[0]['large'] if images else 'No image available'
    slug = listing.get('slug', '')
    full_url = BASE_URL + slug

    return {
        'title': title,
        'price': f"{price} {currency}",
        'location': location,
        'url': full_url,
        'image_url': image_url
    }

# Function to print the listing details
def print_listing_details(listing_details):
    print(f"Title: {listing_details['title']}")
    print(f"Price: {listing_details['price']}")
    print(f"Location: {listing_details['location']}")
    print(f"URL: {listing_details['url']}")
    print(f"Image URL: {listing_details['image_url']}")
    print('-' * 40)

# Main function to scrape the listings
def scrape_listings(url):
    try:
        page_content = fetch_page_content(url)
        data = extract_json_data(page_content)
        listings = data['props']['pageProps']['data']['searchAds']['items']

        for listing in listings:
            listing_details = process_listing(listing)
            print_listing_details(listing_details)

    except Exception as e:
        print(f"Error occurred: {e}")