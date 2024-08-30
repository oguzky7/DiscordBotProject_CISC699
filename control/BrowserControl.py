from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from entity.BrowserEntity import BrowserEntity

class BrowserControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()
        self.driver = None

    def launch_browser(self, incognito=False):
        options = webdriver.ChromeOptions()
        if incognito:
            options.add_argument("--incognito")
            self.browser_entity.set_incognito(True)
        self.driver = webdriver.Chrome(service=Service(), options=options)
        return "Browser launched"

    def navigate_to_url(self, url):
        if self.driver:
            self.driver.get(url)
            return f"Navigated to {url}"
        return "Browser not launched"

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            return "Browser closed"
        return "No browser to close"
