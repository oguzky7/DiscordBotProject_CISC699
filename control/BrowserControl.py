from entity.BrowserEntity import BrowserEntity

class BrowserControl:
    
    def __init__(self):
        # Initialize the entity object inside the control layer
        self.browser_entity = BrowserEntity()

    def receive_command(self, command_data):
        # Validate the command
        print("Data Received from boundary object: ", command_data)
        if command_data == "launch_browser":
            # Call the entity to perform the actual operation
            result = self.browser_entity.launch_browser()
            return result
        
        elif command_data == "close_browser":
            # Call the entity to perform the close operation
            result = self.browser_entity.close_browser()
            return result
        
        else:
            return "Invalid command."
