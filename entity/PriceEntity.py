import time
from selenium.webdriver.common.by import By
from utils.css_selectors import Selectors
from entity.BrowserEntity import BrowserEntity  # Import the browser interaction logic

class PriceEntity:
    def __init__(self):
        self.browser_entity = BrowserEntity()

    def get_price(self, url):
        """Fetch the price from the provided URL using CSS selectors."""
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors:
            raise ValueError(f"No selectors found for URL: {url}")
        
        # Navigate to the URL using the browser entity
        self.browser_entity.navigate_to_url(url)
        time.sleep(2)  # Wait for the page to load

        try:
            # Use the CSS selector to find the price on the page
            price_element = self.browser_entity.driver.find_element(By.CSS_SELECTOR, selectors['price'])
            price = price_element.text
            print(f"Price found: {price}")
            return price
        except Exception as e:
            print(f"Error finding price: {e}")
            return None
