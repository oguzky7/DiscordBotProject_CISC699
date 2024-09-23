# File: test_!fetch_all_accounts.py
# Purpose: Unit tests for the !fetch_all_accounts command.
from unittest.mock import patch
import logging, unittest
from test_init import BaseTestSetup, CustomTextTestRunner

class TestFetchAllAccountsCommand(BaseTestSetup):
    @patch('DataObjects.AccountDAO.AccountDAO.fetch_all_accounts')
    async def test_fetch_all_accounts_success(self, mock_fetch_all_accounts):
        """Test the fetch_all_accounts command when it succeeds."""
        logging.info("Starting test: test_fetch_all_accounts_success")

        mock_fetch_all_accounts.return_value = [("1", "testuser", "password", "example.com")]
        
        command = self.bot.get_command("fetch_all_accounts")
        self.assertIsNotNone(command)
        await command(self.ctx)
        
        # Correct the expected message
        expected_message = "Accounts:\nID: 1, Username: testuser, Password: password, Website: example.com"
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful fetch.")


    @patch('DataObjects.AccountDAO.AccountDAO.fetch_all_accounts')  # Correct path
    async def test_fetch_all_accounts_error(self, mock_fetch_all_accounts):
        """Test the fetch_all_accounts command when it encounters an error."""
        logging.info("Starting test: test_fetch_all_accounts_error")

        # Simulate an error
        mock_fetch_all_accounts.side_effect = Exception("Database error")
        
        command = self.bot.get_command("fetch_all_accounts")
        await command(self.ctx)
        
        # Verify that the correct error message is sent
        self.ctx.send.assert_called_with("Error fetching accounts.")
        logging.info("Verified error handling.")


if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
