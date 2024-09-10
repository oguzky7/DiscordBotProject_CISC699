from entity.BrowserEntity import BrowserEntity
from control.AccountControl import AccountControl  # Use AccountControl for consistency

class BrowserControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()
        self.account_control = AccountControl()  # Use AccountControl to fetch credentials

    def launch_browser(self, user, incognito=False):
        return self.browser_entity.launch_browser(incognito=incognito, user=user)
