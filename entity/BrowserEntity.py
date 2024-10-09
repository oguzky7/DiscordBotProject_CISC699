import asyncio
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.configuration import load_config
from utils.css_selectors import Selectors


class BrowserEntity:
    _instance = None
    config = load_config()
    search_element_timeOut = config.get('project_options', {}).get('search_element_timeOut', 15)
    sleep_time = config.get('project_options', {}).get('sleep_time', 3)
    
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
                return result
            else:
                result = "Browser is already running."
                return result
        except Exception as e:
            result = f"BrowserEntity_Failed to launch browser: {str(e)}"
            return result
        
    def close_browser(self):
        try:
            if self.browser_open and self.driver:
                self.driver.quit()
                self.browser_open = False
                return "Browser closed."
            else:
                return "No browser is currently open."
        except Exception as e:
            return f"BrowserEntity_Failed to close browser: {str(e)}"

    def navigate_to_website(self, url):
        try:
            if not self.is_browser_open():
                launch_message = self.launch_browser()
                if "Failed" in launch_message:
                    return launch_message

            if self.driver:
                self.driver.get(url)
                return f"Navigated to {url}"
            else:
                return "Failed to open browser."
        except Exception as e:
            return f"BrowserEntity_Failed to navigate to {url}: {str(e)}"

    async def login(self, url, username, password):
        try:
            navigate_message = self.navigate_to_website(url)
            if "Failed" in navigate_message:
                return navigate_message

            email_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['email_field'])
            email_field.send_keys(username)
            await asyncio.sleep(self.sleep_time)

            password_field = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['password_field'])
            password_field.send_keys(password)
            await asyncio.sleep(self.sleep_time)

            sign_in_button = self.driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['SignIn_button'])
            sign_in_button.click()
            await asyncio.sleep(self.sleep_time)

            WebDriverWait(self.driver, self.search_element_timeOut).until(EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.get_selectors_for_url(url)['homePage'])))
            return f"Logged in to {url} successfully with username: {username}"
        except Exception as e:
            return f"BrowserEntity_Failed to log in to {url}: {str(e)}"