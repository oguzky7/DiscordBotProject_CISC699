from entity.BrowserEntity import BrowserEntity

class CloseBrowserControl:
    def __init__(self, browser_entity):
        # Use the shared browser_entity instance passed from the boundary
        self.browser_entity = browser_entity

    def close_browser(self):
        # Check if the browser is open by accessing the shared browser_entity instance
        if self.browser_entity.is_browser_open():
            if self.browser_entity.driver:
                # Close the browser and update the state
                self.browser_entity.driver.quit()  # Close the browser instance
                self.browser_entity.set_browser_open(False)
                return "Browser closed."
            else:
                return "Browser instance is missing."
        else:
            return "No browser is currently open."
