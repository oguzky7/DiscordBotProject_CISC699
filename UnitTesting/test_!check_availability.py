import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!check_availability.py
Purpose: Unit tests for the !check_availability command in the Discord bot.
"""

class TestCheckAvailabilityCommand(BaseTestSetup):

    @patch('control.AvailabilityControl.AvailabilityControl.receive_command')
    async def test_check_availability_success(self, mock_receive_command):
        """Test the check_availability command when it succeeds."""
        logging.info("Starting test: test_check_availability_success")

        mock_receive_command.return_value = "Available for booking."

        command = self.bot.get_command("check_availability")
        self.assertIsNotNone(command)

        await command(self.ctx, "https://example.com", "2024-09-30")
        expected_message = "Available for booking."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful availability check.")

    @patch('control.AvailabilityControl.AvailabilityControl.receive_command')
    async def test_check_availability_error(self, mock_receive_command):
        """Test the check_availability command when it encounters an error."""
        logging.info("Starting test: test_check_availability_error")

        mock_receive_command.return_value = "No availability found."

        command = self.bot.get_command("check_availability")
        self.assertIsNotNone(command)

        await command(self.ctx, "https://invalid-url.com", "2024-09-30")
        expected_message = "No availability found."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling during availability check.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
