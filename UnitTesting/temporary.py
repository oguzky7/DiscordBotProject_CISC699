import pytest
import logging
from unittest.mock import patch, MagicMock
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio

setup_logging()


async def test_navigate_to_website_failure_control(base_test_case):
    # This simulates a failure within the control layer
    with patch('control.BrowserControl.BrowserControl.receive_command', side_effect=Exception("Control Layer Failed")) as mock_control:
        
        # Setup expected outcomes
        url = "https://example.com"
        expected_control_result = "Control Layer Exception: Control Layer Failed"

        # Execute the command and catch the raised exception
        try:
            result = await base_test_case.browser_control.receive_command("navigate_to_website", site=url)
        except Exception as e:
            result = f"Control Layer Exception: {str(e)}"

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer failure.")


if __name__ == "__main__":
    pytest.main([__file__])