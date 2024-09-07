from entity.BrowserEntity import BrowserEntity

class CloseBrowserControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()

    def close_browser(self):
        return self.browser_entity.close_browser()
