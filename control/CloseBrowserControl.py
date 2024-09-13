class CloseBrowserControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity

    def close_browser(self):
        return self.browser_entity.close_browser()
