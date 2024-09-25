# from src.utils import fetch_page_content
from bs4 import BeautifulSoup
from src.utils import fetch_page_content
from src.config import ScrapeConfig

# OLX base URL for constructing listing links
OLX_BASE_URL = 'https://www.olx.pl'

# Function to process individual listings (OLX-specific)
def process_olx_listing(listing):
    title = listing.find('h6').text if listing.find('h6') else 'N/A'
    price = listing.find('p', {'data-testid': 'ad-price'}).text if listing.find('p', {'data-testid': 'ad-price'}) else 'N/A'
    location_date = listing.find('p', {'data-testid': 'location-date'}).text if listing.find('p', {'data-testid': 'location-date'}) else 'N/A'
    location = location_date.split(" - ")[0]  # Extract location before the hyphen
    link = listing.find('a')['href'] if listing.find('a') else ''
    if link.startswith('http'):  # If it's a full URL (like Otodom)
        full_url = link
    else:  # It's an internal OLX link
        full_url = OLX_BASE_URL + link
    
    return {
        'title': title,
        'price': price,
        'location': location,
        'url': full_url,
    }

# Function to print OLX listing details
def print_olx_listing_details(listing_details):
    print(f"Title: {listing_details['title']}")
    print(f"Price: {listing_details['price']}")
    print(f"Location: {listing_details['location']}")
    print(f"URL: {listing_details['url']}")
    print('-' * 40)

# Main function to scrape OLX listings
def scrape_olx_listings(scrape_config: ScrapeConfig):
    try:
        # Build the URL using the provided config
        url = scrape_config.build_url()
        
        page_content = fetch_page_content(url)
        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(page_content, 'lxml')

        # Find the listings in OLX's HTML structure
        listings = soup.find_all('div', {'data-cy': 'l-card'})
        
        # Process each listing
        for listing in listings:
            listing_details = process_olx_listing(listing)
            print_olx_listing_details(listing_details)


    except Exception as e:
        print(f"Error occurred during OLX scraping: {e}")


# Test the OLX scraper directly within this file
if __name__ == "__main__":
    test_url = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/q-mieszkanie-krak%C3%B3w/?search%5Bfilter_float_price:from%5D=2500&search%5Bfilter_float_price:to%5D=3000&search%5Bfilter_float_m:from%5D=40&search%5Bfilter_float_m:to%5D=50'
    
    # Test the OLX scraper with the test URL
    scrape_olx_listings(test_url)
