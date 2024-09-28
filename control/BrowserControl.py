from entity.BrowserEntity import BrowserEntity

class BrowserControl:
    
    def __init__(self):
        self.browser_entity = BrowserEntity()

    def receive_command(self, command_data):
        print("Data Received from boundary object: ", command_data)
        try:
            if command_data == "launch_browser":
                result = self.browser_entity.launch_browser()
            elif command_data == "close_browser":
                result = self.browser_entity.close_browser()
            else:
                result = "Invalid command."
            print(f"Control Layer Output: {result}")
            return f"Control Object Result: {result}"
        except Exception as e:
            error_msg = f"Control Layer Exception: {str(e)}"
            print(error_msg)
            return error_msg
