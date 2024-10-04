import logging
import unittest
from unittest.mock import patch
from test_init import base_test_case, setup_logging, run_monitoring_loop

# Enable asyncio for all tests in this file
setup_logging()

class TestAvailabilityControl(unittest.TestCase):

    async def test_start_monitoring_availability_success(self):
        with patch('entity.AvailabilityEntity.AvailabilityEntity.check_availability') as mock_check:
            url = "https://example.com"
            mock_check.return_value = "Selected or default date is available for booking."
            
            expected_control_result = [
                ('Checked availability: Selected or default date is available for booking.', 
                 'Data saved to Excel file at ExportedFiles\\excelFiles\\check_availability.xlsx.', 
                 'HTML file saved and updated at ExportedFiles\\htmlFiles\\check_availability.html.'),
                'Monitoring stopped successfully!'
            ]
            
            # Run the monitoring loop once
            actual_control_result = await run_monitoring_loop(
                base_test_case.availability_control,
                base_test_case.availability_control.check_availability,
                url,
                "2024-10-01",
                1
            )

            logging.info(f"Control Layer Expected: {expected_control_result}")
            logging.info(f"Control Layer Received: {actual_control_result}")
            self.assertEqual(actual_control_result, expected_control_result, "Control layer assertion failed.")
            logging.info("Unit Test Passed for control layer.")


    async def test_start_monitoring_availability_already_running(self):
        with patch('entity.AvailabilityEntity.AvailabilityEntity.check_availability') as mock_check:
            url = "https://example.com"
            base_test_case.availability_control.is_monitoring = True
            expected_control_result = "Already monitoring availability."

            result = await base_test_case.availability_control.receive_command(
                "start_monitoring_availability", url, "2024-10-01", 5
            )

            logging.info(f"Control Layer Expected: {expected_control_result}")
            logging.info(f"Control Layer Received: {result}")
            self.assertEqual(result, expected_control_result, "Control layer failed to handle already running condition.")
            logging.info("Unit Test Passed for control layer already running handling.\n")


if __name__ == "__main__":
    unittest.main()


import pytest
import logging
from unittest.mock import patch, AsyncMock
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
setup_logging()


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

if __name__ == "__main__":
    pytest.main([__file__])







import pytest
import logging
from unittest.mock import patch, MagicMock
from test_init import base_test_case, setup_logging, log_test_start_end

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio

setup_logging()

async def test_login_success(base_test_case):
    """Test that the login is successful when valid credentials are provided."""
    # Patch methods
    with patch('entity.BrowserEntity.BrowserEntity.login') as mock_login:
        with patch('control.AccountControl.AccountControl.fetch_account_by_website') as mock_fetch_account:
            # Setup mock return values
            mock_login.return_value = "Logged in to http://example.com successfully with username: sample_username"
            mock_fetch_account.return_value = ("sample_username", "sample_password")
            
            expected_entity_result = "Logged in to http://example.com successfully with username: sample_username"
            expected_control_result = f"Control Object Result: {expected_entity_result}"
            
            # Execute the command
            result = await base_test_case.browser_control.receive_command("login", site="example.com")
            
            # Assert results and logging
            logging.info(f"Entity Layer Expected: {expected_entity_result}")
            logging.info(f"Entity Layer Received: {mock_login.return_value}")
            assert mock_login.return_value == expected_entity_result, "Entity layer assertion failed."
            logging.info("Unit Test Passed for entity layer.\n")
            
            logging.info(f"Control Layer Expected: {expected_control_result}")
            logging.info(f"Control Layer Received: {result}")
            assert result == expected_control_result, "Control layer assertion failed."
            logging.info("Unit Test Passed for control layer.")


if __name__ == "__main__":
    pytest.main([__file__])


    """    forget to initailize and commented out something in the test_init #bto_control"""

        """   Infinite loop not broken, thats an error cause"""
