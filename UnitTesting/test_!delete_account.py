import logging, unittest
from unittest.mock import patch
from test_init import BaseTestSetup, CustomTextTestRunner

"""
File: test_!delete_account.py
Purpose: Unit tests for the !delete_account command in the Discord bot.
The tests validate both successful and error scenarios, ensuring the bot deletes the account properly or handles errors gracefully.
"""

class TestDeleteAccountCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.delete_account')
    async def test_delete_account_success(self, mock_delete_account, mock_parse_user_message):
        """Test the delete_account command when it succeeds."""
        logging.info("Starting test: test_delete_account_success")

        mock_delete_account.return_value = True
        mock_parse_user_message.return_value = ["delete_account", "123"]

        command = self.bot.get_command("delete_account")
        self.assertIsNotNone(command)
        await command(self.ctx)

        expected_message = "Account with ID 123 deleted successfully."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful account deletion.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.delete_account')
    async def test_delete_account_error(self, mock_delete_account, mock_parse_user_message):
        """Test the delete_account command when it encounters an error."""
        logging.info("Starting test: test_delete_account_error")

        mock_delete_account.return_value = False
        mock_parse_user_message.return_value = ["delete_account", "999"]

        command = self.bot.get_command("delete_account")
        self.assertIsNotNone(command)
        await command(self.ctx)

        expected_message = "Failed to delete account with ID 999."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling during account deletion.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
