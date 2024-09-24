import logging, unittest
from unittest.mock import AsyncMock, patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!stop_bot.py
Purpose: This file contains unit tests for the !stop_bot command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the bot correctly shuts down or handles errors during shutdown.
Tests:
- Positive: Simulates the !stop_bot command and verifies the bot shuts down correctly.
- Negative: Simulates an error during shutdown and ensures it is handled gracefully.
"""

class TestStopBotCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.StopControl.StopControl.receive_command', new_callable=AsyncMock)
    async def test_stop_bot_success(self, mock_receive_command, mock_parse_user_message):
        """Test the stop bot command when it successfully shuts down."""
        logging.info("Starting test: test_stop_bot_success")

        # Setup mocks
        mock_receive_command.return_value = "The bot is shutting down..."
        mock_parse_user_message.return_value = ["stop_bot"]
        
        # Simulate calling the stop_bot command
        command = self.bot.get_command("stop_bot")
        self.assertIsNotNone(command, "stop_bot command is not registered.")
        await command(self.ctx)
        
        # Verify the message was sent before shutdown is initiated
        self.ctx.send.assert_called_once_with("Command recognized, passing data to control.")
        logging.info("Verified that the shutdown message was sent to the user.")

        # Ensure bot.close() is called
        mock_receive_command.assert_called_once()
        logging.info("Verified that the bot's close method was called once.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('control.StopControl.StopControl.receive_command', new_callable=AsyncMock)
    async def test_stop_bot_error(self, mock_receive_command, mock_parse_user_message):
        """Test the stop bot command when it encounters an error during shutdown."""
        logging.info("Starting test: test_stop_bot_error")

        # Setup mocks
        exception_message = "Error stopping bot"
        mock_receive_command.side_effect = Exception(exception_message)
        mock_parse_user_message.return_value = ["stop_bot"]

        # Simulate calling the stop_bot command
        command = self.bot.get_command("stop_bot")
        self.assertIsNotNone(command, "stop_bot command is not registered.")

        with self.assertRaises(Exception) as context:
            await command(self.ctx)
        
        # Verify that the correct error message is sent
        self.ctx.send.assert_called_with('Command recognized, passing data to control.')
        self.assertTrue(exception_message in str(context.exception))
        logging.info("Verified error handling during bot shutdown.")
        
        # Verify that the close method was still attempted
        mock_receive_command.assert_called_once_with("stop_bot", self.ctx)
        logging.info("Verified that the bot's close method was attempted even though it raised an error.")

if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
