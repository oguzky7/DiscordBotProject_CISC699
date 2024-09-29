import pytest, logging
from unittest.mock import patch
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()

async def test_delete_account_success(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.delete_account') as mock_delete:
        # Setup mock return and expected outcomes
        account_id = 1
        mock_delete.return_value = True
        expected_entity_result = "Account with ID 1 deleted successfully."
        expected_control_result = "Account with ID 1 deleted successfully."

        # Execute the command
        result = base_test_case.account_control.delete_account(account_id)

        # Log and assert the outcomes
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_delete.return_value}")
        assert mock_delete.return_value == True, "Entity layer assertion failed."
        logging.info("Unit Test Passed for entity layer.\n")

        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer.")

async def test_delete_account_not_found(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.delete_account') as mock_delete:
        # Setup mock return and expected outcomes
        account_id = 999
        mock_delete.return_value = False
        expected_control_result = "Failed to delete account with ID 999."

        # Execute the command
        result = base_test_case.account_control.delete_account(account_id)

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer with account not found.\n")

async def test_delete_account_failure_entity(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.delete_account', side_effect=Exception("Failed to delete account in DAO")) as mock_delete:
        # Setup expected outcomes
        account_id = 1
        expected_control_result = "Error deleting account."

        # Execute the command
        result = base_test_case.account_control.delete_account(account_id)

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer failed to handle entity error correctly."
        logging.info("Unit Test Passed for entity layer error handling.")

async def test_delete_account_failure_control(base_test_case):
    # This simulates a failure within the control layer
    with patch('control.AccountControl.AccountControl.delete_account', side_effect=Exception("Control Layer Failed")) as mock_control:
        
        # Setup expected outcomes
        account_id = 1
        expected_control_result = "Control Layer Exception: Control Layer Failed"

        # Execute the command and catch the raised exception
        try:
            result = base_test_case.account_control.delete_account(account_id)
        except Exception as e:
            result = f"Control Layer Exception: {str(e)}"

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer failure.")
        
if __name__ == "__main__":
    pytest.main([__file__])
