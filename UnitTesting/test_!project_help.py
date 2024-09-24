import logging, unittest
from unittest.mock import patch, AsyncMock, call
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!project_help.py
Purpose: This file contains unit tests for the !project_help command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the bot provides the correct help message and handles errors properly.
Tests:
- Positive: Simulates the !project_help command and verifies the correct help message is sent.
- Negative: Simulates an error scenario and ensures the error is handled gracefully.
"""

class TestProjectHelpCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    async def test_project_help_success(self, mock_parse_user_message):
        """Test the project help command when it successfully returns the help message."""
        logging.info("Starting test: test_project_help_success")
        mock_parse_user_message.return_value = ["project_help"]  # Mock the command parsing to return the command
        
        # Simulate calling the project_help command
        command = self.bot.get_command("project_help")
        self.assertIsNotNone(command, "project_help command is not registered.")  # Ensure the command is registered
        
        await command(self.ctx)
        
        # Define the expected help message from the module
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


        # Check if the correct help message was sent
        self.ctx.send.assert_called_with(help_message)
        logging.info("Verified that the correct help message was sent.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    async def test_project_help_error(self, mock_parse_user_message):
        """Test the project help command when it encounters an error during execution."""
        logging.info("Starting test: test_project_help_error")
        mock_parse_user_message.return_value = ["project_help"]  # Mock the command parsing to return the command

        # Simulate an error when sending the message
        self.ctx.send.side_effect = Exception("Error during project_help execution.")
        
        command = self.bot.get_command("project_help")
        self.assertIsNotNone(command, "project_help command is not registered.")  # Ensure the command is registered
        
        with self.assertRaises(Exception):
            await command(self.ctx)
        
        logging.info("Verified that an error occurred and was handled.")

if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
