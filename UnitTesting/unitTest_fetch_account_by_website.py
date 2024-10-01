import pytest, os, sys
from unittest.mock import MagicMock
from test_init import setup_logging, base_test_case, save_test_results_to_file, log_test_start_end, logging


setup_logging()  # Initialize logging if needed

@pytest.mark.usefixtures("base_test_case")
class TestAccountDAOFetchByWebsite:
    @pytest.fixture
    def account_dao(self, base_test_case, mocker):
        # Mock the psycopg2 connection and cursor
        mocker.patch('psycopg2.connect')
        account_dao = base_test_case.account_dao
        account_dao.connection = MagicMock()
        account_dao.cursor = MagicMock()
        logging.info("Fake database connection established")
        return account_dao

    def test_entity_fetch_account_success(self, account_dao):
        # Setup the cursor's behavior for successful fetch
        account_dao.cursor.execute = MagicMock()
        account_dao.cursor.fetchone.return_value = ("test_user", "password123")
        
        # Test the fetch_account_by_website method for success
        result = account_dao.fetch_account_by_website("example.com")
    
        # Log the result of the operation
        logging.info(f"AccountDAO.fetch_account_by_website returned {result}")
        logging.info("Expected result: ('test_user', 'password123')")
        
        # Assert and log the final outcome
        assert result == ("test_user", "password123"), "Account should be fetched successfully"
        logging.info("Test fetch_account_success passed")

    def test_entity_fetch_account_fail(self, account_dao):
        # Setup the cursor's behavior to simulate failure
        account_dao.cursor.execute = MagicMock()
        account_dao.cursor.fetchone.return_value = None

        # Perform the test
        result = account_dao.fetch_account_by_website("fail.com")
        
        # Log the result of the operation
        logging.info(f"AccountDAO.fetch_account_by_website returned {result}")
        logging.info("Expected result: None")
        
        # Assert and log the final outcome
        assert result is None, "No account should be fetched"
        logging.info("Test fetch_account_fail passed")



@pytest.mark.usefixtures("base_test_case")
class TestAccountControlFetchByWebsite:
    @pytest.fixture
    def account_control(self, base_test_case, mocker):
        # Get the mocked AccountControl from base_test_case
        account_control = base_test_case.account_control
        account_control.account_dao = MagicMock(spec=base_test_case.account_dao)
        
        # Mock methods used in the control layer's fetch_account_by_website
        mocker.patch.object(account_control.account_dao, 'connect')
        mocker.patch.object(account_control.account_dao, 'close')
        logging.info("Mocked AccountDAO connection and close methods")
        return account_control

    def test_control_fetch_account_success(self, account_control):
        # Mock successful fetch in the DAO layer
        account_control.account_dao.fetch_account_by_website.return_value = ("test_user", "password123")
        
        # Call the control method and check the response
        result = account_control.fetch_account_by_website("example.com")
        expected_message = ("test_user", "password123")
        
        # Log the response and expectations
        logging.info(f"Control method fetch_account_by_website returned: '{result}'")
        logging.info("Expected message: ('test_user', 'password123')")
        
        # Assert the success message
        assert result == expected_message, "The fetch result should match expected output"
        logging.info("Test control_fetch_account_success passed")

    def test_control_fetch_account_fail(self, account_control):
        # Mock failure in the DAO layer
        account_control.account_dao.fetch_account_by_website.return_value = None
        
        # Call the control method and check the response
        result = account_control.fetch_account_by_website("fail.com")
        expected_message = "No account found for fail.com."
        
        # Log the response and expectations
        logging.info(f"Control method fetch_account_by_website returned: '{result}'")
        logging.info("Expected message: 'No account found for fail.com.'")
        
        # Assert the failure message
        assert result == expected_message, "The failure message should match expected output"
        logging.info("Test control_fetch_account_fail passed")




if __name__ == "__main__":
    pytest.main([__file__])  # Run pytest directly
