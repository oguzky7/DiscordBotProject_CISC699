import logging, unittest
from unittest.mock import patch, AsyncMock
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!start_monitoring_price.py
Purpose: This file contains unit tests for the !start_monitoring_price command in the Discord bot.
The tests validate both successful and error scenarios, ensuring that the bot starts monitoring prices or handles errors gracefully.

Tests:
- Positive: Simulates the !start_monitoring_price command and verifies the monitoring is initiated successfully.
- Negative: Simulates an error during the initiation of price monitoring and ensures it is handled gracefully.
"""

class TestStartMonitoringPriceCommand(BaseTestSetup):
    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_start_monitoring_price_success(self, mock_receive_command, mock_parse_user_message):
        """Test the start_monitoring_price command when it succeeds."""
        logging.info("Starting test: test_start_monitoring_price_success")

        # Mock the parsed message to return the expected command and parameters
        mock_parse_user_message.return_value = ["start_monitoring_price", "https://example.com", "20"]

        # Simulate successful price monitoring start
        mock_receive_command.return_value = "Monitoring started for https://example.com."

        # Retrieve the start_monitoring_price command from the bot
        command = self.bot.get_command("start_monitoring_price")
        self.assertIsNotNone(command)

        # Call the command without explicit parameters due to mocked GlobalState
        await command(self.ctx)

        # Verify the expected message was sent to the user
        expected_message = "Monitoring started for https://example.com."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful price monitoring start.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_start_monitoring_price_error(self, mock_receive_command, mock_parse_user_message):
        """Test the start_monitoring_price command when it encounters an error."""
        logging.info("Starting test: test_start_monitoring_price_error")

        # Mock the parsed message to simulate the command being executed with an invalid URL
        mock_parse_user_message.return_value = ["start_monitoring_price", "https://invalid-url.com", "20"]

        # Simulate a failure during price monitoring start
        mock_receive_command.return_value = "Failed to start monitoring"

        # Retrieve the start_monitoring_price command from the bot
        command = self.bot.get_command("start_monitoring_price")
        self.assertIsNotNone(command)

        # Call the command without explicit parameters due to mocked GlobalState
        await command(self.ctx)

        # Verify the correct error message is sent
        expected_message = "Failed to start monitoring"
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling during price monitoring start.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
