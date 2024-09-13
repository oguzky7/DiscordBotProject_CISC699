from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors

class NavigationControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity

    def navigate_to_website(self, url: str = None):
        if not url:
            selectors = Selectors.get_selectors_for_url("google")
            url = selectors.get('url')
            if not url:
                return "No URL provided, and default URL for google could not be found."
            print("URL not provided, default URL for Google is: " + url)
        return self.browser_entity.navigate_to_url(url)
