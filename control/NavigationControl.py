class NavigationControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity

    def navigate_to_website(self, site_name: str):
        # Navigate to the specified URL by calling the entity method
        return self.browser_entity.navigate_to_url(site_name)
