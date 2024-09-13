from entity.BrowserEntity import BrowserEntity
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class LaunchBrowserControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity  # Use the existing BrowserEntity instance

    def launch_browser(self):
        # Only launch if no browser is open
        if not self.browser_entity.is_browser_open():
            
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

            self.browser_entity.driver = webdriver.Chrome(service=Service(), options=options)
            print(f"Driver initialized: {self.browser_entity.driver}")  # Debugging print
            self.browser_entity.set_browser_open(True)
            return "Browser launched."
        else:
            return "Browser is already running."
