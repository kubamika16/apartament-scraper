class ScrapeConfig:
    def __init__(self, city, min_price, max_price, min_area, max_area, base_url):
        self.city = city
        self.min_price = min_price
        self.max_price = max_price
        self.min_area = min_area
        self.max_area = max_area
        self.base_url = base_url

   # Build URL for OLX or Otodom listings
    def build_url(self):
        if 'otodom' in self.base_url:
            return f"{self.base_url}/{self.city}?ownerTypeSingleSelect=ALL&distanceRadius=5&priceMin={self.min_price}&priceMax={self.max_price}&areaMin={self.min_area}&areaMax={self.max_area}&viewType=listing"
        elif 'olx' in self.base_url:
            # Example OLX URL pattern
            return f"{self.base_url}/q-mieszkanie-{self.city}/?search%5Bfilter_float_price:from%5D={self.min_price}&search%5Bfilter_float_price:to%5D={self.max_price}&search%5Bfilter_float_m:from%5D={self.min_area}&search%5Bfilter_float_m:to%5D={self.max_area}"
        else:
            raise ValueError("Unsupported website base URL")