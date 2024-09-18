from control.AccountControl import AccountControl
from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors

class LoginControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()
        self.account_control = AccountControl()  # Manages account data

    async def receive_command(self, command_data, site=None):
        """Handle login command and perform business logic."""
        print("Data received from boundary:", command_data)
        
        if command_data == "login" and site:
            # Fetch account credentials from the entity
            account_info = self.account_control.fetch_account_by_website(site)
            if not account_info:
                return f"No account found for {site}"

            username, password = account_info[0], account_info[1]
            print(f"Username: {username}, Password: {password}")

            # Get the URL from the CSS selectors
            url = Selectors.get_selectors_for_url(site).get('url')
            print(url)
            if not url:
                return f"URL for {site} not found."

            # Perform the login process via the entity
            result = await self.browser_entity.perform_login(url, username, password)
            return result
        else:
            return "Invalid command or site."
