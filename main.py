from src.otodom.otodom_scraper import scrape_listings

def main():
    scrape_url = 'https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/malopolskie/krakow/krakow/krakow/stare-miasto?ownerTypeSingleSelect=ALL&distanceRadius=5&priceMin=2500&priceMax=2500&areaMin=40&areaMax=40&viewType=listing'
    
    scrape_listings(scrape_url)

if __name__ == "__main__":
    main()
