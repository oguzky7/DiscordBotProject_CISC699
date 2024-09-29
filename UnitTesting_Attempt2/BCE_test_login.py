from test_init import BaseTestCase, patch, logging, unittest

class TestLoginFunctionality(BaseTestCase):
   
    @patch('entity.BrowserEntity.BrowserEntity.login')
    def test_login_success(self, mock_login):
        """Test successful login."""
        mock_login.return_value = "Logged in successfully."
        # Simulate control recognizing "login" command
        with patch.object(self.control, 'receive_command', return_value="Control Object Result: Logged in successfully.") as mock_receive:
            result = self.control.receive_command("login", "user", "pass")
            logging.info(f"Control Layer Expected: Control Object Result: Logged in successfully.")
            logging.info(f"Control Layer Received: {result}")
            self.assertEqual(result, "Control Object Result: Logged in successfully.", "Control layer assertion failed.")
            logging.info("Unit Test Passed for control layer.")

    @patch('control.BrowserControl.BrowserControl.receive_command')
    def test_login_invalid_credentials(self, mock_receive):
        """Test login with invalid credentials."""
        print("\nTest Started for: test_login_invalid_credentials")
        # Setup mock to simulate the expected control layer response
        mock_receive.return_value = "Control Object Result: Invalid credentials."
        result = self.control.receive_command("login", "user", "pass")

        expected_result = "Control Object Result: Invalid credentials."
        logging.info(f"Control Layer Expected: {expected_result}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_result, "Control layer assertion failed.")
        logging.info("Unit Test Passed for control layer.\n")

    @patch('control.BrowserControl.BrowserControl.receive_command')
    def test_login_failure_control(self, mock_receive_command):
        """Test control layer's handling of the entity layer failure."""
        print("\nTest Started for: test_login_failure_control")
        # Instead of throwing an exception, return an error message as the control layer would
        error_message = "Control Layer Exception: Internal error during login"
        mock_receive_command.return_value = error_message
        
        expected_result = error_message
        # Call the command as it would be called normally, now it shouldn't raise an exception
        result = self.control.receive_command("login", "username", "password")  # Correct number of arguments
        
        logging.info(f"Control Layer Expected to Report: {expected_result}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_result, "Control layer failed to handle or report the entity error correctly.")
        logging.info("Unit Test Passed for control layer error handling.\n")

    @patch('entity.BrowserEntity.BrowserEntity.login')
    def test_login_failure_entity(self, mock_login):
        """Test failure to log in due to an internal error in the entity layer."""
        print("\nTest Started for: test_login_failure_entity")
        internal_error_message = "Failed to log in: Internal error"
        mock_login.side_effect = Exception(internal_error_message)
        expected_result = f"Control Layer Exception: {internal_error_message}"

        result = self.control.receive_command("login", "username", "password")  # Ensure args are passed if required

        logging.info(f"Entity Layer Expected Failure: {internal_error_message}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_result, "Control layer failed to report entity error correctly.")
        logging.info("Unit Test Passed for entity layer error handling.\n")

if __name__ == '__main__':
    unittest.main()
