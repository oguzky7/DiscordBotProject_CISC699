import asyncio
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.css_selectors import Selectors


class BrowserEntity:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(BrowserEntity, cls).__new__(cls, *args, **kwargs)
        return cls._instance


    def __init__(self):
        self.driver = None
        self.browser_open = False


    def set_browser_open(self, is_open: bool):
        self.browser_open = is_open


    def is_browser_open(self) -> bool:
        return self.browser_open


    def launch_browser(self):
        try:
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
                result = "Browser launched."
                print(result)
                return result
            else:
                result = "Browser is already running."
                print(result)
                return result
        except Exception as e:
            result = f"Failed to launch browser: {str(e)}"
            print(result)
            return result

    def close_browser(self):
        if self.browser_open and self.driver:
            self.driver.quit()
            self.browser_open = False
            result = "Browser closed."
            print(result)
            return result
        else:
            result = "No browser is currently open."
            print(result)
            return result


    def navigate_to_website(self, url):       
            # Ensure the browser is launched before navigating
            if not self.is_browser_open():
                self.launch_browser()

            # Navigate to the URL if browser is open
            if self.driver:
                self.driver.get(url)
                result = f"Navigated to {url}"
                print(result)
                return result
            else:
                result = "Failed to open browser."
                print(result)
                return result
        

    async def login(self, url, username, password):
        # Navigate to the website
        self.navigate_to_website(url)
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

            result = f"Logged in to {url} successfully with username: {username}"
            print(result)
            return result
        except Exception as e:
            result = f"Failed to log in: {str(e)}"
            print(result)
            return result
        
    