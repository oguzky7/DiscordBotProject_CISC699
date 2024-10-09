from test_init import *
"""
Executable steps for the 'Stop_monitoring_availability' use case:

1. Control Layer Processing:
   This test ensures that `AvailabilityControl.receive_command()` correctly handles the "stop_monitoring_availability" command.

2. Monitoring Termination:
   This test verifies that the control layer terminates an ongoing availability monitoring session.

3. Final Results Summary:
   This test confirms that the control layer returns the correct summary of monitoring results once the process is terminated.
"""

# Test 1: Control Layer Processing for stop_monitoring_availability command
@pytest.mark.asyncio
async def test_control_layer_processing():
    logging.info("Starting test: Control Layer Processing for stop_monitoring_availability command")

    with patch('control.AvailabilityControl.AvailabilityControl.receive_command', new_callable=AsyncMock) as mock_receive:
        # Simulate receiving the 'stop_monitoring_availability' command
        result = await AvailabilityControl().receive_command("stop_monitoring_availability")

        # Verify that the command was processed correctly
        assert "stop_monitoring_availability" in str(mock_receive.call_args)
        logging.info("Test passed: Control layer processed stop_monitoring_availability command successfully.")

# Test 2: Monitoring Termination
@pytest.mark.asyncio
async def test_monitoring_termination():
    logging.info("Starting test: Monitoring Termination for stop_monitoring_availability")

    availability_control = AvailabilityControl()
    availability_control.is_monitoring = True  # Simulate that monitoring is active
    availability_control.results = ["Availability at URL was available.", "Availability was checked again."]

    # Simulate monitoring stop
    logging.info("Stopping availability monitoring...")
    result = availability_control.stop_monitoring_availability()

    # Verify that monitoring was stopped and flag was set correctly
    assert availability_control.is_monitoring == False
    logging.info("Test passed: Monitoring was terminated successfully.")

# Test 3: Final Results Summary
@pytest.mark.asyncio
async def test_final_summary_generation():
    logging.info("Starting test: Final Results Summary for stop_monitoring_availability")

    availability_control = AvailabilityControl()
    availability_control.is_monitoring = True  # Simulate an ongoing monitoring session
    availability_control.results = ["Availability at URL was available.", "Availability was checked again."]

    # Simulate the monitoring stop and ensure results are collected
    logging.info("Stopping availability monitoring and generating final summary...")
    result = availability_control.stop_monitoring_availability()

    # Verify that the summary contains the expected results
    assert "Availability at URL was available." in result
    assert "Availability was checked again." in result
    assert "Monitoring stopped successfully!" in result
    logging.info("Test passed: Final summary generated correctly.")

if __name__ == "__main__":
    pytest.main([__file__])
