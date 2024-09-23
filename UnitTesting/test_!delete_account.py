import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!delete_account.py
Purpose: This file contains unit tests for the !delete_account command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the bot deletes the account properly or handles errors.
Tests:
- Positive: Simulates the !delete_account command and verifies the account is deleted successfully.
- Negative: Simulates an error during account deletion and ensures it is handled gracefully.
"""

class TestDeleteAccountCommand(BaseTestSetup):
    
    @patch('DataObjects.AccountDAO.AccountDAO.delete_account')
    async def test_delete_account_success(self, mock_delete_account):
        """Test the delete_account command when it succeeds."""
        logging.info("Starting test: test_delete_account_success")
        mock_delete_account.return_value = True  # Simulate successful deletion

        command = self.bot.get_command("delete_account")
        self.assertIsNotNone(command)

        await command(self.ctx, '123')  # Simulate passing account ID '123'

        expected_message = "Account with ID 123 deleted successfully."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful account deletion.")

    @patch('DataObjects.AccountDAO.AccountDAO.delete_account')
    async def test_delete_account_error(self, mock_delete_account):
        """Test the delete_account command when it encounters an error."""
        logging.info("Starting test: test_delete_account_error")
        mock_delete_account.return_value = False  # Simulate failure in deletion

        command = self.bot.get_command("delete_account")
        self.assertIsNotNone(command)

        await command(self.ctx, '999')  # Simulate passing a non-existent account ID '999'

        expected_message = "Failed to delete account with ID 999."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling during account deletion.")

if __name__ == "__main__":
    # Use the custom test runner to display 'Unit test passed'
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
