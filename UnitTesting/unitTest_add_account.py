import pytest, os, sys
from unittest.mock import MagicMock
from test_init import setup_logging, base_test_case, save_test_results_to_file, log_test_start_end, logging


setup_logging()  # Initialize logging if needed

@pytest.mark.usefixtures("base_test_case")
class TestAccountDAO:
    @pytest.fixture
    def account_dao(self,base_test_case, mocker):
        # Mock the psycopg2 connection and cursor
        mocker.patch('psycopg2.connect')
        account_dao = base_test_case.account_dao
        account_dao.connection = MagicMock()
        account_dao.cursor = MagicMock()
        logging.info("Fake database connection established")
        return account_dao

    def test_add_account_success(self, account_dao):
        # Setup the cursor's behavior for successful insertion
        account_dao.cursor.execute = MagicMock()
        account_dao.cursor.rowcount = 1
        account_dao.connection.commit = MagicMock()
        
        # Test the add_account method for success
        result = account_dao.add_account("test_user", "password123", "example.com")
    
        # Log the result of the operation
        logging.info(f"AccountDAO.add_account returned {result}")
        logging.info("Expected result: True")

         # Assert and log the final outcome
        assert result == True, "Account should be added successfully"
        logging.info("Test add_account_success passed")

    def test_add_account_fail(self, account_dao):
        # Setup the cursor's behavior to simulate a failure during insertion
        account_dao.cursor.execute.side_effect = Exception("Database error")
        account_dao.cursor.rowcount = 0
        account_dao.connection.commit = MagicMock()

         # Perform the test
        result = account_dao.add_account("fail_user", "fail123", "fail.com")
        
        # Log the result of the operation
        logging.info(f"AccountDAO.add_account returned {result}")
        logging.info("Expected result: False")
        
        # Assert and log the final outcome
        assert result == False, "Account should not be added"
        logging.info("Test add_account_fail passed")


if __name__ == "__main__":
    pytest.main([__file__])  # Run pytest directly
