from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from css_selectors import Selectors
import time, random

class BrowserInterface:

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
        # Add options to avoid crashing
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--remote-debugging-port=9222")  # Required for ChromeDriver to communicate with Chrome
        
        # Disable the "Chrome is being controlled by automated test software" banner
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)

        # Use a real Chrome user profile
        #options.add_argument(f"user-data-dir={Config.CHROME_USER_DATA_PATH}")
        
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
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        options.add_argument(f"user-agent={user_agent}")

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
            print(f"Navigated to URL: {url}")
        except Exception as e:
            print(f"Error navigating to URL: {e}")
            raise

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

    def login(self, url, username, password, incognito=False, retries=1):
        for attempt in range(retries):
            try:
                # Launch browser with or without incognito
                self.launch_browser(incognito=incognito)
                self.navigate_to_url(url)
                time.sleep(3)

                # Enter the email address
                email_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['email_field'])
                email_field.click()
                time.sleep(3)
                email_field.send_keys(username)
                time.sleep(3)  # Delay between entering email and clicking continue

                # Enter the password
                password_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['password_field'])
                password_field.click()
                time.sleep(3)
                password_field.send_keys(password)
                time.sleep(3)  # Delay between entering password and clicking login

                # Click the login button
                SignIn_button = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['SignIn_button'])
                SignIn_button.click()
                time.sleep(5)  # Wait for the login to process

                WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['homePage'])))
                
                return f"Logged in to {url} successfully with username: {username}"

            except Exception as e:
                if attempt < retries - 1:
                    time.sleep(3)  # Wait time before retrying
                    print(f"Retrying login attempt {attempt + 1}...")
                else:
                    print(f"Failed to log in to {url}: {e}")
                    raise e
