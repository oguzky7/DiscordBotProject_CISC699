class BrowserEntity:
    def __init__(self):
        self.browser_type = None  
        self.is_incognito = False

    def set_browser_type(self, browser_type):
        self.browser_type = browser_type

    def set_incognito(self, incognito):
        self.is_incognito = incognito
