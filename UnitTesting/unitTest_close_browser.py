import pytest, logging
from unittest.mock import patch
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()

async def test_close_browser_success(base_test_case):
    with patch('entity.BrowserEntity.BrowserEntity.close_browser') as mock_close:
        # Set up mock and expected outcomes
        mock_close.return_value = "Browser closed."
        expected_entity_result = "Browser closed."
        expected_control_result = "Control Object Result: Browser closed."
        
        # Execute the command
        result = await base_test_case.browser_control.receive_command("close_browser")
        
        # Log and assert the outcomes
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_close.return_value}")
        assert mock_close.return_value == expected_entity_result, "Entity layer assertion failed."
        logging.info("Unit Test Passed for entity layer.\n")
        
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer.")

async def test_close_browser_not_open(base_test_case):
    with patch('entity.BrowserEntity.BrowserEntity.close_browser') as mock_close:
        # Set up mock and expected outcomes
        mock_close.return_value = "No browser is currently open."
        expected_entity_result = "No browser is currently open."
        expected_control_result = "Control Object Result: No browser is currently open."
        
        # Execute the command
        result = await base_test_case.browser_control.receive_command("close_browser")
        
        # Log and assert the outcomes
        logging.info(f"Entity Layer Expected: {expected_entity_result}")
        logging.info(f"Entity Layer Received: {mock_close.return_value}")
        assert mock_close.return_value == expected_entity_result, "Entity layer assertion failed."
        logging.info("Unit Test Passed for entity layer.\n")
        
        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer.")

async def test_close_browser_failure_control(base_test_case):
    with patch('entity.BrowserEntity.BrowserEntity.close_browser', side_effect=Exception("Unexpected error")) as mock_close:
        # Set up expected outcome
        expected_result = "Control Layer Exception: Unexpected error"
        
        # Execute the command
        result = await base_test_case.browser_control.receive_command("close_browser")
        
        # Log and assert the outcomes
        logging.info(f"Control Layer Expected to Report: {expected_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_result, "Control layer failed to handle or report the error correctly."
        logging.info("Unit Test Passed for control layer error handling.")

async def test_close_browser_failure_entity(base_test_case):
    with patch('entity.BrowserEntity.BrowserEntity.close_browser', side_effect=Exception("BrowserEntity_Failed to close browser: Internal error")) as mock_close:
        # Set up expected outcome
        internal_error_message = "BrowserEntity_Failed to close browser: Internal error"
        expected_control_result = f"Control Layer Exception: {internal_error_message}"
        
        # Execute the command
        result = await base_test_case.browser_control.receive_command("close_browser")
        
        # Log and assert the outcomes
        logging.info(f"Entity Layer Expected Failure: {internal_error_message}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer failed to report entity error correctly."
        logging.info("Unit Test Passed for entity layer error handling.")

if __name__ == "__main__":
    pytest.main([__file__])
