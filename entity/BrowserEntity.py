from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from utils.css_selectors import Selectors  # Assuming this is your css_selectors.py file

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


    def navigate_to_url(self, site_name: str):
        # Fetch the URL from the CSS selectors file
        selectors = Selectors.SELECTORS.get(site_name.lower())
        if selectors and 'url' in selectors:
            url = selectors['url']

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
        else:
            return "URL not found for the specified site."