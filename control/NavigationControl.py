from entity.BrowserEntity import BrowserEntity

class NavigationControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()

    def navigate_to_url(self, url):
        """Navigate to a specific URL."""
        return self.browser_entity.navigate_to_url(url)
