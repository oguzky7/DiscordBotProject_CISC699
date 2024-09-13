import asyncio
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.css_selectors import Selectors


class BrowserEntity:
    def __init__(self):
        self.driver = None
        self.browser_open = False


    def set_browser_open(self, is_open: bool):
        self.browser_open = is_open


    def is_browser_open(self) -> bool:
        return self.browser_open


    def launch_browser(self):
        if not self.browser_open:
            options = webdriver.ChromeOptions()
            options.add_argument("--remote-debugging-port=9222")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-webgl")
            options.add_argument("--disable-webrtc")
            options.add_argument("--disable-rtc-smoothing")

            self.driver = webdriver.Chrome(service=Service(), options=options)
            self.browser_open = True
            return "Browser launched."
        else:
            return "Browser is already running."


    def close_browser(self):
        if self.browser_open and self.driver:
            self.driver.quit()
            self.browser_open = False
            return "Browser closed."
        else:
            return "No browser is currently open."


    def navigate_to_url(self, url):       
            # Ensure the browser is launched before navigating
            if not self.is_browser_open():
                launch_message = self.launch_browser()
                print(launch_message)

            # Navigate to the URL if browser is open
            if self.driver:
                self.driver.get(url)
                return f"Navigated to {url}"
            else:
                return "Failed to open browser."
        

    async def perform_login(self, url, username, password):
        # Navigate to the website
        self.navigate_to_url(url)
        await asyncio.sleep(3)

        # Enter the username
        email_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['email_field'])
        email_field.send_keys(username)
        await asyncio.sleep(3)

        # Enter the password
        password_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['password_field'])
        password_field.send_keys(password)
        await asyncio.sleep(3)

        # Click the login button
        sign_in_button = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['SignIn_button'])
        sign_in_button.click()
        await asyncio.sleep(5)

        # Wait for the homepage to load
        try:
            WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['homePage'])))
            return f"Logged in to {url} successfully with username: {username}"
        except Exception as e:
            return f"Failed to log in: {str(e)}"
        
"""
    def get_price_from_page(self, url: str):
            selectors = Selectors.get_selectors_for_url(url)
            self.navigate_to_url(url)
            try:
                price_element = self.driver.find_element(By.CSS_SELECTOR, selectors['price'])
                price = price_element.text
                return f"Price found: {price}"
            except Exception as e:
                return f"Error fetching price: {str(e)}"
"""