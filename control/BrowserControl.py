from entity.BrowserEntity import BrowserEntity
from control.AccountControl import AccountControl  # Needed for LoginControl
from utils.css_selectors import Selectors  # Used in both LoginControl and NavigationControl

class BrowserControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()  # Initialize the entity object inside the control layer
        self.account_control = AccountControl()  # Manages account data for login use case

    # Browser-related command handler
    def receive_command(self, command_data, site=None, url=None):
        print("Data Received from boundary object: ", command_data)
        
        # Handle browser commands
        if command_data == "launch_browser":
            try:
                result = self.browser_entity.launch_browser()
                return f"Control Object Result: {result}"
            except Exception as e:
                return f"Control Layer Exception: {str(e)}"
        
        elif command_data == "close_browser":
            try:
                result = self.browser_entity.close_browser()
                return f"Control Object Result: {result}"
            except Exception as e:
                return f"Control Layer Exception: {str(e)}"

        # Handle login commands
        elif command_data == "login" and site:
            try:
                # Fetch account credentials from the account control
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

                result = self.browser_entity.login(url, username, password)
                return f"Control Object Result: {result}"
            except Exception as e:
                return f"Control Layer Exception: {str(e)}"
        
        # Handle navigation commands
        elif command_data == "navigate_to_website":
            if not url:
                selectors = Selectors.get_selectors_for_url("google")
                url = selectors.get('url')
                if not url:
                    return "No URL provided, and default URL for google could not be found."
                print("URL not provided, default URL for Google is: " + url)
            try:
                result = self.browser_entity.navigate_to_website(url)
                return f"Control Object Result: {result}"
            except Exception as e:
                return f"Control Layer Exception: {str(e)}"

        else:
            return "Invalid command."
