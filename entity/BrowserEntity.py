class BrowserEntity:
    def __init__(self):
        self.driver = None
        self.browser_open = False

    def set_browser_open(self, is_open):
        self.browser_open = is_open

    def is_browser_open(self):
        return self.browser_open
