import unittest
from unittest.mock import patch
from test_init import BaseTestCase  # Ensure BaseTestCase correctly inherits from IsolatedAsyncioTestCase

class TestLoginFunctionality(BaseTestCase):

    @patch('control.LoginControl.LoginControl.receive_command', new_callable=AsyncMock)
    async def test_login_failure_entity(self, mock_receive_command):
        """Test failure to log in due to an internal error in the entity layer."""
        print("\nTest Started for: test_login_failure_entity")
        internal_error_message = "Failed to log in: Internal error"
        
        # Set up the mock to return an error message
        mock_receive_command.return_value = f"Control Layer Exception: {internal_error_message}"
        
        # Call the method under test
        result = await self.control.receive_command("login", "example_site")
        
        # Check results
        self.assertEqual(result, f"Control Layer Exception: {internal_error_message}", "Control layer failed to report entity error correctly.")
        print("Unit Test Passed for entity layer error handling.\n")

if __name__ == '__main__':
    unittest.main()
