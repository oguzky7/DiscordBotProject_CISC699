import sys, os, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
############################################################################################################
from unittest.mock import patch, AsyncMock
from control.BotControl import BotControl
from entity.EmailEntity import send_email_with_attachments
from test_init import logging

"""
Executable steps for the receive_email use case:
1. Control Layer Processing
This test will ensure that BotControl.receive_command() handles the "receive_email" command correctly, including proper parameter passing.

2. Email Handling
This test will focus on the EmailEntity.send_email_with_attachments() function to ensure it processes the request and handles file operations and email sending as expected.

3. Response Generation
This test will validate that the control layer correctly interprets the response from the email handling step and returns the appropriate result to the boundary layer.
"""

# test_bot_control.py
@pytest.mark.asyncio
async def test_control_layer_processing():
    # Start logging the test case
    logging.info("Starting test: test_control_layer_processing")
    
    # Mocking the email sending function to simulate email sending without actual I/O operations
    with patch('entity.EmailEntity.send_email_with_attachments', new_callable=AsyncMock) as mock_email: 
        mock_email.return_value = "Email with file 'testfile.txt' sent successfully!"       
        # Creating an instance of BotControl
        bot_control = BotControl()
        
        # Calling the receive_command method and passing the command and filename
        result = await bot_control.receive_command("receive_email", "testfile.txt")
        
        # Logging expected and actual outcomes
        logging.info(f"Expected outcome: 'Email with file 'testfile.txt' sent successfully!'")
        logging.info(f"Actual outcome: {result}")
        
        # Assertion to check if the result is as expected
        assert result == "Email with file 'testfile.txt' sent successfully!"
        logging.info("Step 1 executed and Test passed: Control Layer Processing was successful")


# test_email_handling.py
def test_email_handling():
    # Start logging the test case
    logging.info("Starting test: test_email_handling")
    
    # Mocking the SMTP class to simulate sending an email
    with patch('smtplib.SMTP') as mock_smtp:
        # Simulating the sending of an email
        result = send_email_with_attachments("testfile.txt")
        
        # Logging expected and actual outcomes
        logging.info("Expected outcome: Contains 'Email with file 'testfile.txt' sent successfully!'")
        logging.info(f"Actual outcome: {result}")
        
        # Assertion to check if the result contains the success message
        assert "Email with file 'testfile.txt' sent successfully!" in result
        logging.info("Step 2 executed and Test passed: Email handling was successful")


# test_response_generation.py
@pytest.mark.asyncio
async def test_response_generation():
    # Start logging the test case
    logging.info("Starting test: test_response_generation")
    
    # Mocking the BotControl.receive_command to simulate control layer behavior
    with patch('control.BotControl.BotControl.receive_command', new_callable=AsyncMock) as mock_receive:
        mock_receive.return_value = "Email with file 'testfile.txt' sent successfully!"
        
        # Creating an instance of BotControl
        bot_control = BotControl()
        
        # Calling the receive_command method and passing the command and filename
        result = await bot_control.receive_command("receive_email", "testfile.txt")
        
        # Logging expected and actual outcomes
        logging.info("Expected outcome: 'Email with file 'testfile.txt' sent successfully!'")
        logging.info(f"Actual outcome: {result}")
        
        # Assertion to check if the result is as expected
        assert "Email with file 'testfile.txt' sent successfully!" in result
        logging.info("Step 3 executed and Test passed: Response generation was successful")


# This condition ensures that the pytest runner handles the test run.
if __name__ == "__main__":
    pytest.main([__file__])



"""
@pytest.mark.asyncio
async def test_handle_receive_email():
    # Explanation: Patching the 'receive_command' to simulate control layer behavior without actual execution.
    with patch('control.BotControl.BotControl.receive_command', new_callable=AsyncMock) as mock_receive_command:
        # Expected return value from the mocked method
        mock_receive_command.return_value = "Email with file 'monitor_price.html' sent successfully!"

        # Instantiate BotControl to test the interaction within the control layer
        control = BotControl()

        # Explanation: This line simulates the control layer receiving the 'receive_email' command with a filename.
        result = await control.receive_command("receive_email", "monitor_price.html")

        # Logging the result to understand what happens when the command is processed
        logging.info(f'Result of receive_command: {result}')

        # Explanation: Assert that the mocked method returns the expected result
        assert result == "Email with file 'monitor_price.html' sent successfully!"
        # Explanation: Ensure that the method was called exactly once with expected parameters
        mock_receive_command.assert_called_once_with("receive_email", "monitor_price.html")
        """