from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors

class NavigationControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity

    def navigate_to_website(self, site: str):
        # Fetch URL in the control
        url = Selectors.get_selectors_for_url(site).get('url')
        if not url:
            return f"URL for {site} not found."

        return self.browser_entity.navigate_to_url(url)
