class LaunchBrowserControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity

    def launch_browser(self):
        return self.browser_entity.launch_browser()
