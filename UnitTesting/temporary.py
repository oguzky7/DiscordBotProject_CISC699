import pytest
import logging
from unittest.mock import patch, MagicMock
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio

setup_logging()

async def test_login_success(base_test_case):
    """Test that the login is successful when valid credentials are provided."""
    # Patch methods
    with patch('entity.BrowserEntity.BrowserEntity.login') as mock_login:
        with patch('control.AccountControl.AccountControl.fetch_account_by_website') as mock_fetch_account:
            # Setup mock return values
            mock_login.return_value = "Logged in to http://example.com successfully with username: sample_username"
            mock_fetch_account.return_value = ("sample_username", "sample_password")
            
            expected_entity_result = "Logged in to http://example.com successfully with username: sample_username"
            expected_control_result = f"Control Object Result: {expected_entity_result}"
            
            # Execute the command
            result = await base_test_case.browser_control.receive_command("login", site="example.com")
            
            # Assert results and logging
            logging.info(f"Entity Layer Expected: {expected_entity_result}")
            logging.info(f"Entity Layer Received: {mock_login.return_value}")
            assert mock_login.return_value == expected_entity_result, "Entity layer assertion failed."
            logging.info("Unit Test Passed for entity layer.\n")
            
            logging.info(f"Control Layer Expected: {expected_control_result}")
            logging.info(f"Control Layer Received: {result}")
            assert result == expected_control_result, "Control layer assertion failed."
            logging.info("Unit Test Passed for control layer.")

if __name__ == "__main__":
    pytest.main([__file__])