import sys, os, pytest, asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
############################################################################################################
from unittest.mock import patch, AsyncMock
from control.AvailabilityControl import AvailabilityControl

"""
Executable steps for the `start_monitoring_availability` use case:

1. Control Layer Processing
   This test ensures that `AvailabilityControl.receive_command()` handles the "start_monitoring_availability" command correctly,
   including proper parameter passing for the URL, date, and frequency.

2. Availability Monitoring Initiation
   This test verifies that the control layer starts the monitoring process by calling `check_availability()` at regular intervals.

3. Stop Monitoring Logic
   This test confirms that the monitoring can be stopped correctly using the "stop_monitoring_availability" command and that the final results are collected.
"""

# Test 3: Email Notification Trigger
@pytest.mark.asyncio
async def test_email_notification_trigger():
    availability_control = AvailabilityControl()
    
    # Mock both check_availability and email sending
    with patch.object(availability_control, 'check_availability', new_callable=AsyncMock) as mock_check_availability, \
         patch('entity.EmailEntity.send_email_with_attachments', new_callable=AsyncMock) as mock_send_email:
        
        # Mock the return value for check_availability to "Available"
        mock_check_availability.return_value = "Available"
        
        url = "https://example.com/availability"
        frequency = 5
        
        # Start monitoring availability
        monitoring_task = asyncio.create_task(availability_control.start_monitoring_availability(url, None, frequency))
        
        # Simulate monitoring for two intervals
        await asyncio.sleep(11)
        
        # Check if email was sent twice (once per check)
        print(f"Email send function call count: {mock_send_email.call_count}")
        assert mock_send_email.call_count == 2, f"Expected 2 emails to be sent, but got {mock_send_email.call_count} instead."
        
        # Stop the monitoring
        availability_control.stop_monitoring_availability()
        await monitoring_task  # Wait for the task to finish

if __name__ == "__main__":
    pytest.main([__file__])
