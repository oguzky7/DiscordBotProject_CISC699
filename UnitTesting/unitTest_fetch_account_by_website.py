import pytest
import logging
from unittest.mock import patch
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()

async def test_fetch_account_by_website_success(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.fetch_account_by_website') as mock_fetch:
        # Setup mock return and expected outcomes
        website = "example.com"
        mock_fetch.return_value = ("sample_username", "sample_password")
        expected_entity_result = ("sample_username", "sample_password")
        expected_control_result = ("sample_username", "sample_password")

        # Execute the command
        result = base_test_case.account_control.fetch_account_by_website(website)

        # Log and assert the outcomes
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_fetch.return_value}")
        assert mock_fetch.return_value == expected_entity_result, "Entity layer assertion failed."
        logging.info("Unit Test Passed for entity layer.\n")

        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer.")


async def test_fetch_account_by_website_no_account(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.fetch_account_by_website') as mock_fetch:
        # Setup mock return and expected outcomes
        website = "nonexistent.com"
        mock_fetch.return_value = None
        expected_control_result = "No account found for nonexistent.com."

        # Execute the command
        result = base_test_case.account_control.fetch_account_by_website(website)

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer no account found.\n")


async def test_fetch_account_by_website_failure_entity(base_test_case):
    with patch('DataObjects.AccountDAO.AccountDAO.fetch_account_by_website', side_effect=Exception("Database Error")) as mock_fetch:
        # Setup expected outcomes
        website = "example.com"
        expected_control_result = "Error: Database Error"

        # Execute the command
        result = base_test_case.account_control.fetch_account_by_website(website)

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer failed to handle entity error correctly."
        logging.info("Unit Test Passed for entity layer error handling.")


async def test_fetch_account_by_website_failure_control(base_test_case):
    with patch('control.AccountControl.AccountControl.fetch_account_by_website', side_effect=Exception("Control Layer Error")) as mock_control:
        # Setup expected outcomes
        website = "example.com"
        expected_control_result = "Control Layer Exception: Control Layer Error"

        # Execute the command and catch the raised exception
        try:
            result = base_test_case.account_control.fetch_account_by_website(website)
        except Exception as e:
            result = f"Control Layer Exception: {str(e)}"

        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer failed to handle its own error correctly."
        logging.info("Unit Test Passed for control layer error handling.")


if __name__ == "__main__":
    pytest.main([__file__])
