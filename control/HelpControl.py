class HelpControl:
    def receive_command(self, command_data):
        """Handles the command and returns the appropriate message."""
        print("Data received from boundary:", command_data)
        
        if command_data == "project_help":
            help_message = (
                "Here are the available commands:\n"
                "!project_help - Get help on available commands.\n"
                "!fetch_all_accounts - Fetch all stored accounts.\n"
                "!add_account 'username' 'password' 'website' - Add a new account to the database.\n"
                "!fetch_account_by_website 'website' - Fetch account details by website.\n"
                "!delete_account 'account_id' - Delete an account by its ID.\n"
                "!launch_browser - Launch the browser.\n"
                "!close_browser - Close the browser.\n"
                "!navigate_to_website 'url' - Navigate to a specified website.\n"
                "!login 'website' - Log in to a website (e.g., !login bestbuy).\n"
                "!get_price 'url' - Check the price of a product on a specified website.\n"
                "!start_monitoring_price 'url' 'frequency' - Start monitoring a product's price at a specific interval (frequency in minutes).\n"
                "!stop_monitoring_price - Stop monitoring the product's price.\n"
                "!check_availability 'url' - Check availability for a restaurant or service.\n"
                "!start_monitoring_availability 'url' 'frequency' - Monitor availability at a specific interval.\n"
                "!stop_monitoring_availability - Stop monitoring availability.\n"
                "!stop_bot - Stop the bot.\n"
            )

            return help_message
        else:
            return "Invalid command."
