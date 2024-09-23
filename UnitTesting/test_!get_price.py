import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!get_price.py
Purpose: This file contains unit tests for the !get_price command in the Discord bot.
The tests validate both successful and error scenarios, ensuring that the price is fetched correctly or errors are handled.
"""

class TestGetPriceCommand(BaseTestSetup):
    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_get_price_success(self, mock_receive_command):
        """Test the get_price command when it succeeds."""
        logging.info("Starting test: test_get_price_success")

        # Simulate successful price fetch
        mock_receive_command.return_value = "Price: $199.99"

        # Retrieve the get_price command from the bot
        command = self.bot.get_command("get_price")
        self.assertIsNotNone(command)

        # Call the command with a valid URL
        await command(self.ctx, "https://example.com")

        # Verify the expected message was sent to the user
        expected_message = "Price: $199.99"
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful price fetch.")

    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_get_price_error(self, mock_receive_command):
        """Test the get_price command when it encounters an error."""
        logging.info("Starting test: test_get_price_error")

        # Simulate a failure during price fetch
        mock_receive_command.return_value = "Failed to fetch price"

        # Retrieve the get_price command from the bot
        command = self.bot.get_command("get_price")
        self.assertIsNotNone(command)

        # Call the command with an invalid URL
        await command(self.ctx, "https://invalid-url.com")

        # Verify the correct error message is sent
        self.ctx.send.assert_called_with("Failed to fetch price")
        logging.info("Verified error handling during price fetch.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
