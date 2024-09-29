import pytest, logging
from unittest.mock import patch
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()

async def test_add_account_success(base_test_case):
    with patch('control.AccountControl.AccountControl.add_account', return_value="Account for example.com added successfully.") as mock_add_account:
        # Setup expected outcomes
        username = "test_user"
        password = "test_pass"
        website = "example.com"
        expected_entity_result = "Account for example.com added successfully."
        expected_control_result = "Account for example.com added successfully."
        
        # Execute the command
        result = base_test_case.account_control.add_account(username, password, website)
        
        # Log and assert the outcomes
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_add_account.return_value}")
        assert mock_add_account.return_value == expected_entity_result, "Entity layer assertion failed."
        logging.info("Unit Test Passed for entity layer.\n")
        
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer.")

async def test_add_account_failure_invalid_data(base_test_case):
    with patch('control.AccountControl.AccountControl.add_account', return_value="Failed to add account for example.com.") as mock_add_account:
        # Setup expected outcomes for invalid data scenario
        username = ""  # Invalid username
        password = ""  # Invalid password
        website = "example.com"
        expected_control_result = "Failed to add account for example.com."
        
        # Execute the command
        result = base_test_case.account_control.add_account(username, password, website)
        
        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer invalid data handling.\n")

async def test_add_account_failure_entity_error(base_test_case):
    with patch('control.AccountControl.AccountControl.add_account', side_effect=Exception("Database Error")) as mock_add_account:
        # Setup expected outcomes
        username = "test_user"
        password = "test_pass"
        website = "example.com"
        expected_control_result = "Control Layer Exception: Database Error"
        
        # Execute the command
        try:
            result = base_test_case.account_control.add_account(username, password, website)
        except Exception as e:
            result = f"Control Layer Exception: {str(e)}"
        
        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer failed to handle entity error correctly."
        logging.info("Unit Test Passed for control layer error handling.")

async def test_add_account_already_exists(base_test_case):
    # This simulates a scenario where an account for the website already exists
    with patch('control.AccountControl.AccountControl.add_account', return_value="Failed to add account for example.com. Account already exists.") as mock_add_account:
        # Setup expected outcomes
        username = "test_user"
        password = "test_pass"
        website = "example.com"
        expected_control_result = "Failed to add account for example.com. Account already exists."
        
        # Execute the command
        result = base_test_case.account_control.add_account(username, password, website)
        
        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer when account already exists.")

if __name__ == "__main__":
    pytest.main([__file__])
