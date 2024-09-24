import logging, unittest
from unittest.mock import patch, AsyncMock
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!navigate_to_website.py
Purpose: This file contains unit tests for the !navigate_to_website command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the bot navigates to the website correctly or handles errors.
"""

class TestNavigateToWebsiteCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('entity.BrowserEntity.BrowserEntity.navigate_to_website')

    async def test_navigate_to_website_success(self, mock_receive_command, mock_parse_user_message):
        """Test the navigate_to_website command when it succeeds."""
        logging.info("Starting test: test_navigate_to_website_success")

        # Mock the parsed message to return the expected command and URL
        mock_parse_user_message.return_value = ["navigate_to_website", "https://example.com"]
        
        # Simulate successful navigation
        mock_receive_command.return_value = "Navigated to https://example.com."

        # Retrieve the navigate_to_website command from the bot
        command = self.bot.get_command("navigate_to_website")
        self.assertIsNotNone(command)

        # Call the command without arguments (since GlobalState is mocked)
        await command(self.ctx)

        # Verify the expected message was sent to the user
        expected_message = "Navigated to https://example.com."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful website navigation.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('entity.BrowserEntity.BrowserEntity.navigate_to_website')
    async def test_navigate_to_website_error(self, mock_receive_command, mock_parse_user_message):
        """Test the navigate_to_website command when it encounters an error."""
        logging.info("Starting test: test_navigate_to_website_error")

        # Mock the parsed message to return the expected command and URL
        mock_parse_user_message.return_value = ["navigate_to_website", "https://invalid-url.com"]
        
        # Simulate a failure during navigation
        mock_receive_command.side_effect = Exception("Failed to navigate to the website.")

        # Retrieve the navigate_to_website command from the bot
        command = self.bot.get_command("navigate_to_website")
        self.assertIsNotNone(command)

        # Call the command without arguments (since GlobalState is mocked)
        await command(self.ctx)

        # Verify the correct error message is sent
        self.ctx.send.assert_called_with("Failed to navigate to the website.")  # Error message handled
        logging.info("Verified error handling during website navigation.")

if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
