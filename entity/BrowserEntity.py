from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class BrowserEntity:
    _instance = None  # Singleton instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BrowserEntity, cls).__new__(cls)
            cls._instance.driver = None  # Initialize driver to None
        return cls._instance

    def initialize_driver(self, options):
        """Initialize the browser driver with the given options."""
        if self.driver:
            return "Browser is already running."
        self.driver = webdriver.Chrome(service=Service(), options=options)
        return "Browser initialized."

    def get_driver(self):
        """Return the current browser driver instance."""
        if not self.driver:
            raise Exception("Browser not initialized.")
        return self.driver

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            return "Browser closed."
        return "No browser is currently open."
