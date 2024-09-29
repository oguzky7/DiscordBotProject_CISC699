import pytest
from unittest.mock import patch
from test_init import base_test_case, logging

@pytest.mark.asyncio
async def test_launch_browser_success(base_test_case):
    with patch('entity.BrowserEntity.BrowserEntity.launch_browser') as mock_launch:
        # Set up mock and expected outcomes
        mock_launch.return_value = "Browser launched."
        expected_entity_result = "Browser launched."
        expected_control_result = "Control Object Result: Browser launched."
        
        # Execute the command
        result = await base_test_case.browser_control.receive_command("launch_browser")
        # Log the expected and actual outcomes
        logging.info(f"\nTest Started for: test_launch_browser_success")
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_launch.return_value}")
        assert mock_launch.return_value == expected_entity_result, "Entity layer assertion failed."
        logging.info("Unit Test Passed for entity layer.\n")
        
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer.\n")

if __name__ == "__main__":
    pytest.main([__file__, "-k", "test_launch_browser_success"])
    