from unittest.mock import patch
import logging, unittest
from test_init import BaseTestSetup, CustomTextTestRunner

class TestDeleteAccountCommand(BaseTestSetup):
    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.delete_account')
    async def test_delete_account_success(self, mock_delete_account, mock_parse_user_message):
        """Test the delete_account command when it succeeds."""
        logging.info("Unit test for delete account starting for positive test:")
        logging.info("Starting test: test_delete_account_success")

        # Mock setup to simulate user input parsing and successful account deletion
        mock_delete_account.return_value = True
        mock_parse_user_message.return_value = ["delete_account", "123"]

        # Triggering the delete account command in the bot
        command = self.bot.get_command("delete_account")
        await command(self.ctx)

        # Checking if the success message was correctly sent to the user
        expected_message = "Account with ID 123 deleted successfully."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified successful account deletion.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.delete_account')
    async def test_delete_account_error(self, mock_delete_account, mock_parse_user_message):
        """Test the delete_account command when it encounters an error."""
        logging.info("Unit test for delete account starting for negative test:")
        logging.info("Starting test: test_delete_account_error")

        # Mock setup for testing account deletion failure
        mock_delete_account.return_value = False
        mock_parse_user_message.return_value = ["delete_account", "999"]

        # Executing the delete account command with expected failure
        command = self.bot.get_command("delete_account")
        await command(self.ctx)

        # Checking if the error message was correctly relayed to the user
        expected_message = "Failed to delete account with ID 999."
        self.ctx.send.assert_called_with(expected_message)
        logging.info("Verified error handling during account deletion.")

if __name__ == "__main__":
    # Custom test runner to highlight the test results
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
