import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!fetch_account_by_website.py
Purpose: Unit tests for the !fetch_account_by_website command in the Discord bot.
"""

class TestFetchAccountByWebsiteCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.fetch_account_by_website')
    async def test_fetch_account_by_website_success(self, mock_fetch_account_by_website, mock_parse_user_message):
        """Test the fetch_account_by_website command when it succeeds."""
        logging.info("Starting test: test_fetch_account_by_website_success")

        mock_fetch_account_by_website.return_value = ("testuser", "password123")
        mock_parse_user_message.return_value = ["fetch_account_by_website", "example.com"]

        command = self.bot.get_command("fetch_account_by_website")
        self.assertIsNotNone(command)

        await command(self.ctx)
        expected_message = "testuser", "password123"
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful account fetch.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.fetch_account_by_website')
    async def test_fetch_account_by_website_error(self, mock_fetch_account_by_website, mock_parse_user_message):
        """Test the fetch_account_by_website command when it encounters an error."""
        logging.info("Starting test: test_fetch_account_by_website_error")

        mock_fetch_account_by_website.return_value = None
        mock_parse_user_message.return_value = ["fetch_account_by_website", "nonexistent.com"]

        command = self.bot.get_command("fetch_account_by_website")
        self.assertIsNotNone(command)

        await command(self.ctx)
        expected_message = "No account found for nonexistent.com."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling for nonexistent account.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
