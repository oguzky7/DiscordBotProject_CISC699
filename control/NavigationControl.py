from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors

class NavigationControl:
    
    def __init__(self):
        # Initialize the entity object inside the control layer
        self.browser_entity = BrowserEntity()

    def process_command(self, command_data, url=None):
        # Validate the command
        if command_data == "navigate_to_website":
            if not url:
                selectors = Selectors.get_selectors_for_url("google")
                url = selectors.get('url')
                if not url:
                    return "No URL provided, and default URL for google could not be found."
                print("URL not provided, default URL for Google is: " + url)
                # Call the entity to navigate to the given URL
            result = self.browser_entity.navigate_to_url(url)
            return result
        else:
            return "Invalid command or URL."
