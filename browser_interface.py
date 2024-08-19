from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  # Corrected import
from webdriver_manager.chrome import ChromeDriverManager
from config import Config

class BrowserInterface:
    def __init__(self, use_existing_session=False):
        self.driver = None
        self.use_existing_session = use_existing_session

    def launch_browser(self, incognito=False):
        chrome_options = Options()
        chrome_options.add_argument(f"user-data-dir={Config.CHROME_USER_DATA_PATH}")
        
        if incognito:
            chrome_options.add_argument("--incognito")

        if self.use_existing_session:
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--remote-debugging-port=9222")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.maximize_window()
        print("Chrome browser launched and maximized.")

    def navigate_to_url(self, url):
        if self.driver:
            self.driver.get(url)
            print(f"Navigated to URL: {url}")
        else:
            raise ValueError("Browser must be launched before navigating to a URL.")

    def get_price(self, url):
        self.navigate_to_url(url)
        selectors = Config.CSS_SELECTORS.get(url.split('//')[1].split('/')[0].lower())
        if selectors and "price" in selectors:
            try:
                price_element = self.driver.find_element(By.CSS_SELECTOR, selectors["price"])
                price = price_element.text
                print(f"Price found: {price}")
                return price
            except Exception as e:
                print(f"Error finding price: {e}")
                return None
        else:
            print("No valid CSS selector found for the given URL.")
            return None

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            print("Browser closed.")
        else:
            print("No browser is currently open.")
