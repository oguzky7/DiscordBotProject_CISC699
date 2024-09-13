from entity.BrowserEntity import BrowserEntity
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

class BrowserControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()

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



    def close_browser(self):
        """Close the browser."""
        return self.browser_entity.close_browser()
