import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!stop_monitoring_availability.py
Purpose: Unit tests for the !stop_monitoring_availability command in the Discord bot.
"""

class TestStopMonitoringAvailabilityCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.AvailabilityControl.AvailabilityControl.receive_command')
    async def test_stop_monitoring_availability_no_active_session(self, mock_receive_command, mock_parse_user_message):
        """Test the stop_monitoring_availability command when no active session exists."""
        logging.info("Starting test: test_stop_monitoring_availability_no_active_session")

        # Mock the parsed message to return the expected command and arguments
        mock_parse_user_message.return_value = ["stop_monitoring_availability"]

        # Simulate no active session scenario
        mock_receive_command.return_value = "There was no active availability monitoring session."

        command = self.bot.get_command("stop_monitoring_availability")
        self.assertIsNotNone(command)

        # Call the command without arguments (since GlobalState is mocked)
        await command(self.ctx)

        expected_message = "There was no active availability monitoring session."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified no active session stop scenario.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.AvailabilityControl.AvailabilityControl.receive_command')
    async def test_stop_monitoring_availability_success(self, mock_receive_command, mock_parse_user_message):
        """Test the stop_monitoring_availability command when it succeeds."""
        logging.info("Starting test: test_stop_monitoring_availability_success")

        # Mock the parsed message to return the expected command and arguments
        mock_parse_user_message.return_value = ["stop_monitoring_availability"]

        # Simulate successful stopping of monitoring
        mock_receive_command.return_value = "Availability monitoring stopped successfully."

        command = self.bot.get_command("stop_monitoring_availability")
        self.assertIsNotNone(command)

        # Call the command without arguments (since GlobalState is mocked)
        await command(self.ctx)

        expected_message = "Availability monitoring stopped successfully."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful availability monitoring stop.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
