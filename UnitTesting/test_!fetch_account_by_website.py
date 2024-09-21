import unittest, logging
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

class TestFetchAccountByWebsiteCommand(BaseTestSetup):
    
    @patch('DataObjects.AccountDAO.AccountDAO.fetch_account_by_website')
    async def test_fetch_account_by_website_success(self, mock_fetch_account_by_website):
        """Test the fetch_account_by_website command when it succeeds."""
        logging.info("Starting test: test_fetch_account_by_website_success")
        mock_fetch_account_by_website.return_value = ('testuser', 'password123')

        command = self.bot.get_command("fetch_account_by_website")
        self.assertIsNotNone(command)

        await command(self.ctx, 'example.com')
        
        expected_message = 'Account found for example.com: Username: testuser, Password: password123'
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful account fetch.")

    @patch('DataObjects.AccountDAO.AccountDAO.fetch_account_by_website')
    async def test_fetch_account_by_website_error(self, mock_fetch_account_by_website):
        """Test the fetch_account_by_website command when it encounters an error."""
        logging.info("Starting test: test_fetch_account_by_website_error")
        mock_fetch_account_by_website.return_value = None

        command = self.bot.get_command("fetch_account_by_website")
        self.assertIsNotNone(command)

        await command(self.ctx, 'nonexistent.com')
        
        expected_message = 'No account found for nonexistent.com.'
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling for nonexistent account.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
