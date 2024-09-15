import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
from unittest.mock import MagicMock, AsyncMock
from boundary.StopBoundary import StopBoundary  # Import StopBoundary to test
from control.StopControl import StopControl
import logging

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class CustomTextTestResult(unittest.TextTestResult):
    """Custom test result to output 'Unit test passed' instead of 'ok'."""
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write("Unit test passed\n")  # Custom success message
        self.stream.flush()


class CustomTextTestRunner(unittest.TextTestRunner):
    """Custom test runner that uses the custom result class."""
    resultclass = CustomTextTestResult


class TestStopBot(unittest.IsolatedAsyncioTestCase):

    async def asyncSetUp(self):
        # Create a mock for the bot and the context
        self.bot_mock = MagicMock()  # Mock for the bot
        self.ctx_mock = AsyncMock()  # AsyncMock for the context (Discord's ctx)

        # Create a mock for StopControl
        self.stop_control_mock = AsyncMock(spec=StopControl)
        
        # Initialize StopBoundary with the bot mock
        self.stop_boundary = StopBoundary(self.bot_mock)
        self.stop_boundary.control = self.stop_control_mock  # Replace the control with the mock

        logging.info("Test setup complete: Initialized mocks for bot, ctx, and control.")

    async def test_stop_bot_success(self):
        logging.info("Starting test: test_stop_bot_success")
        
        # Arrange
        self.stop_control_mock.stop_bot.return_value = "Bot stopped successfully."
        logging.info("Simulated successful bot stop in the mock.")

        # Act
        await StopBoundary.stop_bot(self.stop_boundary, self.ctx_mock)
        logging.info("Called stop_bot method on StopBoundary.")

        # Assert
        self.ctx_mock.send.assert_called_with("Command recognized, taking action")
        logging.info("Verified that ctx.send was called with the expected message.")
        
        self.stop_control_mock.stop_bot.assert_called_once_with(self.ctx_mock, self.bot_mock)
        logging.info("Verified that stop_bot in StopControl was called with the correct parameters.")

    async def test_stop_bot_error(self):
        logging.info("Starting test: test_stop_bot_error")

        # Arrange
        self.stop_control_mock.stop_bot.side_effect = Exception("Error stopping bot")
        logging.info("Simulated error in stop_bot mock.")

        # Act & Assert
        with self.assertRaises(Exception):
            await StopBoundary.stop_bot(self.stop_boundary, self.ctx_mock)

        logging.info("Error scenario handled correctly with an exception being raised.")

        # Ensure ctx.send was still called with the recognition message
        self.ctx_mock.send.assert_called_with("Command recognized, taking action")
        logging.info("Verified that ctx.send was still called despite the error.")
        
        self.stop_control_mock.stop_bot.assert_called_once_with(self.ctx_mock, self.bot_mock)
        logging.info("Verified that stop_bot in StopControl was called even during error scenario.")


if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
