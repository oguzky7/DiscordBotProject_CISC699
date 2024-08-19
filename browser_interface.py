from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BrowserInterface:
    """
    Handles interactions with Chrome browser, including launching, navigating to URLs, and logging in.
    """

    def __init__(self, browser_type="chrome"):
        # Initialize the browser interface with browser type
        self.browser_type = browser_type
        self.driver = None

    def launch_browser(self):
        # Launch Chrome browser in incognito mode and maximize the window
        if self.browser_type.lower() == "chrome":
            options = Options()
            options.add_argument("--incognito")
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
            print("Chrome browser launched in incognito mode and maximized.")
        else:
            raise ValueError("Unsupported browser type. Only 'chrome' is supported.")

    def navigate_to_url(self, url):
        # Launch the browser if not already running and navigate to the specified URL
        if not self.driver:
            self.launch_browser()
        self.driver.get(url)
        print(f"Navigated to URL: {url}")

    def login(self, username, password, username_field_id, password_field_id, login_button_xpath):
        # Log in using provided credentials
        if self.driver:
            username_field = self.driver.find_element(By.ID, username_field_id)
            password_field = self.driver.find_element(By.ID, password_field_id)
            login_button = self.driver.find_element(By.XPATH, login_button_xpath)

            username_field.send_keys(username)
            password_field.send_keys(password)
            login_button.click()

            print(f"Logged in with username: {username}")
        else:
            raise ValueError("Browser must be launched before logging in.")

    def close_browser(self):
        # Close the browser
        if self.driver:
            self.driver.quit()
            print("Browser closed.")
        else:
            print("No browser is currently open.")
