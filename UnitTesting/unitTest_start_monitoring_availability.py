import pytest, logging
from unittest.mock import patch
from test_init import base_test_case, setup_logging, run_monitoring_loop, log_test_start_end
import asyncio

# Enable asyncio for all tests in this file
pytestmark = pytest.mark.asyncio
setup_logging()

async def test_start_monitoring_availability_success(base_test_case):
    with patch('entity.AvailabilityEntity.AvailabilityEntity.check_availability') as mock_check:
        url = "https://example.com"
        mock_check.return_value = "Selected or default date is available for booking."
        
        expected_control_result = [
            "Checked availability: Selected or default date is available for booking.",
            "Monitoring stopped successfully!"
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
        assert actual_control_result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer.")


async def test_start_monitoring_availability_failure_entity(base_test_case):
    with patch('entity.AvailabilityEntity.AvailabilityEntity.check_availability', side_effect=Exception("Failed to check availability")):
        url = "https://example.com"
        expected_control_result = [
            "Failed to check availability: Failed to check availability",
            "Monitoring stopped successfully!"
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
        assert actual_control_result == expected_control_result, "Control layer failed to handle entity error correctly."
        logging.info("Unit Test Passed for entity layer error handling.")


async def test_start_monitoring_availability_failure_control(base_test_case):
    with patch('control.AvailabilityControl.AvailabilityControl.receive_command', side_effect=Exception("Control Layer Failed")):
        url = "https://example.com"
        expected_control_result = "Control Layer Exception: Control Layer Failed"

        try:
            result = await base_test_case.availability_control.receive_command("start_monitoring_availability", url, "2024-10-01", 5)
        except Exception as e:
            result = f"Control Layer Exception: {str(e)}"

        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer assertion failed."
        logging.info("Unit Test Passed for control layer failure.")


async def test_start_monitoring_availability_already_running(base_test_case):
    with patch('entity.AvailabilityEntity.AvailabilityEntity.check_availability') as mock_check:
        url = "https://example.com"
        base_test_case.availability_control.is_monitoring = True
        expected_control_result = "Already monitoring availability."

        result = await base_test_case.availability_control.receive_command("start_monitoring_availability", url, "2024-10-01", 5)

        logging.info(f"Control Layer Expected: {expected_control_result}")
        logging.info(f"Control Layer Received: {result}")
        assert result == expected_control_result, "Control layer failed to handle already running condition."
        logging.info("Unit Test Passed for control layer already running handling.\n")


if __name__ == "__main__":
    pytest.main([__file__])
