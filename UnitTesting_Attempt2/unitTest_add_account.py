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

    @patch('DataObjects.AccountDAO.AccountDAO.add_account')
    def test_add_account_validation_failure(self, mock_add_account):
        """Test adding an account with validation failure."""
        print("\nTest Started for: test_add_account_validation_failure")
        mock_add_account.return_value = False
        expected_result = "Failed to add account for website."
        result = self.account_control.receive_command("add_account", "user", "pass", "")
        
        logging.info(f"Expected: {expected_result}")
        logging.info(f"Received: {result}")
        self.assertEqual(result, expected_result, "Validation should fail with inadequate data.")
        logging.info("Unit Test Passed for account validation failure.\n")

    @patch('DataObjects.AccountDAO.AccountDAO.add_account')
    def test_add_account_control_layer_failure(self, mock_add_account):
        """Test control layer's handling of account addition failure."""
        print("\nTest Started for: test_add_account_control_layer_failure")
        mock_add_account.side_effect = Exception("Database error")
        expected_result = "Error inserting account: Database error"
        result = self.account_control.receive_command("add_account", "user", "pass", "website")
        
        logging.info(f"Expected: {expected_result}")
        logging.info(f"Received: {result}")
        self.assertEqual(result, expected_result, "Control layer should handle database errors gracefully.")
        logging.info("Unit Test Passed for control layer error handling in account addition.\n")

    @patch('DataObjects.AccountDAO.AccountDAO.add_account')
    def test_add_account_entity_layer_failure(self, mock_add_account):
        """Test entity layer failure during account addition."""
        print("\nTest Started for: test_add_account_entity_layer_failure")
        internal_error_message = "Failed to add account: Permission denied"
        mock_add_account.side_effect = Exception(internal_error_message)
        expected_result = f"Error: {internal_error_message}"
        result = self.account_control.receive_command("add_account", "user", "pass", "website")
        
        logging.info(f"Expected: {expected_result}")
        logging.info(f"Received: {result}")
        self.assertEqual(result, expected_result, "Entity layer should report permission issues correctly.")
        logging.info("Unit Test Passed for entity layer error handling in account addition.\n")

if __name__ == '__main__':
    unittest.main()
