from control.BrowserControl import BrowserControl

class CloseBrowserControl:
    def __init__(self):
        self.browser_control = BrowserControl()

    def close_browser(self):
        """Close the browser via BrowserControl."""
        return self.browser_control.close_browser()
