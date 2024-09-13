from control.BrowserControl import BrowserControl

class NavigationControl:
    def __init__(self):
        self.browser_control = BrowserControl()

    def navigate_to_url(self, url: str):
        """Ensure the browser is launched and navigate to the specified URL."""
        # First, launch the browser if not already running
        browser_status = self.browser_control.launch_browser()

        # Get the browser driver instance
        driver = self.browser_control.browser_entity.get_driver()

        # Navigate to the URL
        driver.get(url)
        return f"{browser_status}\nNavigated to {url}"
