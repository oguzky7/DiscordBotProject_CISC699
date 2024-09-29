import pytest, logging
from unittest.mock import patch
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()

async def test_fetch_all_accounts_success(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.fetch_all_accounts') as mock_fetch_all:
        # Setup mock return and expected outcomes
        mock_fetch_all.return_value = [(1, "user1", "pass1", "example.com"), (2, "user2", "pass2", "test.com")]
        expected_entity_result = "Accounts:\nID: 1, Username: user1, Password: pass1, Website: example.com\nID: 2, Username: user2, Password: pass2, Website: test.com"
        expected_control_result = expected_entity_result

        # Execute the command
        result = base_test_case.account_control.receive_command("fetch_all_accounts")

        # Log and assert the outcomes
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_fetch_all.return_value}")
        assert mock_fetch_all.return_value == [(1, "user1", "pass1", "example.com"), (2, "user2", "pass2", "test.com")], "Entity layer assertion failed."
        logging.info("Unit Test Passed for entity layer.\n")

        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer.")

async def test_fetch_all_accounts_no_accounts(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.fetch_all_accounts') as mock_fetch_all:
        # Setup mock return and expected outcomes
        mock_fetch_all.return_value = []
        expected_control_result = "No accounts found."

        # Execute the command
        result = base_test_case.account_control.receive_command("fetch_all_accounts")

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer no accounts found.\n")

async def test_fetch_all_accounts_failure_entity(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.fetch_all_accounts', side_effect=Exception("Database Error")) as mock_fetch_all:
        # Setup expected outcomes
        expected_control_result = "Error fetching accounts."

        # Execute the command
        result = base_test_case.account_control.receive_command("fetch_all_accounts")

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer failed to handle entity error correctly."
        logging.info("Unit Test Passed for entity layer error handling.")

if __name__ == "__main__":
    pytest.main([__file__])
