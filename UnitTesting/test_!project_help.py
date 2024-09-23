import logging, unittest
from test_init import BaseTestSetup, CustomTextTestRunner
from unittest.mock import call
"""
File: test_!project_help.py
Purpose: This file contains unit tests for the !project_help command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the bot provides the correct help message and handles errors properly.
Tests:
- Positive: Simulates the !project_help command and verifies the correct help message is sent.
- Negative: Simulates an error scenario and ensures the error is handled gracefully.
"""

class TestStopBotCommand(BaseTestSetup):
    
    async def test_project_help_success(self):
        """Test the project help command when it successfully returns the help message."""
        logging.info("Starting test: test_project_help_success")

        # Simulate calling the project_help command
        logging.info("Simulating the project_help command call.")
        command = self.bot.get_command("project_help")
        self.assertIsNotNone(command, "project_help command is not registered.")  # Ensure the command is registered
        await command(self.ctx)

        # Check both the control message and help message were sent
        expected_calls = [
            call('Command recognized, passing data to control.'),  # First message sent by the bot
            call(help_message)  # Second message: the actual help message
        ]
        self.ctx.send.assert_has_calls(expected_calls, any_order=False)  # Ensure the messages are sent in the correct order
        logging.info("Verified that both the control and help messages were sent.")


    async def test_project_help_error(self):
        """Test the project help command when it encounters an error during execution."""
        logging.info("Starting test: test_project_help_error")

        # Simulate calling the project_help command and an error occurring
        logging.info("Simulating the project_help command call.")
        self.ctx.send.side_effect = Exception("Error during project_help execution.")  # Simulate an error

        command = self.bot.get_command("project_help")
        self.assertIsNotNone(command, "project_help command is not registered.")  # Ensure the command is registered
        
        # Act & Assert: Expect the exception to be raised
        with self.assertRaises(Exception):
            await command(self.ctx)

        logging.info("Verified that an error occurred and was handled.")

# Expected help message
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

if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
