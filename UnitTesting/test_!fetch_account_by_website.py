import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!fetch_all_accounts.py
Purpose: Unit tests for the !fetch_all_accounts command in the Discord bot.
The tests validate both successful and error scenarios, ensuring accounts are fetched successfully or errors are handled properly.
"""

class TestFetchAllAccountsCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.fetch_all_accounts')
    async def test_fetch_all_accounts_success(self, mock_fetch_all_accounts, mock_parse_user_message):
        """Test the fetch_all_accounts command when it succeeds."""
        logging.info("Starting test: test_fetch_all_accounts_success")

        mock_fetch_all_accounts.return_value = [("1", "testuser", "password", "example.com")]
        mock_parse_user_message.return_value = ["fetch_all_accounts"]

        command = self.bot.get_command("fetch_all_accounts")
        self.assertIsNotNone(command)
        await command(self.ctx)
        
        expected_message = "Accounts:\nID: 1, Username: testuser, Password: password, Website: example.com"
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful fetch.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.fetch_all_accounts')
    async def test_fetch_all_accounts_error(self, mock_fetch_all_accounts, mock_parse_user_message):
        """Test the fetch_all_accounts command when it encounters an error."""
        logging.info("Starting test: test_fetch_all_accounts_error")

        mock_fetch_all_accounts.side_effect = Exception("Database error")
        mock_parse_user_message.return_value = ["fetch_all_accounts"]

        command = self.bot.get_command("fetch_all_accounts")
        self.assertIsNotNone(command)
        await command(self.ctx)
        
        self.ctx.send.assert_called_with("Error fetching accounts.")
        logging.info("Verified error handling.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
