# File: test_!add_account.py
# Purpose: Unit tests for the !add_account command.

from unittest.mock import patch
import logging, unittest
from test_init import BaseTestSetup, CustomTextTestRunner  # Import the shared setup

"""
File: test_!add_account.py
Purpose: This file contains unit tests for the !add_account command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the account is added successfully or errors are handled properly.
Tests:
- Positive: Simulates the !add_account command and verifies the account is added correctly.
- Negative: Simulates an error while adding the account.
"""

class TestAddAccountCommand(BaseTestSetup):

    @patch('DataObjects.AccountDAO.AccountDAO.add_account')
    async def test_add_account_success(self, mock_add_account):
        """Test the add_account command when it succeeds."""
        logging.info("Starting test: test_add_account_success")

        # Mock the DAO method to simulate successful account addition
        mock_add_account.return_value = True
        
        command = self.bot.get_command("add_account")
        self.assertIsNotNone(command)
        await command(self.ctx, "testuser", "password123", "example.com")
        
        expected_message = "Account for example.com added successfully."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful account addition.")

    @patch('DataObjects.AccountDAO.AccountDAO.add_account')
    async def test_add_account_error(self, mock_add_account):
        """Test the add_account command when it encounters an error."""
        logging.info("Starting test: test_add_account_error")

        # Mock the DAO method to simulate an error during account addition
        mock_add_account.return_value = False
        
        command = self.bot.get_command("add_account")
        await command(self.ctx, "testuser", "password123", "example.com")
        
        self.ctx.send.assert_called_with("Failed to add account for example.com.")
        logging.info("Verified error handling during account addition.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
