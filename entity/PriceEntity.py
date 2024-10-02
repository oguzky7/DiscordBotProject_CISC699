from selenium.webdriver.common.by import By
from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors  # Import selectors to get CSS selectors for the browser

class PriceEntity:
    """PriceEntity is responsible for interacting with the system (browser) to fetch prices 
    and handle the exporting of data to Excel and HTML."""
    
    def __init__(self):
        self.browser_entity = BrowserEntity()

    def get_price_from_page(self, url: str):        
        # Navigate to the URL using BrowserEntity
        self.browser_entity.navigate_to_website(url)
        selectors = Selectors.get_selectors_for_url(url)
        try:
            # Find the price element on the page using the selector
            price_element = self.browser_entity.driver.find_element(By.CSS_SELECTOR, selectors['price'])
            result = price_element.text
            return result
        except Exception as e:
            return f"Error fetching price: {str(e)}"    
        