from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors  # Used in both LoginControl and NavigationControl
import re  # Used for URL pattern matching in LoginControl

class BrowserControl:
    def __init__(self):
        self.browser_entity = BrowserEntity()  # Initialize the entity object inside the control layer

    # Browser-related command handler
    async def receive_command(self, command_data, *args):
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
        elif command_data == "login":
            try:
                site = args[0]
                username = args[1]
                password = args[2]
                print(f"Username: {username}, Password: {password}")

                # Improved regex to detect URLs even without http/https
                url_pattern = re.compile(r'(https?://)?(www\.)?(\w+)(\.\w{2,})')

                # Check if the input is a full URL or a site name
                if url_pattern.search(site):
                    # If it contains a valid domain pattern, treat it as a URL
                    if not site.startswith('http'):
                        # Add 'https://' if the URL does not include a protocol
                        url = f"https://{site}"
                    else:
                        url = site
                    print(f"Using provided URL: {url}")
                else:
                    # If not a URL, look it up in the CSS selectors
                    selectors = Selectors.get_selectors_for_url(site)
                    if not selectors or 'url' not in selectors:
                        return f"URL for {site} not found."
                    url = selectors.get('url')
                    print(f"URL from selectors: {url}")

                if not url:
                    return f"URL for {site} not found."

                result = await self.browser_entity.login(url, username, password)
                return f"Control Object Result: {result}"
            except Exception as e:
                return f"Control Layer Exception: {str(e)}"
        
        # Handle navigation commands
        elif command_data == "navigate_to_website" and site:
            url_pattern = re.compile(r'(https?://)?(www\.)?(\w+)(\.\w{2,})')

            # Check if the input is a full URL or a site name
            if url_pattern.search(site):
                # If it contains a valid domain pattern, treat it as a URL
                if not site.startswith('http'):
                    # Add 'https://' if the URL does not include a protocol
                    url = f"https://{site}"
                else:
                    url = site
                print(f"Using provided URL: {url}")
            else:
                # If not a URL, look it up in the CSS selectors
                selectors = Selectors.get_selectors_for_url(site)
                if not selectors or 'url' not in selectors:
                    return f"URL for {site} not found."
                url = selectors.get('url')
                
                print("URL not provided, default URL for Google is: " + url)

            try:
                result = self.browser_entity.navigate_to_website(url)
                return f"Control Object Result: {result}"
            except Exception as e:
                return f"Control Layer Exception: {str(e)}"

        else:
            return "Invalid command."
