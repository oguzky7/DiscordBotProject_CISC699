from entity.BrowserEntity import BrowserEntity
from control.AccountControl import AccountControl  # Use AccountControl for consistency

class BrowserControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()
        self.account_control = AccountControl()  # Use AccountControl to fetch credentials

    def launch_browser(self, user, incognito=False):
        return self.browser_entity.launch_browser(incognito=incognito, user=user)

    def navigate_to_url(self, url):
        return self.browser_entity.navigate_to_url(url)

    async def login(self, site, incognito=False, retries=1):
        # Fetch credentials using AccountControl
        account = self.account_control.fetch_account_by_website(site)
        
        if account:
            username, password = account  # Unpack the credentials
            # Proceed with the login process in the browser entity
            return await self.browser_entity.login(site, username, password, incognito, retries)
        else:
            # If no matching account is found, raise an error
            raise ValueError(f"No credentials found for {site}")
