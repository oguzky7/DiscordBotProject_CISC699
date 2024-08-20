from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config import Config
from css_selectors import Selectors
import time
import random


class BrowserInterface:
    """
    Handles interactions with Chrome browser, including launching, navigating to URLs, logging in, and getting prices.
    """
    

    def click_random_location(self):
        if self.driver:
            try:
                # Get the dimensions of the page
                body = self.driver.find_element(By.TAG_NAME, 'body')
                width = body.size['width']
                height = body.size['height']

                # Click at a random location within the page dimensions
                random_x = random.randint(0, width)
                random_y = random.randint(0, height)

                action = webdriver.common.action_chains.ActionChains(self.driver)
                action.move_by_offset(random_x, random_y).click().perform()

                print(f"Clicked at random location: ({random_x}, {random_y})")
            except Exception as e:
                print(f"Error clicking random location: {e}")
        else:
            print("No browser is currently open.")


    def __init__(self, browser_type="chrome"):
        self.browser_type = browser_type
        self.driver = None

    def launch_browser(self, incognito=False):
        options = webdriver.ChromeOptions()
        
        # Removed user-data-dir to avoid issues
        # options.add_argument(f"user-data-dir={Config.CHROME_USER_DATA_PATH}")
        
        # Add options to avoid crashing
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")  # Required for ChromeDriver to communicate with Chrome
        
        # This will create a new temporary user profile
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")  # Disable infobars
        options.add_argument("--disable-extensions")  # Disable extensions

        if incognito:
            options.add_argument("--incognito")
        
        try:
            self.driver = webdriver.Chrome(service=Service(), options=options)
            print("Chrome browser launched successfully in incognito mode." if incognito else "Chrome browser launched successfully.")
        except Exception as e:
            print(f"Error launching Chrome browser: {e}")
            raise

    def navigate_to_url(self, url):
        if not self.driver:
            self.launch_browser()  # Launch the browser if it's not already running
        try:
            self.driver.get(url)
            
            # Example: Automatically accept cookies using JavaScript
            self.driver.execute_script("document.querySelectorAll('button[aria-label=\"Accept Cookies\"]').forEach(button => button.click());")
            
            print(f"Navigated to URL: {url}")
        except Exception as e:
            print(f"Error navigating to URL: {e}")
            raise



    def navigate_to_url(self, url):
        if not self.driver:
            self.launch_browser()  # Launch the browser if it's not already running
        try:
            self.driver.get(url)
            print(f"Navigated to URL: {url}")
        except Exception as e:
            print(f"Error navigating to URL: {e}")
            raise
    def login(self, url, username, password, max_retries=3):
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors:
            raise ValueError(f"No selectors found for URL: {url}")
        
        for attempt in range(max_retries):
            try:
                self.navigate_to_url(selectors['url'])  # Navigate to the login page

                # Enter the email address
                email_field = self.driver.find_element(By.CSS_SELECTOR, selectors['email_field'])
                email_field.send_keys(username)

                # Click a random location to dismiss pop-ups after entering the email
                self.click_random_location()

                continue_button = self.driver.find_element(By.CSS_SELECTOR, selectors['continue_button'])
                continue_button.click()

                time.sleep(2)  # Wait for the password field to appear

                # Enter the password
                password_field = self.driver.find_element(By.CSS_SELECTOR, selectors['password_field'])
                password_field.send_keys(password)

                login_button = self.driver.find_element(By.CSS_SELECTOR, selectors['login_button'])
                login_button.click()

                print(f"Logged in to {url} with username: {username}")
                return  # Exit if login is successful

            except Exception as e:
                print(f"Login attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    print(f"Retrying login... (Attempt {attempt + 2})")
                    self.driver.refresh()
                    time.sleep(2)  # Wait for the page to reload
                else:
                    raise  # Re-raise the exception if all retries fail


    def get_price(self, url):
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors:
            raise ValueError(f"No selectors found for URL: {url}")
        
        self.navigate_to_url(url)
        time.sleep(2)  # Wait for the page to load

        try:
            price_element = self.driver.find_element(By.CSS_SELECTOR, selectors['price'])
            price = price_element.text
            print(f"Price found: {price}")
            return price
        except Exception as e:
            print(f"Error finding price: {e}")
            return None

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            print("Browser closed.")
        else:
            print("No browser is currently open.")

    def select_date(self, date_selector, date):
        try:
            date_field = self.driver.find_element(By.CSS_SELECTOR, date_selector)
            date_field.clear()
            date_field.send_keys(date)
            print(f"Selected date: {date}")
        except Exception as e:
            print(f"Error selecting date: {e}")
            raise

    def select_time(self, time_selector, time_slot):
        try:
            time_field = self.driver.find_element(By.CSS_SELECTOR, time_selector)
            time_field.clear()
            time_field.send_keys(time_slot)
            print(f"Selected time: {time_slot}")
        except Exception as e:
            print(f"Error selecting time: {e}")
            raise
    def check_availability(self, url, date, time_slot):
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors:
            raise ValueError(f"No selectors found for URL: {url}")

        self.navigate_to_url(selectors['url'])

        try:
            date_field = self.driver.find_element(By.CSS_SELECTOR, selectors['date_field'])
            date_field.clear()
            date_field.send_keys(date)

            time_field = self.driver.find_element(By.CSS_SELECTOR, selectors['time_field'])
            time_field.clear()
            time_field.send_keys(time_slot)

            find_table_button = self.driver.find_element(By.CSS_SELECTOR, selectors['find_table_button'])
            find_table_button.click()

            time.sleep(2)  # Wait for the results to load

            availability_result = self.driver.find_element(By.CSS_SELECTOR, selectors['availability_result'])
            availability_text = availability_result.text
            print(f"Availability result: {availability_text}")
            return availability_text
        except Exception as e:
            print(f"Error checking availability: {e}")
            return None
