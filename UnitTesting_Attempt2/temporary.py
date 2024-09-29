from test_init import BaseTestCase, patch, logging, unittest

class TestAddAccountFunctionality(BaseTestCase):

    @patch('DataObjects.AccountDAO.AccountDAO.add_account')
    def test_add_account_success(self, mock_add_account):
        """Test adding an account successfully."""
        print("\nTest Started for: test_add_account_success")
        mock_add_account.return_value = True
        expected_result = "Account for website added successfully."
        result = self.account_control.receive_command("add_account", "user", "pass", "website")
        
        logging.info(f"Expected: {expected_result}")
        logging.info(f"Received: {result}")
        self.assertEqual(result, expected_result, "Account should be added successfully.")
        logging.info("Unit Test Passed for successful account addition.\n")


if __name__ == '__main__':
    unittest.main()
