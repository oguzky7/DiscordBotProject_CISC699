import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.css_selectors import Selectors  # Import CSS selectors for the website

class BrowserEntity:
    _instance = None  # Singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BrowserEntity, cls).__new__(cls)
            cls._instance.driver = None  # Initialize driver to None
        return cls._instance


    def launch_browser(self, incognito=False, user=None):
        if self.driver:
            print("Browser is already running. No need to launch a new one.")
            return "Browser is already running."

        try:
            # Special launch options as per your original implementation
            options = webdriver.ChromeOptions()

            # Add options to avoid crashing and improve performance
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

            if incognito:
                options.add_argument("--incognito")

            self.driver = webdriver.Chrome(service=Service(), options=options)
            success_message = "Chrome browser launched successfully in incognito mode." if incognito else "Chrome browser launched successfully."
            print(f"Driver initialized: {self.driver}")  # Debug: Print the driver
            return success_message
        except Exception as e:
            error_message = f"Failed to launch browser: {e}"
            print(error_message)
            raise


    def navigate_to_url(self, url):
        if not self.driver:
            print("Driver is not initialized, launching browser first.")  # Debug
            self.launch_browser()
        try:
            self.driver.get(url)
            print(f"Navigated to URL: {url}")
            return f"Navigated to URL: {url}"
        except Exception as e:
            raise


    def close_browser(self):
        print(f"Closing browser. Current driver: {self.driver}")  # Debug: Check the driver status
        if self.driver:
            self.driver.quit()  # Close the browser session
            self.driver = None  # Set to None after closing
            print("Browser closed successfully.")
            return "Browser closed successfully."
        else:
            print("No browser is currently open.")
            return "No browser is currently open."


    async def login(self, site, username, password, incognito=False, retries=1):
        # Get the URL and selectors from css_selectors
        url = Selectors.get_selectors_for_url(site)['url']
        for attempt in range(retries):
            try:
                self.navigate_to_url(url)
                await asyncio.sleep(3)

                # Enter the email address
                email_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(site)['email_field'])
                email_field.click()
                email_field.send_keys(username)
                await asyncio.sleep(3)

                # Enter the password
                password_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(site)['password_field'])
                password_field.click()
                password_field.send_keys(password)
                await asyncio.sleep(3)

                # Click the login button
                sign_in_button = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(site)['SignIn_button'])
                sign_in_button.click()
                await asyncio.sleep(5)

                # Wait for the homepage to load after login
                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.get_selectors_for_url(site)['homePage'])))
                
                return f"Logged in to {url} successfully with username: {username}"
            except Exception as e:
                if attempt < retries - 1:
                    await asyncio.sleep(3)
                else:
                    raise e
