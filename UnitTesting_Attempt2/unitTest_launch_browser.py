from test_init import BaseTestCase, patch, logging, unittest

class TestBrowserFunctionality(BaseTestCase):
    
    @patch('entity.BrowserEntity.BrowserEntity.launch_browser')
    def test_launch_browser_success(self, mock_launch):
        """Test successful browser launch."""
        print("\nTest Started for: test_launch_browser_success")
        mock_launch.return_value = "Browser launched."
        expected_entity_result = "Browser launched."
        expected_control_result = "Control Object Result: Browser launched."
        result = self.control.receive_command("launch_browser")
        
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_launch.return_value}")
        self.assertEqual(mock_launch.return_value, expected_entity_result, "Entity layer assertion failed.")
        logging.info("Unit Test Passed for entity layer.\n")
        
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_control_result, "Control layer assertion failed.")
        logging.info("Unit Test Passed for control layer.\n")

    @patch('entity.BrowserEntity.BrowserEntity.launch_browser')
    def test_launch_browser_already_running(self, mock_launch):
        """Test launch browser when already running."""
        print("\nTest Started for: test_launch_browser_already_running")
        mock_launch.return_value = "Browser is already running."
        expected_entity_result = "Browser is already running."
        expected_control_result = "Control Object Result: Browser is already running."
        result = self.control.receive_command("launch_browser")
        
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_launch.return_value}")
        self.assertEqual(mock_launch.return_value, expected_entity_result, "Entity layer assertion failed.")
        logging.info("Unit Test Passed for entity layer.\n")
        
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_control_result, "Control layer assertion failed.")
        logging.info("Unit Test Passed for control layer.\n")

    @patch('entity.BrowserEntity.BrowserEntity.launch_browser')
    def test_launch_browser_failure_control(self, mock_launch):
        """Test control layer's handling of the entity layer failure."""
        print("\nTest Started for: test_launch_browser_failure_control")
        mock_launch.side_effect = Exception("Internal error")
        expected_result = "Control Layer Exception: Internal error"
        result = self.control.receive_command("launch_browser")
        
        logging.info(f"Control Layer Expected to Report: {expected_result}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_result, "Control layer failed to handle or report the entity error correctly.")
        logging.info("Unit Test Passed for control layer error handling.\n")

    @patch('entity.BrowserEntity.BrowserEntity.launch_browser')
    def test_launch_browser_failure_entity(self, mock_launch):
        """Test failure to launch browser due to an internal error in the entity layer."""
        print("\nTest Started for: test_launch_browser_failure_entity")
        internal_error_message = "Failed to launch browser: Internal error"
        mock_launch.side_effect = Exception(internal_error_message)  # Simulate an exception on error
        expected_control_result = f"Control Layer Exception: {internal_error_message}"

        # Execute command
        result = self.control.receive_command("launch_browser")

        # Check if the control layer returns the correct error message
        logging.info(f"Entity Layer Expected Failure: {internal_error_message}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_control_result, "Control layer failed to report entity error correctly.")
        logging.info("Unit Test Passed for entity layer error handling.\n")


if __name__ == '__main__':
    unittest.main()
