from src.otodom.otodom_scraper import scrape_otodom_listings
from src.olx.olx_scraper import scrape_olx_listings
from src.config import ScrapeConfig

def main():

    # Create an Otodom-specific scrape configuration
    otodom_config = ScrapeConfig(
        city='krakow/krakow/krakow/stare-miasto',
        min_price=2500,
        max_price=3000,
        min_area=40,
        max_area=50,
        base_url='https://www.otodom.pl/pl/wyniki/wynajem/mieszkanie/malopolskie'
    )

    # Create an OLX scrape configuration
    olx_config = ScrapeConfig(
        city='krakow',
        min_price=2500,
        max_price=3000,
        min_area=40,
        max_area=50,
        base_url='https://www.olx.pl/nieruchomosci/mieszkania/wynajem',
    )
    scrape_otodom_listings(otodom_config)
    scrape_olx_listings(olx_config)


if __name__ == "__main__":
    main()
