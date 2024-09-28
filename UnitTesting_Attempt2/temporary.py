import unittest
from unittest.mock import patch, AsyncMock
import logging
import sys, os, discord, logging, unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Import your classes
from control.BrowserControl import BrowserControl

class TestBrowserFunctionality(unittest.TestCase):

    def setUp(self):
        """Set up BrowserControl and context for each test."""
        self.control = BrowserControl()
        self.ctx = AsyncMock()  # Mocking the context to use in the control object

    @patch('entity.BrowserEntity.BrowserEntity.launch_browser')
    def test_launch_browser_failure_entity(self, mock_launch):
        """Test failure to launch browser due to an internal error in the entity layer."""
        internal_error_message = "Failed to launch browser: Internal error"
        mock_launch.side_effect = Exception(internal_error_message)  # Simulate an exception on error
        expected_control_result = f"Control Layer Exception: {internal_error_message}"

        # Execute command
        result = self.control.receive_command("launch_browser")

        # Check if the control layer returns the correct error message
        logging.info(f"Entity Layer Expected Failure: {internal_error_message}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_control_result, "Control layer failed to report entity error correctly.")
        logging.info("Unit Test Passed for entity layer error handling.")

if __name__ == '__main__':
    unittest.main()
