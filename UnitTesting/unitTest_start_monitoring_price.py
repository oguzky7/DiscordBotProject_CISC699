import sys, os, pytest, asyncio, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch, AsyncMock
from control.PriceControl import PriceControl

"""
Executable steps for the `start_monitoring_price` use case:

1. Control Layer Processing:
   This test will ensure that `PriceControl.receive_command()` correctly handles the "start_monitoring_price" command,
   including proper URL and frequency parameter passing.

2. Price Monitoring Initiation:
   This test will verify that the control layer starts the monitoring process by repeatedly calling `get_price()` at regular intervals.

3. Stop Monitoring Logic:
   This test confirms that the monitoring can be stopped correctly using the "stop_monitoring_price" command and that final results are collected.
"""

# Test 1: Control Layer Processing for start_monitoring_price command
@pytest.mark.asyncio
async def test_control_layer_processing():
    logging.info("Starting test: test_control_layer_processing")

    url = "https://example.com/product"
    frequency = 2
    logging.info(f"Testing command processing for URL: {url} with frequency: {frequency}")

    # Mock the actual command handling to simulate command receipt and processing
    with patch('control.PriceControl.PriceControl.receive_command', new_callable=AsyncMock) as mock_receive:
        logging.info("Patching receive_command method...")
        
        # Simulate receiving the 'start_monitoring_price' command
        result = await PriceControl().receive_command("start_monitoring_price", url, frequency)
        
        logging.info("Verifying if 'start_monitoring_price' was processed correctly...")
        assert "start_monitoring_price" in str(mock_receive.call_args)
        assert mock_receive.call_args[0][1] == url
        assert mock_receive.call_args[0][2] == frequency
        logging.info("Test passed: Control layer processed 'start_monitoring_price' correctly.")

# Test 2: Price Monitoring Initiation
@pytest.mark.asyncio
async def test_price_monitoring_initiation():
    logging.info("Starting test: test_price_monitoring_initiation")

    price_control = PriceControl()
    url = "https://example.com/product"
    frequency = 3
    logging.info(f"Initiating price monitoring for URL: {url} with frequency: {frequency}")

    # Mock the get_price method to return a constant value
    with patch.object(price_control, 'get_price', new_callable=AsyncMock) as mock_get_price:
        logging.info("Patching get_price method...")
        mock_get_price.return_value = "100.00"

        # Start the monitoring process (monitoring in a separate task)
        monitoring_task = asyncio.create_task(price_control.start_monitoring_price(url, frequency))
        logging.info("Monitoring task started.")

        # Simulate a brief period of monitoring (e.g., two intervals)
        await asyncio.sleep(8)
        logging.info(f"Simulated monitoring for 5 seconds, checking number of calls to get_price.")

        # Check if get_price was called twice due to the frequency
        assert mock_get_price.call_count == 2, f"Expected 2 price checks, but got {mock_get_price.call_count}"
        logging.info("Test passed: Price monitoring initiated and 'get_price' called twice.")

        # Stop the monitoring
        logging.info("Stopping price monitoring...")
        price_control.stop_monitoring_price()
        await monitoring_task  # Wait for the task to stop

    # Ensure monitoring stopped and results were collected
    assert len(price_control.results) == 2
    logging.info(f"Test passed: Monitoring stopped with {len(price_control.results)} results.")

# Test 3: Stop Monitoring Logic
@pytest.mark.asyncio
async def test_stop_monitoring_logic():
    logging.info("Starting test: test_stop_monitoring_logic")

    price_control = PriceControl()
    url = "https://example.com/product"
    frequency = 2
    logging.info(f"Initiating monitoring to test stopping logic for URL: {url} with frequency: {frequency}")

    # Mock get_price method
    with patch.object(price_control, 'get_price', new_callable=AsyncMock) as mock_get_price:
        logging.info("Patching get_price method...")
        mock_get_price.return_value = "100.00"

        # Start monitoring
        monitoring_task = asyncio.create_task(price_control.start_monitoring_price(url, frequency))
        logging.info("Monitoring task started.")

        # Simulate monitoring for one interval
        await asyncio.sleep(3)
        logging.info("Simulated monitoring for 3 seconds, stopping monitoring now.")

        # Stop the monitoring
        price_control.stop_monitoring_price()
        await monitoring_task  # Wait for the task to stop

        # Ensure the monitoring has stopped
        assert price_control.is_monitoring == False
        assert len(price_control.results) >= 1
        logging.info(f"Test passed: Monitoring stopped with {len(price_control.results)} result(s).")

if __name__ == "__main__":
    pytest.main([__file__])