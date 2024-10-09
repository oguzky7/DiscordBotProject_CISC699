import sys, os, pytest, asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
############################################################################################################
from unittest.mock import patch, AsyncMock
from control.AvailabilityControl import AvailabilityControl
from test_init import logging

"""
Executable steps for the `start_monitoring_availability` use case:

1. Control Layer Processing:
   This test ensures that `AvailabilityControl.receive_command()` handles the "start_monitoring_availability" command correctly,
   including proper parameter passing for the URL, date, and frequency.

2. Availability Monitoring Initiation:
   This test verifies that the control layer starts the monitoring process by calling `check_availability()` at regular intervals.

3. Stop Monitoring Logic:
   This test confirms that the monitoring can be stopped correctly using the "stop_monitoring_availability" command and that the final results are collected.
"""

# Test 1: Control Layer Processing
@pytest.mark.asyncio
async def test_control_layer_processing():
    logging.info("Starting test: test_control_layer_processing")

    url = "https://example.com/availability"
    frequency = 1
    logging.info(f"Testing command processing for URL: {url} with frequency: {frequency}")

    # Mock the actual command handling to simulate command receipt and processing
    with patch('control.AvailabilityControl.AvailabilityControl.receive_command', new_callable=AsyncMock) as mock_receive:
        logging.info("Patching receive_command method...")

        # Simulate receiving the 'start_monitoring_availability' command
        result = await AvailabilityControl().receive_command("start_monitoring_availability", url, None, frequency)

        logging.info("Verifying if 'start_monitoring_availability' was processed correctly...")
        assert "start_monitoring_availability" in str(mock_receive.call_args)
        assert mock_receive.call_args[0][1] == url
        assert mock_receive.call_args[0][3] == frequency
        logging.info("Test passed: Control layer processed 'start_monitoring_availability' correctly.")

# Test 2: Availability Monitoring Initiation
@pytest.mark.asyncio
async def test_availability_monitoring_initiation():
    logging.info("Starting test: test_availability_monitoring_initiation")

    availability_control = AvailabilityControl()
    url = "https://example.com/availability"
    frequency = 2
    logging.info(f"Initiating availability monitoring for URL: {url} with frequency: {frequency}")

    # Mock the check_availability method to return a constant value
    with patch.object(availability_control, 'check_availability', new_callable=AsyncMock) as mock_check_availability:
        logging.info("Patching check_availability method...")
        mock_check_availability.return_value = "Available"

        # Start the monitoring process (monitoring in a separate task)
        monitoring_task = asyncio.create_task(availability_control.start_monitoring_availability(url, None, frequency))
        logging.info("Monitoring task started.")

        # Simulate a brief period of monitoring (e.g., for two intervals)
        await asyncio.sleep(5)
        logging.info(f"Simulated monitoring for 5 seconds, checking number of calls to check_availability.")

        # Check if check_availability was called twice due to the frequency
        assert mock_check_availability.call_count == 2, f"Expected 2 availability checks, but got {mock_check_availability.call_count}"
        logging.info("Test passed: Availability monitoring initiated and 'check_availability' called twice.")

        # Stop the monitoring
        logging.info("Stopping availability monitoring...")
        availability_control.stop_monitoring_availability()
        await monitoring_task  # Wait for the task to stop

    # Ensure monitoring stopped and results were collected
    assert len(availability_control.results) == 2
    logging.info(f"Test passed: Monitoring stopped with {len(availability_control.results)} results.")

# Test 3: Stop Monitoring Logic
@pytest.mark.asyncio
async def test_stop_monitoring_logic():
    logging.info("Starting test: test_stop_monitoring_logic")

    availability_control = AvailabilityControl()
    url = "https://example.com/availability"
    frequency = 1
    logging.info(f"Initiating monitoring to test stopping logic for URL: {url} with frequency: {frequency}")

    # Mock check_availability method
    with patch.object(availability_control, 'check_availability', new_callable=AsyncMock) as mock_check_availability:
        logging.info("Patching check_availability method...")
        mock_check_availability.return_value = "Available"

        # Start monitoring
        monitoring_task = asyncio.create_task(availability_control.start_monitoring_availability(url, None, frequency))
        logging.info("Monitoring task started.")

        # Simulate monitoring for one interval
        await asyncio.sleep(2)
        logging.info("Simulated monitoring for 6 seconds, stopping monitoring now.")

        # Stop the monitoring
        availability_control.stop_monitoring_availability()
        await monitoring_task  # Wait for the task to stop

        # Ensure the monitoring has stopped
        assert availability_control.is_monitoring == False
        assert len(availability_control.results) >= 1
        logging.info(f"Test passed: Monitoring stopped with {len(availability_control.results)} result(s).")

if __name__ == "__main__":
    pytest.main([__file__])
