import logging, unittest
from unittest.mock import patch, AsyncMock
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!stop_monitoring_price.py
Purpose: This file contains unit tests for the !stop_monitoring_price command in the Discord bot.
The tests validate both successful and error scenarios, ensuring that the bot stops monitoring prices or handles errors gracefully.
"""

class TestStopMonitoringPriceCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_stop_monitoring_price_no_active_session(self, mock_receive_command, mock_parse_user_message):
        """Test the stop_monitoring_price command when no active monitoring session exists."""
        logging.info("Starting test: test_stop_monitoring_price_no_active_session")

        # Simulate scenario with no active price monitoring session
        mock_parse_user_message.return_value = ["stop_monitoring_price"]
        mock_receive_command.return_value = "There was no active price monitoring session. Nothing to stop."

        # Retrieve the stop_monitoring_price command from the bot
        command = self.bot.get_command("stop_monitoring_price")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx)

        # Verify the expected message was sent to the user
        expected_message = "There was no active price monitoring session. Nothing to stop."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified no active session stop scenario.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_stop_monitoring_price_success_with_results(self, mock_receive_command, mock_parse_user_message):
        """Test the stop_monitoring_price command when monitoring was active and results are returned."""
        logging.info("Starting test: test_stop_monitoring_price_success_with_results")

        # Simulate stopping monitoring and receiving results
        mock_parse_user_message.return_value = ["stop_monitoring_price"]
        mock_receive_command.return_value = "Results for price monitoring:\nPrice: $199.99\nPrice monitoring stopped successfully!"

        # Retrieve the stop_monitoring_price command from the bot
        command = self.bot.get_command("stop_monitoring_price")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx)

        # Verify the expected message was sent to the user
        expected_message = "Results for price monitoring:\nPrice: $199.99\nPrice monitoring stopped successfully!"
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful stop with results.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.PriceControl.PriceControl.receive_command')
    async def test_stop_monitoring_price_error(self, mock_receive_command, mock_parse_user_message):
        """Test the stop_monitoring_price command when it encounters an error."""
        logging.info("Starting test: test_stop_monitoring_price_error")

        # Simulate a failure during price monitoring stop
        mock_parse_user_message.return_value = ["stop_monitoring_price"]
        mock_receive_command.return_value = "Error stopping price monitoring"

        # Retrieve the stop_monitoring_price command from the bot
        command = self.bot.get_command("stop_monitoring_price")
        self.assertIsNotNone(command)

        # Call the command
        await command(self.ctx)

        # Verify the correct error message is sent
        expected_message = "Error stopping price monitoring"
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling during price monitoring stop.")

if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
