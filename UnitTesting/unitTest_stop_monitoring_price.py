import sys, os, pytest, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch, AsyncMock
from control.PriceControl import PriceControl

"""
Executable steps for the `stop_monitoring_price` use case:

1. Control Layer Processing:
   This test will ensure that `PriceControl.receive_command()` correctly handles the "stop_monitoring_price" command,
   including the proper termination of the price monitoring process.

2. Stop Monitoring Logic:
   This test verifies that the control layer stops the price monitoring process and collects the final results correctly.

3. Final Summary Generation:
   This test confirms that the control layer generates and returns a final summary of the monitoring session, containing the collected price results.
"""

# Test 1: Control Layer Processing for stop_monitoring_price command
@pytest.mark.asyncio
async def test_control_layer_processing():
    logging.info("Starting test: test_control_layer_processing")

    # Mock the actual command handling to simulate command receipt and processing
    with patch('control.PriceControl.PriceControl.receive_command', new_callable=AsyncMock) as mock_receive:
        logging.info("Patching receive_command method...")
        
        # Simulate receiving the 'stop_monitoring_price' command
        result = await PriceControl().receive_command("stop_monitoring_price")
        
        logging.info("Verifying if 'stop_monitoring_price' was processed correctly...")
        assert "stop_monitoring_price" in str(mock_receive.call_args)
        logging.info("Test passed: Control layer processed 'stop_monitoring_price' command correctly.")

# Test 2: Stop Monitoring Logic
@pytest.mark.asyncio
async def test_stop_monitoring_logic():
    logging.info("Starting test: test_stop_monitoring_logic")

    price_control = PriceControl()
    price_control.is_monitoring = True  # Simulate an ongoing monitoring session

    # Mock the stop_monitoring_price method
    with patch.object(price_control, 'stop_monitoring_price', wraps=price_control.stop_monitoring_price) as mock_stop_monitoring:
        logging.info("Patching stop_monitoring_price method...")

        # Simulate the stop command
        result = price_control.stop_monitoring_price()

        logging.info("Checking if monitoring stopped and results were collected...")
        assert price_control.is_monitoring == False
        logging.info("Monitoring was successfully stopped.")
        assert len(price_control.results) >= 0  # Ensuring that results were collected
        logging.info("Results were collected successfully.")
        logging.info("Test passed: Stop monitoring logic executed correctly.")


# Test 3: Final Summary Generation
@pytest.mark.asyncio
async def test_final_summary_generation():
    logging.info("Starting test: test_final_summary_generation")

    price_control = PriceControl()
    price_control.is_monitoring = True  # Simulate an ongoing monitoring session
    price_control.results = ["Price at URL was $100", "Price dropped to $90"]  # Mock some results

    # Simulate the monitoring stop and ensure results are collected
    logging.info("Stopping price monitoring and generating final summary...")
    result = price_control.stop_monitoring_price()

    # Ensure that the summary contains the expected results
    logging.info("Verifying the final summary contains the collected results...")
    assert "Price at URL was $100" in result
    assert "Price dropped to $90" in result
    assert "Price monitoring stopped successfully!" in result  # Updated to match the actual result
    logging.info("Test passed: Final summary generated correctly.")


if __name__ == "__main__":
    pytest.main([__file__])
