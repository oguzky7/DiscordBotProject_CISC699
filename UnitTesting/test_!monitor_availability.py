import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!monitor_availability.py
Purpose: Unit tests for the !monitor_availability command in the Discord bot.
"""

class TestMonitorAvailabilityCommand(BaseTestSetup):

    @patch('control.AvailabilityControl.AvailabilityControl.receive_command')
    async def test_monitor_availability_success(self, mock_receive_command):
        """Test the monitor_availability command when it succeeds."""
        logging.info("Starting test: test_monitor_availability_success")

        mock_receive_command.return_value = "Monitoring started for https://example.com."

        command = self.bot.get_command("start_monitoring_availability")
        self.assertIsNotNone(command)

        await command(self.ctx, "https://example.com", "2024-09-30", 15)
        expected_message = "Monitoring started for https://example.com."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful availability monitoring start.")

    @patch('control.AvailabilityControl.AvailabilityControl.receive_command')
    async def test_monitor_availability_error(self, mock_receive_command):
        """Test the monitor_availability command when it encounters an error."""
        logging.info("Starting test: test_monitor_availability_error")

        mock_receive_command.return_value = "Failed to start monitoring."

        command = self.bot.get_command("start_monitoring_availability")
        self.assertIsNotNone(command)

        await command(self.ctx, "https://invalid-url.com", "2024-09-30", 15)
        expected_message = "Failed to start monitoring."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling during availability monitoring.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
