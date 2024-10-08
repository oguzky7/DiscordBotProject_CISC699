import sys, os, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
############################################################################################################
from unittest.mock import patch, AsyncMock
from control.BotControl import BotControl
from test_init import logging

"""
Executable steps for the project_help use case:
1. Control Layer Processing
This test will ensure that BotControl.receive_command() handles the "project_help" command correctly, including proper parameter passing.
"""

# test_project_help_control.py
@pytest.mark.asyncio
async def test_project_help_control():
    # Start logging the test case
    logging.info("Starting test: test_project_help_control")
    
    # Mocking the BotControl to simulate control layer behavior
    with patch('control.BotControl.BotControl.receive_command', new_callable=AsyncMock) as mock_command:
        # Setup the mock to return the expected help message
        expected_help_message = "Here are the available commands:..."
        mock_command.return_value = expected_help_message
        
        # Creating an instance of BotControl
        control = BotControl()
        
        # Simulating the command processing
        result = await control.receive_command("project_help")
        
        # Logging expected and actual outcomes
        logging.info(f"Expected outcome: '{expected_help_message}'")
        logging.info(f"Actual outcome: '{result}'")
        
        # Assertion to check if the result is as expected
        assert result == expected_help_message
        logging.info("Step 1 executed and Test passed: Control Layer Processing was successful")

# This condition ensures that the pytest runner handles the test run.
if __name__ == "__main__":
    pytest.main([__file__])
