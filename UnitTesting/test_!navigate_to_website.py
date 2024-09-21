import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!navigate_to_website.py
Purpose: This file contains unit tests for the !navigate_to_website command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the bot navigates to the website correctly or handles errors.
"""

class TestNavigateToWebsiteCommand(BaseTestSetup):

    @patch('entity.BrowserEntity.BrowserEntity.navigate_to_website')
    async def test_navigate_to_website_success(self, mock_navigate_to_website):
        """Test the navigate_to_website command when it succeeds."""
        logging.info("Starting test: test_navigate_to_website_success")

        # Simulate successful navigation
        mock_navigate_to_website.return_value = "Navigated to https://example.com."

        # Retrieve the navigate_to_website command from the bot
        command = self.bot.get_command("navigate_to_website")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx, "https://example.com")

        # Verify the expected message was sent to the user
        expected_message = "Navigated to https://example.com."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful website navigation.")

    @patch('entity.BrowserEntity.BrowserEntity.navigate_to_website')
    async def test_navigate_to_website_error(self, mock_navigate_to_website):
        """Test the navigate_to_website command when it encounters an error."""
        logging.info("Starting test: test_navigate_to_website_error")

        # Simulate a failure during navigation
        mock_navigate_to_website.side_effect = Exception("Failed to navigate to the website.")

        # Retrieve the navigate_to_website command from the bot
        command = self.bot.get_command("navigate_to_website")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx, "https://invalid-url.com")

        # Verify the correct error message is sent
        self.ctx.send.assert_called_with("Failed to navigate to the website.")  # Error message handled
        logging.info("Verified error handling during website navigation.")

if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
