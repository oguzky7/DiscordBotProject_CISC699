import pytest, logging
from unittest.mock import patch
from test_init import base_test_case, setup_logging, log_test_start_end
import asyncio

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()

async def test_stop_monitoring_availability_success(base_test_case):
    # Simulate the case where monitoring is already running
    base_test_case.availability_control.is_monitoring = True
    base_test_case.availability_control.results = ["Checked availability: Selected or default date is available for booking."]
    
    # Expected message to be present in the result
    expected_control_result_contains = "Monitoring stopped successfully!"
    
    # Execute the stop command
    result = base_test_case.availability_control.stop_monitoring_availability()
    
    # Log and assert the outcomes
    logging.info(f"Control Layer Expected to contain: {expected_control_result_contains}")
    logging.info(f"Control Layer Received: {result}")
    
    assert expected_control_result_contains in result, "Control layer assertion failed for stop monitoring."
    logging.info("Unit Test Passed for stop monitoring availability.")

async def test_stop_monitoring_availability_no_active_session(base_test_case):
    # Simulate the case where no monitoring session is active
    base_test_case.availability_control.is_monitoring = False
    expected_control_result = "There was no active availability monitoring session. Nothing to stop."
    
    # Execute the stop command
    result = base_test_case.availability_control.stop_monitoring_availability()
    
    # Log and assert the outcomes
    logging.info(f"Control Layer Expected: {expected_control_result}")
    logging.info(f"Control Layer Received: {result}")
    assert result == expected_control_result, "Control layer assertion failed for no active session."
    logging.info("Unit Test Passed for stop monitoring with no active session.")

if __name__ == "__main__":
    pytest.main([__file__])
