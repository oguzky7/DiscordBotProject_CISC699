import logging, unittest
from unittest.mock import patch, AsyncMock
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!login.py
Purpose: Unit tests for the !login command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the bot correctly logs in to a specified website or handles errors gracefully.

Tests:
- Positive: Simulates the !login command and verifies the login is successful.
- Negative: Simulates an error during login and ensures it is handled gracefully.
"""

class TestLoginCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.LoginControl.LoginControl.receive_command')
    async def test_login_success(self, mock_receive_command, mock_parse_user_message):
        """Test the login command when it succeeds."""
        logging.info("Starting test: test_login_success")

        # Mock the parsed message to return the expected command and arguments
        mock_parse_user_message.return_value = ["login", "ebay"]

        # Simulate a successful login
        mock_receive_command.return_value = "Login successful."

        # Retrieve the login command from the bot
        command = self.bot.get_command("login")
        self.assertIsNotNone(command)

        # Call the command without arguments (since GlobalState is mocked)
        await command(self.ctx)

        # Verify the expected message was sent to the user
        expected_message = "Login successful."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful login.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.LoginControl.LoginControl.receive_command')
    async def test_login_error(self, mock_receive_command, mock_parse_user_message):
        """Test the login command when it encounters an error."""
        logging.info("Starting test: test_login_error")

        # Mock the parsed message to return the expected command and arguments
        mock_parse_user_message.return_value = ["login", "nonexistent.com"]

        # Simulate a failure during login
        mock_receive_command.return_value = "Failed to login. No account found."

        # Retrieve the login command from the bot
        command = self.bot.get_command("login")
        self.assertIsNotNone(command)

        # Call the command without arguments (since GlobalState is mocked)
        await command(self.ctx)

        # Verify the correct error message is sent
        expected_message = "Failed to login. No account found."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling during login.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
