from test_init import BaseTestCase, patch, AsyncMock, logging, unittest

class TestLoginFunctionality(BaseTestCase):
    
    @patch('entity.BrowserEntity.BrowserEntity.login')
    async def test_login_success(self, mock_login):
        """Test successful login."""
        print("\nTest Started for: test_login_success")
        mock_login.return_value = "Logged in successfully."
        expected_result = "Control Object Result: Logged in successfully."
        result = await self.browser_control.receive_command("login", site="example.com")
        
        logging.info(f"Expected Result: {expected_result}")
        logging.info(f"Received Result: {result}")
        self.assertEqual(result, expected_result, "Login success test failed.")
        logging.info("Unit Test Passed for login success.\n")

    @patch('entity.BrowserEntity.BrowserEntity.login')
    async def test_login_failure(self, mock_login):
        """Test login failure due to incorrect credentials."""
        print("\nTest Started for: test_login_failure")
        mock_login.return_value = "Login failed: Incorrect credentials."
        expected_result = "Control Object Result: Login failed: Incorrect credentials."
        result = await self.browser_control.receive_command("login", site="example.com")
        
        logging.info(f"Expected Result: {expected_result}")
        logging.info(f"Received Result: {result}")
        self.assertEqual(result, expected_result, "Login failure test failed.")
        logging.info("Unit Test Passed for login failure.\n")

    @patch('entity.BrowserEntity.BrowserEntity.login')
    def test_login_without_browser_open(self, mock_login):
        """Test login attempt when browser is not initially open."""
        print("\nTest Started for: test_login_without_browser_open")
        mock_login.return_value = "Browser launched and logged in successfully."
        expected_result = "Control Object Result: Browser launched and logged in successfully."
        result = self.browser_control.receive_command("login", site="example.com")
        
        logging.info(f"Expected Result: {expected_result}")
        logging.info(f"Received Result: {result}")
        self.assertEqual(result, expected_result, "Test failed when browser was not open.")
        logging.info("Unit Test Passed when browser was not initially open.\n")

    @patch('entity.BrowserEntity.BrowserEntity.login')
    def test_login_with_invalid_site(self, mock_login):
        """Test login failure when the site URL is not available."""
        print("\nTest Started for: test_login_with_invalid_site")
        mock_login.return_value = "URL for site not found."
        expected_result = "Control Object Result: URL for site not found."
        result = self.browser_control.receive_command("login", site="unknownsite.com")
        
        logging.info(f"Expected Result: {expected_result}")
        logging.info(f"Received Result: {result}")
        self.assertEqual(result, expected_result, "Test failed due to unavailable URL.")
        logging.info("Unit Test Passed for invalid site URL.\n")

if __name__ == '__main__':
    unittest.main()
