import pytest
import logging
from unittest.mock import patch, MagicMock
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio

setup_logging()



async def test_login_control_layer_failure(base_test_case):
    """Test that the control layer handles an unexpected failure or exception."""
    with patch('control.AccountControl.AccountControl.fetch_account_by_website') as mock_fetch_account:
        # Simulate an exception being raised in the control layer
        mock_fetch_account.side_effect = Exception("Control layer failure during account fetch.")
        
        expected_result = "Control Layer Exception: Control layer failure during account fetch."
        
        # Execute the command
        result = await base_test_case.browser_control.receive_command("login", site="example.com")
        
        # Assert results and logging
        logging.info(f"Control Layer Expected: {expected_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_result, "Control layer failed to handle control layer exception."
        logging.info("Unit Test Passed for control layer failure handling.")




if __name__ == "__main__":
    pytest.main([__file__])