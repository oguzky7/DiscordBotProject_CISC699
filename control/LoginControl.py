from entity.BrowserEntity import BrowserEntity
from control.AccountControl import AccountControl

class LoginControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()
        self.account_control = AccountControl()

    async def login(self, site, incognito=False, retries=1):
        # Fetch credentials using AccountControl
        account = self.account_control.fetch_account_by_website(site)
        if account:
            username, password = account
            return await self.browser_entity.login(site, username, password, incognito, retries)
        else:
            return f"No account found for website {site}"
