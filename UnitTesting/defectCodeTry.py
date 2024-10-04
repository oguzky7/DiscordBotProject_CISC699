import pytest
import logging
from unittest.mock import patch, AsyncMock
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()

async def test_stop_monitoring_price_success(base_test_case):
    # Set up monitoring to be active
    base_test_case.price_control.is_monitoring = True
    base_test_case.price_control.results = ["Price went up!", "Price went down!"]

    # Expected result after stopping monitoring
    expected_result = "Results for price monitoring:Price went up!\nPrice went down!\nPrice monitoring stopped successfully!"
    
    # Execute the command
    result = base_test_case.price_control.stop_monitoring_price()

    # Log and assert the outcomes
    logging.info(f"Control Layer Expected: {expected_result}")
    logging.info(f"Control Layer Received: {result}")
    assert result == expected_result, "Control layer did not return the correct results for stopping monitoring."
    logging.info("Unit Test Passed for stop_monitoring_price success scenario.\n")


if __name__ == "__main__":
    pytest.main([__file__])
