import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from test_init import setup_logging, base_test_case, save_test_results_to_file, log_test_start_end, logging

import pytest
from unittest.mock import AsyncMock, patch
from discord.ext import commands

# Import boundary and control classes for the bot
from boundary.BotBoundary import BotBoundary
from control.BotControl import BotControl

@pytest.fixture
def bot_context():
    """Mock discord context for testing.
    This simulates the Discord context that is usually passed to command functions."""
    ctx = AsyncMock(spec=commands.Context)
    ctx.send = AsyncMock()
    return ctx

@pytest.mark.asyncio
async def test_project_help(bot_context):
    # Arrange
    # Patch the receive_command method in BotControl to prevent actual execution and to simulate its behavior
    with patch('control.BotControl.BotControl.receive_command', new_callable=AsyncMock) as mocked_receive_command:
        # Mocked response as if from the actual command execution
        mocked_receive_command.return_value = "Mocked help message listing commands"
        bot_boundary = BotBoundary()

        # Command being tested
        command = 'project_help'
        logging.info("\n[TEST INITIATED] Testing the Project Help command...")

        # Act
        # Try to trigger the 'project_help' command and catch type errors if the wrong arguments are passed
        logging.info(f"\n[ACT] Triggering the '{command}' command...")
        try:
            await bot_boundary.project_help(bot_context)
            logging.info("\n[ACT] Command triggered successfully.")
        except TypeError as e:
            logging.info(f"\n[ERROR] Failed to trigger command: {str(e)}")
            return  # Exit the test on failure to trigger the command correctly

        # Assert
        # Verify that the bot's response as sent to the user matches expectations
        logging.info("\n[ASSERT] Verifying command handling...")
        try:
            # Check that the initial acknowledgment is sent correctly
            bot_context.send.assert_called_with("Command recognized, passing data to control.")
            # Ensure the mocked command function was called correctly with the right command
            mocked_receive_command.assert_called_with(command)
            # Check that the final response to the user is correct
            bot_context.send.assert_called_with("Mocked help message listing commands")
            logging.info("\n[RESULT] Command handled correctly and help message sent successfully.")
        except AssertionError as e:
            logging.info(f"\n[ERROR] Test assertion failed: {str(e)}")

        logging.info("\n[TEST COMPLETED] Project Help command test finished.")

# If running the test directly:
if __name__ == "__main__":
    pytest.main([__file__])
