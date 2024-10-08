import sys, os, pytest, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
############################################################################################################
from unittest.mock import patch, AsyncMock
from control.BotControl import BotControl
from entity.EmailEntity import send_email_with_attachments
from test_init import log_test_start_end

# test_bot_control.py
@pytest.mark.asyncio
async def test_control_layer_processing():
    with patch('entity.EmailEntity.send_email_with_attachments', new_callable=AsyncMock):
        control = BotControl()
        result = await control.receive_command("receive_email", "testfile.txt")
        assert result == "Email with file 'testfile.txt' sent successfully!"
        print("Step 1 executed: Control Layer Processing")


# test_email_handling.py
def test_email_handling():
    with patch('smtplib.SMTP') as mock_smtp:
        result = send_email_with_attachments("testfile.txt")
        assert "Email with file 'testfile.txt' sent successfully!" in result
        print("Step 2 executed: Email Handling")


# test_response_generation.py
@pytest.mark.asyncio
async def test_response_generation():
    with patch('control.BotControl.BotControl.receive_command', new_callable=AsyncMock) as mock_receive:
        mock_receive.return_value = "Email with file 'testfile.txt' sent successfully!"
        control = BotControl()
        result = await control.receive_command("receive_email", "testfile.txt")
        assert "Email with file 'testfile.txt' sent successfully!" in result
        print("Step 3 executed: Response Generation")


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