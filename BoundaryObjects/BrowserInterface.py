import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from CISC699 import logger
from CISC699.config import Config
from CISC699.css_selectors import Selectors
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio


class BrowserInterface:

    def __init__(self, browser_type="chrome"):
        self.browser_type = browser_type
        self.driver = None

    def launch_browser(self, incognito=False, user=None):
        try:
            logger.log_command_execution('launch_browser', user)
            
            options = webdriver.ChromeOptions()
            # Add options to avoid crashing
            #options.add_argument("--no-sandbox")
            #options.add_argument("--disable-dev-shm-usage")
            #options.add_argument("--disable-gpu")
            options.add_argument("--remote-debugging-port=9222")  # Required for ChromeDriver to communicate with Chrome
            
            # Disable the "Chrome is being controlled by automated test software" banner
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            # Additional options to make the browser behavior more human-like
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_argument("--disable-popup-blocking")
            options.add_argument("--disable-infobars")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-webgl")
            options.add_argument("--disable-webrtc")
            options.add_argument("--disable-rtc-smoothing")

            # User-Agent string to mimic a real browser
            #user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            #options.add_argument(f"user-agent={user_agent}")

            if incognito:
                options.add_argument("--incognito")

            self.driver = webdriver.Chrome(service=Service(), options=options)
            success_message = "Chrome browser launched successfully in incognito mode." if incognito else "Chrome browser launched successfully."
            print(success_message)
            return success_message
        except Exception as e:
            logger.log_command_failed('launch_browser', e)
            error_message = f"Failed to launch browser: {e}"
            print(error_message)
            raise

    def navigate_to_url(self, url):
        if not self.driver:
            self.launch_browser()  # Launch the browser if it's not already running
        try:
            self.driver.get(url)
            print(f"Navigated to URL: {url}")
            return f"Navigated to URL: {url}"
        except Exception as e:
            print(f"Error navigating to URL: {e}")
            raise

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None  # Reset the driver after closing
            print("Browser closed successfully.")
            return "Browser closed successfully."
        else:
            print("No browser is currently open.")
            return "No browser is currently open."

    async def login(self, site, incognito=False, retries=1):
        url = Selectors.get_selectors_for_url(site)['url']
        username = getattr(Config, f"{site.upper()}_USERNAME", None)
        password = getattr(Config, f"{site.upper()}_PASSWORD", None)

        if not username or not password:
            raise ValueError(f"Credentials for {site} are not configured.")

        for attempt in range(retries):
            try:
                # Launch browser with or without incognito
                self.launch_browser(incognito=incognito)
                await asyncio.sleep(3)  # Allow the browser to launch

                # Navigate to the URL
                self.driver.get(url)
                await asyncio.sleep(3)

                # Enter the email address
                email_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(site)['email_field'])
                email_field.click()
                await asyncio.sleep(3)
                email_field.send_keys(username)
                await asyncio.sleep(3)

                # Enter the password
                password_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(site)['password_field'])
                password_field.click()
                await asyncio.sleep(3)
                password_field.send_keys(password)
                await asyncio.sleep(3)

                # Click the login button
                SignIn_button = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(site)['SignIn_button'])
                SignIn_button.click()
                await asyncio.sleep(5)  # Wait for the login to process

                WebDriverWait(self.driver, 30).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.get_selectors_for_url(site)['homePage'])))
                
                return f"Logged in to {url} successfully with username: {username}"

            except Exception as e:
                if attempt < retries - 1:
                    await asyncio.sleep(3)  # Wait time before retrying
                    print(f"Retrying login attempt {attempt + 1}...")
                else:
                    print(f"Failed to log in to {url}: {e}")
                    raise e
