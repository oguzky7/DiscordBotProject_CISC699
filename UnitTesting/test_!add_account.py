from unittest.mock import patch
import logging, unittest
from test_init import BaseTestSetup, CustomTextTestRunner

class TestAddAccountCommand(BaseTestSetup):

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.add_account')
    async def test_add_account_success(self, mock_add_account, mock_parse_user_message):
        """Test the add_account command when it succeeds."""
        # Simulate parsing user message and extracting command parameters
        mock_parse_user_message.return_value = ["add_account", "testuser", "password123", "example.com"]
        # Simulate successful account addition in the database
        mock_add_account.return_value = True

        # Triggering the command within the bot
        command = self.bot.get_command("add_account")
        await command(self.ctx)
        
        # Validate that the success message is correctly sent to the user
        self.ctx.send.assert_called_with("Account for example.com added successfully.")
        logging.info("Verified successful account addition - database addition simulated and feedback provided.")

    @patch('DataObjects.global_vars.GlobalState.parse_user_message')
    @patch('DataObjects.AccountDAO.AccountDAO.add_account')
    async def test_add_account_error(self, mock_add_account, mock_parse_user_message):
        """Test the add_account command when it encounters an error."""
        # Setup for receiving command and failing to add account
        mock_parse_user_message.return_value = ["add_account", "testuser", "password123", "example.com"]
        mock_add_account.return_value = False

        # Command execution with expected failure
        command = self.bot.get_command("add_account")
        await command(self.ctx)
        
        # Ensuring error feedback is correctly relayed to the user
        self.ctx.send.assert_called_with("Failed to add account for example.com.")
        logging.info("Verified error handling during account addition - simulated database failure and error feedback.")

if __name__ == "__main__":
    unittest.main(testRunner=CustomTextTestRunner(verbosity=2))
