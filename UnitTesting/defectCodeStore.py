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




