from selenium.webdriver.common.by import By
from utils.css_selectors import Selectors

class PriceEntity:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity

    def get_price_from_page(self, url: str):
        """Fetches the price from the page using the correct CSS selector."""
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors or 'price' not in selectors:
            return "No price selector found for this URL."

        # Navigate to the URL using BrowserEntity
        self.browser_entity.navigate_to_url(url)
        
        try:
            # Extract the price from the page
            price_element = self.browser_entity.driver.find_element(By.CSS_SELECTOR, selectors['price'])
            price = price_element.text
            return f"Price found: {price}"
        except Exception as e:
            return f"Error fetching price: {str(e)}"
