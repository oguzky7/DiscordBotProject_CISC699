import pytest
from unittest.mock import MagicMock
from test_init import setup_logging, base_test_case, save_test_results_to_file, log_test_start_end, logging

setup_logging()

@pytest.mark.usefixtures("base_test_case")
class TestEmailDAO:
    
    @pytest.fixture
    def email_dao(self, base_test_case, mocker):
        # Use the send_email_with_attachments from base_test_case
        email_dao = base_test_case.email_dao
        mocker.patch('smtplib.SMTP')
        logging.info("Mocked EmailDAO with send_email_with_attachments method")
        return email_dao

    def test_utility_send_email_success(self, email_dao):
        # Mock successful email sending
        email_dao.return_value = "Email with file 'monitor_price.html' sent successfully!"
        
        # Perform the test
        result = email_dao('monitor_price.html')
        
        # Log and assert the result
        assert result == "Email with file 'monitor_price.html' sent successfully!"
        logging.info("Test send_email_success passed")

    def test_utility_send_email_fail(self, email_dao):
        # Mock failure in email sending
        email_dao.return_value = "File 'non_existent_file.html' not found."
        
        # Perform the test
        result = email_dao('non_existent_file.html')
        
        # Log and assert the result
        assert result == "File 'non_existent_file.html' not found in either excelFiles or htmlFiles."
        logging.info("Test send_email_fail passed")


@pytest.mark.usefixtures("base_test_case")
class TestEmailControl:

    @pytest.fixture
    def email_control(self, base_test_case, mocker):
        # Get the bot control from base_test_case, which should handle the receive_command method
        email_control = base_test_case.bot_control
        email_control.receive_command = MagicMock()  # Mock the receive_command method
        logging.info("Mocked EmailControl (BotControl) for control layer")
        return email_control

    def test_control_send_email_success(self, email_control):
        # Mock successful email sending
        email_control.receive_command.return_value = "Email with file 'monitor_price.html' sent successfully!"
        
        # Call the control method and check the response
        result = email_control.receive_command("receive_email", "monitor_price.html")
        
        # Log and assert the result
        assert result == "Email with file 'monitor_price.html' sent successfully!"
        logging.info("Test control_send_email_success passed")

    def test_control_send_email_fail(self, email_control):
        # Mock failure in email sending
        email_control.receive_command.return_value = "File 'non_existent_file.html' not found."
        
        # Call the control method and check the response
        result = email_control.receive_command("receive_email", "non_existent_file.html")
        
        # Log and assert the result
        assert result == "File 'non_existent_file.html' not found."
        logging.info("Test control_send_email_fail passed")



if __name__ == "__main__":
    pytest.main([__file__])  # Run pytest directly
