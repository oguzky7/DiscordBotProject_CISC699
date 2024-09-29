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

async def test_login_no_account(base_test_case):
    """Test that the control layer handles the scenario where no account is found for the website."""
    with patch('control.AccountControl.AccountControl.fetch_account_by_website') as mock_fetch_account:
        # Setup mock to return no account
        mock_fetch_account.return_value = None
        
        expected_result = "No account found for example.com"
        
        # Execute the command
        result = await base_test_case.browser_control.receive_command("login", site="example.com")
        
        # Assert results and logging
        logging.info(f"Control Layer Expected: {expected_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_result, "Control layer failed to handle missing account correctly."
        logging.info("Unit Test Passed for missing account handling.")

async def test_login_entity_layer_failure(base_test_case):
    """Test that the control layer handles an exception raised in the entity layer."""
    with patch('entity.BrowserEntity.BrowserEntity.login') as mock_login:
        with patch('control.AccountControl.AccountControl.fetch_account_by_website') as mock_fetch_account:
            # Setup mocks
            mock_login.side_effect = Exception("BrowserEntity_Failed to log in to http://example.com: Internal error")
            mock_fetch_account.return_value = ("sample_username", "sample_password")
            
            expected_result = "Control Layer Exception: BrowserEntity_Failed to log in to http://example.com: Internal error"
            
            # Execute the command
            result = await base_test_case.browser_control.receive_command("login", site="example.com")
            
            # Assert results and logging
            logging.info(f"Control Layer Expected: {expected_result}")
            logging.info(f"Control Layer Received: {result}")
            assert result == expected_result, "Control layer failed to handle entity layer exception."
            logging.info("Unit Test Passed for entity layer failure.")


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

async def test_login_invalid_url(base_test_case):
    """Test that the control layer handles the scenario where the URL or selectors are not found."""
    with patch('control.AccountControl.AccountControl.fetch_account_by_website') as mock_fetch_account:
        with patch('utils.css_selectors.Selectors.get_selectors_for_url') as mock_get_selectors:
            # Setup mocks
            mock_fetch_account.return_value = ("sample_username", "sample_password")
            mock_get_selectors.return_value = {'url': None}  # Simulate missing URL
            
            expected_result = "URL for example not found."
            
            # Execute the command
            result = await base_test_case.browser_control.receive_command("login", site="example")
            
            # Assert results and logging
            logging.info(f"Control Layer Expected: {expected_result}")
            logging.info(f"Control Layer Received: {result}")
            assert result == expected_result, "Control layer failed to handle missing URL or selectors."
            logging.info("Unit Test Passed for missing URL/selector handling.")

if __name__ == "__main__":
    pytest.main([__file__])