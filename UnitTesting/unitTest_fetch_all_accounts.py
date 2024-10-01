import pytest, os, sys
from unittest.mock import MagicMock
from test_init import setup_logging, base_test_case, save_test_results_to_file, log_test_start_end, logging


setup_logging()  # Initialize logging if needed

@pytest.mark.usefixtures("base_test_case")
class TestAccountDAO:
    @pytest.fixture
    def account_dao(self, base_test_case, mocker):
        mocker.patch('psycopg2.connect')
        account_dao = base_test_case.account_dao
        account_dao.connection = MagicMock()
        account_dao.cursor = MagicMock()
        logging.info("Fake database connection established")
        return account_dao

    def test_entity_fetch_all_accounts_success(self, account_dao):
        # Mock successful fetch operation
        mock_accounts = [(1, "test_user", "password123", "example.com"), (2, "test_user2", "password456", "example2.com")]
        account_dao.cursor.fetchall.return_value = mock_accounts
        
        # Test fetch_all_accounts method
        result = account_dao.fetch_all_accounts()
        
        logging.info(f"AccountDAO.fetch_all_accounts returned {result}")
        logging.info("Expected result: a list of accounts")
        
        # Assert and log the final outcome
        assert result == mock_accounts, "Should return a list of accounts"
        logging.info("Test fetch_all_accounts_success passed")

    def test_entity_fetch_all_accounts_fail(self, account_dao):
        # Mock failed fetch operation
        account_dao.cursor.fetchall.side_effect = Exception("Database error")
        
        # Test fetch_all_accounts method
        result = account_dao.fetch_all_accounts()
        
        logging.info(f"AccountDAO.fetch_all_accounts returned {result}")
        logging.info("Expected result: an empty list due to failure")
        
        # Assert and log the final outcome
        assert result == [], "Should return an empty list due to failure"
        logging.info("Test fetch_all_accounts_fail passed")


@pytest.mark.usefixtures("base_test_case")
class TestAccountControl:
    @pytest.fixture
    def account_control(self, base_test_case, mocker):
        account_control = base_test_case.account_control
        account_control.account_dao = MagicMock(spec=base_test_case.account_dao)
        
        # Mock methods used in the control layer's fetch_all_accounts
        mocker.patch.object(account_control.account_dao, 'connect')
        mocker.patch.object(account_control.account_dao, 'close')
        logging.info("Mocked AccountDAO connection and close methods")
        return account_control

    def test_control_fetch_all_accounts_success(self, account_control):
        # Mock successful fetch in the DAO layer
        mock_accounts = [(1, "test_user", "password123", "example.com"), (2, "test_user2", "password456", "example2.com")]
        account_control.account_dao.fetch_all_accounts.return_value = mock_accounts
        
        # Call the control method and check the response
        result = account_control.fetch_all_accounts()
        
        expected_message = "Accounts:\nID: 1, Username: test_user, Password: password123, Website: example.com\nID: 2, Username: test_user2, Password: password456, Website: example2.com"
        
        logging.info(f"Control method fetch_all_accounts returned: '{result}'")
        logging.info(f"Expected message: '{expected_message}'")
        
        # Assert and log the final outcome
        assert result == expected_message, "The fetched accounts list should match expected output"
        logging.info("Test control_fetch_all_accounts_success passed")

    def test_control_fetch_all_accounts_fail(self, account_control):
        # Mock failed fetch in the DAO layer
        account_control.account_dao.fetch_all_accounts.return_value = []
        
        # Call the control method and check the response
        result = account_control.fetch_all_accounts()
        
        expected_message = "No accounts found."
        
        logging.info(f"Control method fetch_all_accounts returned: '{result}'")
        logging.info(f"Expected message: '{expected_message}'")
        
        # Assert and log the final outcome
        assert result == expected_message, "The message should indicate no accounts found"
        logging.info("Test control_fetch_all_accounts_fail passed")


if __name__ == "__main__":
    pytest.main([__file__])  # Run pytest directly
