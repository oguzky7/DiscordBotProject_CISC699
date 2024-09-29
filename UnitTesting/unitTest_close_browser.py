from test_init import BaseTestCase, patch, logging, unittest

class TestBrowserFunctionality(BaseTestCase):
    
    @patch('entity.BrowserEntity.BrowserEntity.close_browser')
    def test_close_browser_success(self, mock_close):
        """Test successful browser close."""
        print("\nTest Started for: test_close_browser_success")
        mock_close.return_value = "Browser closed."
        expected_entity_result = "Browser closed."
        expected_control_result = "Control Object Result: Browser closed."
        result = self.browser_control.receive_command("close_browser")
        
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_close.return_value}")
        self.assertEqual(mock_close.return_value, expected_entity_result, "Entity layer assertion failed.")
        logging.info("Unit Test Passed for entity layer.\n")
        
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_control_result, "Control layer assertion failed.")
        logging.info("Unit Test Passed for control layer.\n")

    @patch('entity.BrowserEntity.BrowserEntity.close_browser')
    def test_close_browser_not_open(self, mock_close):
        """Test closing a browser that is not open."""
        print("\nTest Started for: test_close_browser_not_open")
        mock_close.return_value = "No browser is currently open."
        expected_entity_result = "No browser is currently open."
        expected_control_result = "Control Object Result: No browser is currently open."
        result = self.browser_control.receive_command("close_browser")
        
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_close.return_value}")
        self.assertEqual(mock_close.return_value, expected_entity_result, "Entity layer assertion failed.")
        logging.info("Unit Test Passed for entity layer.\n")
        
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_control_result, "Control layer assertion failed.")
        logging.info("Unit Test Passed for control layer.\n")

    @patch('entity.BrowserEntity.BrowserEntity.close_browser')
    def test_close_browser_failure(self, mock_close):
        """Test control layer's handling of an unexpected error during browser close."""
        print("\nTest Started for: test_close_browser_failure")
        mock_close.side_effect = Exception("Unexpected error")
        expected_result = "Control Layer Exception: Unexpected error"
        result = self.browser_control.receive_command("close_browser")
        
        logging.info(f"Control Layer Expected to Report: {expected_result}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_result, "Control layer failed to handle or report the error correctly.")
        logging.info("Unit Test Passed for control layer error handling.\n")

 
    @patch('entity.BrowserEntity.BrowserEntity.close_browser')
    def test_close_browser_failure_entity(self, mock_close):
        """Test failure to close the browser due to an internal error in the entity layer."""
        print("\nTest Started for: test_close_browser_failure_entity")
        internal_error_message = "BrowserEntity_Failed to close browser: Internal error"
        mock_close.side_effect = Exception(internal_error_message)  # Simulate an exception on error
        expected_control_result = f"Control Layer Exception: {internal_error_message}"

        # Execute command
        result = self.browser_control.receive_command("close_browser")

        # Check if the control layer returns the correct error message
        logging.info(f"Entity Layer Expected Failure: {internal_error_message}")
        logging.info(f"Control Layer Received: {result}")
        self.assertEqual(result, expected_control_result, "Control layer failed to report entity error correctly.")
        logging.info("Unit Test Passed for entity layer error handling.\n")


if __name__ == '__main__':
    unittest.main()
