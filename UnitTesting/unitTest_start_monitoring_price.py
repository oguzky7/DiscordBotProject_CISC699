import pytest
import logging
from unittest.mock import patch, AsyncMock
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()


async def test_start_monitoring_price_success(base_test_case):
    with patch('entity.PriceEntity.PriceEntity.get_price_from_page', return_value="100 USD") as mock_get_price:
        
        # Setup expected outcomes
        url = "https://example.com/product"
        expected_result = "Starting price monitoring. Current price: 100 USD"
        
        # Mocking the sleep method to break out of the loop after the first iteration
        with patch('asyncio.sleep', side_effect=KeyboardInterrupt):
            try:
                # Execute the command
                base_test_case.price_control.is_monitoring = False
                result = await base_test_case.price_control.receive_command("start_monitoring_price", url, 1)
            except KeyboardInterrupt:
                # Force the loop to stop after the first iteration
                base_test_case.price_control.is_monitoring = False
        
        # Log and assert the outcomes
        logging.info(f"Entity Layer Expected: {expected_result}")
        logging.info(f"Control Layer Received: {base_test_case.price_control.results[0]}")
        assert expected_result in base_test_case.price_control.results[0], "Price monitoring did not start as expected."
        logging.info("Unit Test Passed for start_monitoring_price success scenario.\n")


async def test_start_monitoring_price_already_running(base_test_case):
    # Test when price monitoring is already running
    base_test_case.price_control.is_monitoring = True
    expected_result = "Already monitoring prices."
    
    # Execute the command
    result = await base_test_case.price_control.receive_command("start_monitoring_price", "https://example.com/product", 1)
    
    # Log and assert the outcomes
    logging.info(f"Control Layer Expected: {expected_result}")
    logging.info(f"Control Layer Received: {result}")
    assert result == expected_result, "Control layer did not detect that monitoring was already running."
    logging.info("Unit Test Passed for already running scenario.\n")


async def test_start_monitoring_price_failure_in_entity(base_test_case):
    # Mock entity failure during price fetching
    with patch('entity.PriceEntity.PriceEntity.get_price_from_page', side_effect=Exception("Error fetching price")) as mock_get_price:
        
        # Setup expected outcomes
        url = "https://example.com/product"
        expected_result = "Starting price monitoring. Current price: Failed to fetch price: Error fetching price"
        
        # Mocking the sleep method to break out of the loop after the first iteration
        with patch('asyncio.sleep', side_effect=KeyboardInterrupt):
            try:
                # Execute the command
                base_test_case.price_control.is_monitoring = False
                await base_test_case.price_control.receive_command("start_monitoring_price", url, 1)
            except KeyboardInterrupt:
                # Force the loop to stop after the first iteration
                base_test_case.price_control.is_monitoring = False
        
        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_result}")
        logging.info(f"Control Layer Received: {base_test_case.price_control.results[-1]}")
        assert expected_result in base_test_case.price_control.results[-1], "Entity layer did not handle failure correctly."
        logging.info("Unit Test Passed for entity layer failure scenario.\n")


async def test_start_monitoring_price_failure_in_control(base_test_case):
    # Mock control layer failure
    with patch('control.PriceControl.PriceControl.start_monitoring_price', side_effect=Exception("Control Layer Exception")) as mock_start_monitoring:
        
        # Setup expected outcomes
        expected_result = "Control Layer Exception"
        
        # Execute the command and catch the raised exception
        try:
            result = await base_test_case.price_control.receive_command("start_monitoring_price", "https://example.com/product", 1)
        except Exception as e:
            result = f"Control Layer Exception: {str(e)}"
        
        # Log and assert the outcomes
        logging.info(f"Control Layer Expected: {expected_result}")
        logging.info(f"Control Layer Received: {result}")
        assert expected_result in result, "Control layer did not handle the failure correctly."
        logging.info("Unit Test Passed for control layer failure scenario.\n")


if __name__ == "__main__":
    pytest.main([__file__])
