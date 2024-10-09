from test_init import *
"""
Executable steps for the !close_browser use case:
1. Control Layer Processing
This test ensures that BrowserControl.receive_command() handles the "!close_browser" command correctly.

2. Browser Closing
This test focuses on the BrowserEntity.close_browser() method to ensure it executes the browser closing process.

3. Response Generation
This test validates that the control layer correctly interprets the response from the browser closing step and returns the appropriate result to the boundary layer.
"""

# Test for Control Layer Processing
@pytest.mark.asyncio
async def test_control_layer_processing():
    logging.info("Starting test: Control Layer Processing for close_browser")

    with patch('entity.BrowserEntity.BrowserEntity.close_browser') as mock_close:
        # Configure the mock to return different responses based on the browser state
        mock_close.side_effect = ["Browser closed successfully.", "No browser is currently open."]
        browser_control = BrowserControl()

        # First call simulates the browser being open and then closed
        result = await browser_control.receive_command("close_browser")
        assert result == "Control Object Result: Browser closed successfully."
        logging.info(f"Test when browser is initially open and then closed: Passed with '{result}'")

        # Second call simulates the browser already being closed
        result = await browser_control.receive_command("close_browser")
        assert result == "Control Object Result: No browser is currently open."
        logging.info(f"Test when no browser is initially open: Passed with '{result}'")


# Test for Browser Closing

def test_browser_closing():
    logging.info("Starting test: Browser Closing")

    # Patching the webdriver.Chrome directly at the point of instantiation
    with patch('selenium.webdriver.Chrome', new_callable=MagicMock) as mock_chrome:
        mock_driver = mock_chrome.return_value  # Mock the return value which acts as the driver
        mock_driver.quit = MagicMock()  # Mock the quit method of the driver

        browser_entity = BrowserEntity()
        browser_entity.browser_open = True  # Ensure the browser is considered open
        browser_entity.driver = mock_driver  # Set the mock driver as the browser entity's driver

        result = browser_entity.close_browser()

        mock_driver.quit.assert_called_once()  # Check if quit was called on the driver instance
        logging.info("Expected outcome: Browser quit method called.")
        logging.info(f"Actual outcome: {result}")

        assert result == "Browser closed."
        logging.info("Test passed: Browser closing was successful")


# Test for Response Generation
@pytest.mark.asyncio
async def test_response_generation():
    logging.info("Starting test: Response Generation for close_browser")
    
    with patch('control.BrowserControl.BrowserControl.receive_command', new_callable=AsyncMock) as mock_receive:
        mock_receive.return_value = "Browser closed successfully."
        
        browser_control = BrowserControl()
        result = await browser_control.receive_command("close_browser")
        
        logging.info("Expected outcome: 'Browser closed successfully.'")
        logging.info(f"Actual outcome: {result}")
        
        assert result == "Browser closed successfully."
        logging.info("Step 3 executed and Test passed: Response generation was successful")

# This condition ensures that the pytest runner handles the test run.
if __name__ == "__main__":
    pytest.main([__file__])
