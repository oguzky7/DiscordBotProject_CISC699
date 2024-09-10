class HelpControl:
    def get_help_message(self):
        """Returns a list of available bot commands."""
        return (
            "Here are the available commands:\n"
            "!project_help - Get help on available commands.\n"
            "!login 'website' - Log in to a website.\n"
            "!launch_browser - Launch the browser.\n"
            "!close_browser - Close the browser.\n"
            "!navigate_to_website - Navigate to a website.\n"
            "!get_price - Check the price of a product.\n"
            "!monitor_price - monitor a product price.\n"
            "!stop_monitoring - Stop monitoring a product.\n"
            "!check_availability - Check the availability in a restaurant.\n"
            "!monitor_availability - Monitor the availability in a restaurant.\n"
            "!stop_monitoring_availability - Stop monitoring availibility.\n"
            "!stop_bot - Stop the bot.\n"
            "##!receive_notifications - Receive notifications for price changes.\n"
            "##!extract_data - Export data to Excel or HTML.\n"
        )
