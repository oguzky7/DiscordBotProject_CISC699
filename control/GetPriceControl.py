from entity.BrowserEntity import BrowserEntity
from selenium.webdriver.common.by import By
from utils.css_selectors import Selectors 
import asyncio

class GetPriceControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity

    async def get_price(self, url: str):
        # Fetch the url using the correct CSS selector
        if not url:
            selectors = Selectors.get_selectors_for_url("bestbuy")
            url = selectors.get('priceUrl')  # Get the price URL
            if not url:
                return "No URL provided, and default URL for BestBuy could not be found."
            print("URL not provided, default URL for BestBuy is: " + url)
   
        # Step 3: Call the entity to get the price
        price = self.browser_entity.get_price_from_page(url)
        return price

