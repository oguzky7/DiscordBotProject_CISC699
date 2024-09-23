from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors

class NavigationControl:
    
    def __init__(self):
        # Initialize the entity object inside the control layer
        self.browser_entity = BrowserEntity()

    def receive_command(self, command, url=None):
        # Validate the command
        print("Data Received from boundary object: ", command)
        if command == "navigate_to_website":
            if not url:
                selectors = Selectors.get_selectors_for_url("google")
                url = selectors.get('url')
                if not url:
                    return "No URL provided, and default URL for google could not be found."
                print("URL not provided, default URL for Google is: " + url)
            try:
                result = self.browser_entity.navigate_to_website(url) # Call the entity to perform the actual operation
            except Exception as e:
                result = str(e)  
            return result
        else:
            return "Invalid command."
