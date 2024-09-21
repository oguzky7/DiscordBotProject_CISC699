import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!close_browser.py
Purpose: This file contains unit tests for the !close_browser command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the browser closes properly or errors are handled gracefully.

Tests:
- Positive: Simulates the !close_browser command and verifies the browser closes correctly.
- Negative: Simulates an error during browser closure and ensures it is handled gracefully.
"""

class TestCloseBrowserCommand(BaseTestSetup):

    @patch('entity.BrowserEntity.BrowserEntity.close_browser')
    async def test_close_browser_success(self, mock_close_browser):
        """Test the close_browser command when it succeeds."""
        logging.info("Starting test: test_close_browser_success")

        # Simulate successful browser closure
        mock_close_browser.return_value = "Browser closed."

        # Retrieve the close_browser command from the bot
        command = self.bot.get_command("close_browser")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx)

        # Verify the expected message was sent to the user
        expected_message = "Browser closed."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful browser closure.")

    @patch('entity.BrowserEntity.BrowserEntity.close_browser')
    async def test_close_browser_error(self, mock_close_browser):
        """Test the close_browser command when it encounters an error."""
        logging.info("Starting test: test_close_browser_error")

        # Simulate a failure during browser closure
        mock_close_browser.side_effect = Exception("Failed to close browser")

        # Retrieve the close_browser command from the bot
        command = self.bot.get_command("close_browser")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx)

        # Verify the correct error message is sent
        self.ctx.send.assert_called_with("Failed to close browser")  # Error message handled
        logging.info("Verified error handling during browser closure.")


if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
