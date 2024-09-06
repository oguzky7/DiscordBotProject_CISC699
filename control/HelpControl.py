class HelpControl:
    def get_help_message(self):
        """Returns a list of available bot commands."""
        return (
            "Here are the available commands:\n"
            "!project_help - Get help on available commands.\n"
            "!chat_with_bot - Say hi to the bot.\n"
            "!login_to_website - Log in to a website.\n"
            "!launch_browser - Launch the browser.\n"
            "!close_browser - Close the browser.\n"
            "!navigate_to_website - Navigate to a website.\n"
            "!track_price - Track a product price.\n"
            "!check_price - Check the price of a product.\n"
            "!check_availability - Check the availability of a product.\n"
            "!stop_tracking - Stop tracking a product.\n"
            "!receive_notifications - Receive notifications for price changes.\n"
            "!extract_data - Export data to Excel or HTML.\n"
            "!stop - Stop the bot.\n"
        )
