from entity.BrowserEntity import BrowserEntity
from control.LaunchBrowserControl import LaunchBrowserControl
from selenium import webdriver
from utils.css_selectors import Selectors  # Assuming this is your css_selectors.py file

class NavigationControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity  # Use the same BrowserEntity instance
        self.launch_browser_control = LaunchBrowserControl(browser_entity)  # Share BrowserEntity instance

    def navigate_to_website(self, site_name):
        if not self.browser_entity.is_browser_open():
            self.launch_browser_control.launch_browser()  # Launch the browser if it's not running

        # Check if driver is valid
        if self.browser_entity.driver:
            print(self.browser_entity.driver)
            selectors = Selectors.SELECTORS.get(site_name.lower())
            if selectors and 'url' in selectors:
                self.browser_entity.driver.get(selectors['url'])
                return f"Navigated to {selectors['url']}"
            else:
                return "URL not found for the specified site."
        else:
            return "Browser instance not found."
