import sys, os, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch
from control.BrowserControl import BrowserControl
from test_init import logging

@pytest.mark.asyncio
async def test_close_browser():
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

if __name__ == "__main__":
    pytest.main([__file__])
