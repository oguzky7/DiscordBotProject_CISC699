import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!start_monitoring_price.py
Purpose: This file contains unit tests for the !start_monitoring_price command in the Discord bot.
The tests validate both successful and error scenarios, ensuring that the bot starts monitoring prices or handles errors.
"""

class TestStartMonitoringPriceCommand(BaseTestSetup):
    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_start_monitoring_price_success(self, mock_receive_command):
        """Test the start_monitoring_price command when it succeeds."""
        logging.info("Starting test: test_start_monitoring_price_success")

        # Simulate successful price monitoring start
        mock_receive_command.return_value = "Monitoring started for https://example.com."

        # Retrieve the start_monitoring_price command from the bot
        command = self.bot.get_command("start_monitoring_price")
        self.assertIsNotNone(command)

        # Call the command with a valid URL and frequency
        await command(self.ctx, "https://example.com", 20)

        # Verify the expected message was sent to the user
        expected_message = "Monitoring started for https://example.com."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful price monitoring start.")

    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_start_monitoring_price_error(self, mock_receive_command):
        """Test the start_monitoring_price command when it encounters an error."""
        logging.info("Starting test: test_start_monitoring_price_error")

        # Simulate a failure during price monitoring start
        mock_receive_command.return_value = "Failed to start monitoring"

        # Retrieve the start_monitoring_price command from the bot
        command = self.bot.get_command("start_monitoring_price")
        self.assertIsNotNone(command)

        # Call the command with an invalid URL
        await command(self.ctx, "https://invalid-url.com", 20)

        # Verify the correct error message is sent
        self.ctx.send.assert_called_with("Failed to start monitoring")
        logging.info("Verified error handling during price monitoring start.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
