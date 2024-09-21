import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!launch_browser.py
Purpose: This file contains unit tests for the !launch_browser command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the browser launches properly or errors are handled gracefully.

Tests:
- Positive: Simulates the !launch_browser command and verifies the browser launches correctly.
- Negative: Simulates an error during browser launch and ensures it is handled gracefully.
"""

class TestLaunchBrowserCommand(BaseTestSetup):

    @patch('entity.BrowserEntity.BrowserEntity.launch_browser')
    async def test_launch_browser_success(self, mock_launch_browser):
        """Test the launch_browser command when it succeeds."""
        logging.info("Starting test: test_launch_browser_success")

        # Simulate successful browser launch
        mock_launch_browser.return_value = "Browser launched."

        # Retrieve the launch_browser command from the bot
        command = self.bot.get_command("launch_browser")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx)

        # Verify the expected message was sent to the user
        expected_message = "Browser launched."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful browser launch.")

    @patch('entity.BrowserEntity.BrowserEntity.launch_browser')
    async def test_launch_browser_error(self, mock_launch_browser):
        """Test the launch_browser command when it encounters an error."""
        logging.info("Starting test: test_launch_browser_error")

        # Simulate a failure during browser launch
        mock_launch_browser.side_effect = Exception("Failed to launch browser")

        # Retrieve the launch_browser command from the bot
        command = self.bot.get_command("launch_browser")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx)

        # Verify the correct error message is sent
        self.ctx.send.assert_called_with("Failed to launch browser")  # Error message handled
        logging.info("Verified error handling during browser launch.")


if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
