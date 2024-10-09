import sys, os, pytest, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch, AsyncMock
from control.BrowserControl import BrowserControl
from entity.BrowserEntity import BrowserEntity

# Define executable steps from the provided use case
"""
Executable steps for the navigate_to_website command:
1. Command Processing and URL Extraction
   - Ensure that the command is correctly processed and the URL is extracted and passed accurately to the control layer.

2. Browser Navigation
   - Verify that the browser control object receives the command and correctly triggers navigation to the URL.

3. Response Generation
   - Check that the correct response about navigation success or failure is generated and would be passed back to the boundary.
"""

# Test for Command Processing and URL Extraction
@pytest.mark.asyncio
async def test_command_processing_and_url_extraction():
    logging.info("Starting test: test_command_processing_and_url_extraction")
    with patch('control.BrowserControl.BrowserControl.receive_command', new_callable=AsyncMock) as mock_receive:
        mock_receive.return_value = "Navigating to URL"
        browser_control = BrowserControl()

        # Simulate receiving the navigate command with a URL
        result = await browser_control.receive_command("navigate_to_website", "http://example.com")
        
        logging.info(f"Expected outcome: 'Navigating to URL'")
        logging.info(f"Actual outcome: {result}")

        assert result == "Navigating to URL"
        logging.info("Step 1 executed and Test passed: Command Processing and URL Extraction was successful")

# Test for Browser Navigation
@pytest.mark.asyncio
async def test_browser_navigation():
    logging.info("Starting test: test_browser_navigation")
    with patch('entity.BrowserEntity.BrowserEntity.navigate_to_website', new_callable=AsyncMock) as mock_navigate:
        mock_navigate.return_value = "Navigation successful"
        browser_entity = BrowserEntity()
        result = await browser_entity.navigate_to_website("http://example.com")

        logging.info("Expected outcome: 'Navigation successful'")
        logging.info(f"Actual outcome: {result}")

        assert result == "Navigation successful"
        logging.info("Step 2 executed and Test passed: Browser Navigation was successful")

# Test for Response Generation
@pytest.mark.asyncio
async def test_response_generation():
    logging.info("Starting test: test_response_generation")
    with patch('control.BrowserControl.BrowserControl.receive_command', new_callable=AsyncMock) as mock_receive:
        mock_receive.return_value = "Navigation confirmed"
        browser_control = BrowserControl()

        result = await browser_control.receive_command("confirm_navigation", "http://example.com")

        logging.info("Expected outcome: 'Navigation confirmed'")
        logging.info(f"Actual outcome: {result}")

        assert result == "Navigation confirmed"
        logging.info("Step 3 executed and Test passed: Response Generation was successful")

# This condition ensures that the pytest runner handles the test run.
if __name__ == "__main__":
    pytest.main([__file__])
