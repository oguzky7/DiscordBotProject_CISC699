import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.css_selectors import Selectors  # Import CSS selectors for the website

class BrowserEntity:
    def __init__(self, browser_type="chrome"):
        self.browser_type = browser_type
        self.driver = None

    def launch_browser(self, incognito=False, user=None):
        try:
            # Special launch options as per your original implementation
            options = webdriver.ChromeOptions()

            # Add options to avoid crashing and improve performance
            options.add_argument("--remote-debugging-port=9222")  # Required for ChromeDriver to communicate with Chrome
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

            # Launch in incognito mode if specified
            if incognito:
                options.add_argument("--incognito")

            # Start the Chrome browser with the configured options
            self.driver = webdriver.Chrome(service=Service(), options=options)
            success_message = "Chrome browser launched successfully in incognito mode." if incognito else "Chrome browser launched successfully."
            print(success_message)
            return success_message
        except Exception as e:
            error_message = f"Failed to launch browser: {e}"
            print(error_message)
            raise



    def navigate_to_url(self, url):
        if not self.driver:
            self.launch_browser()  # Launch the browser if it's not already running
        try:
            self.driver.get(url)
            return f"Navigated to URL: {url}"
        except Exception as e:
            raise

    async def login(self, site, username, password, incognito=False, retries=1):
        # Get the URL and selectors from css_selectors
        url = Selectors.get_selectors_for_url(site)['url']
        print(url)
        print(site)
        print(username)
        print("debug4")
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
