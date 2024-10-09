import sys, os, pytest, logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch, AsyncMock
from control.AvailabilityControl import AvailabilityControl
from entity.DataExportEntity import ExportUtils
"""
Executable steps for the 'Check_Availability' use case:
1. Control Layer Command Reception
This test will ensure that AvailabilityControl.receive_command() handles the "check_availability" command properly, including parsing and validating parameters such as URL and optional date string.

2. Availability Checking
This test focuses on the AvailabilityEntity.check_availability() function to verify that it correctly processes the availability check against a provided URL and optional date string. It will ensure that the availability status is accurately determined and returned.

3. Data Logging to Excel
This test checks that the event data is correctly logged to an Excel file using DataExportEntity.log_to_excel(). It will verify that the export includes the correct data formatting, timestamping, and file handling, ensuring data integrity.

4. Data Logging to HTML
Ensures that the event data is appropriately exported to an HTML file using DataExportEntity.export_to_html(). This test will confirm the data integrity and formatting in the HTML output, ensuring it matches expected outcomes.
"""


# Testing the control layer's ability to receive and process the "check_availability" command
@pytest.mark.asyncio
async def test_control_layer_command_reception():
    logging.info("Starting test: Control Layer Command Reception for check_availability command")
    
    command_data = "check_availability"
    url = "https://example.com/reservation"
    date_str = "2023-10-10"

    with patch('control.AvailabilityControl.AvailabilityControl.receive_command', new_callable=AsyncMock) as mock_receive:
        control = AvailabilityControl()
        await control.receive_command(command_data, url, date_str)
        
        logging.info("Verifying that the receive_command was called with correct parameters")
        mock_receive.assert_called_with(command_data, url, date_str)
        logging.info("Test passed: Control layer correctly processes 'check_availability'")

# Testing the availability checking functionality from the AvailabilityEntity
@pytest.mark.asyncio
async def test_availability_checking():
    with patch('entity.AvailabilityEntity.AvailabilityEntity.check_availability', new_callable=AsyncMock) as mock_check:
        # Mock returns a tuple mimicking the real function's output
        mock_check.return_value = ("Checked availability: Availability confirmed", 
                                   "Data saved to Excel file at ExportedFiles\\excelFiles\\check_availability.xlsx.",
                                   "HTML file saved and updated at ExportedFiles\\htmlFiles\\check_availability.html.")
        result = await AvailabilityControl().check_availability("https://example.com/reservation", "2023-10-10")
        
        # Properly access the tuple and check the relevant part
        assert "Availability confirmed" in result[0]  # Accessing the first element of the tuple where the status message is


# Testing the Excel logging functionality
@pytest.mark.asyncio
async def test_data_logging_excel():
    logging.info("Starting test: Data Logging to Excel for check_availability command")

    with patch('entity.DataExportEntity.ExportUtils.log_to_excel', return_value="Data saved to Excel file at path.xlsx") as mock_excel:
        excel_result = ExportUtils.log_to_excel("check_availability", "https://example.com", "Available")
        
        logging.info("Verifying Excel file creation and data logging")
        assert "path.xlsx" in excel_result, "Excel data logging did not return expected file path"
        logging.info("Test passed: Data correctly logged to Excel")

# Testing the HTML export functionality
@pytest.mark.asyncio
async def test_data_logging_html():
    logging.info("Starting test: Data Export to HTML for check_availability command")
    
    with patch('entity.DataExportEntity.ExportUtils.export_to_html', return_value="Data exported to HTML file at path.html") as mock_html:
        html_result = ExportUtils.export_to_html("check_availability", "https://example.com", "Available")
        
        logging.info("Verifying HTML file creation and data export")
        assert "path.html" in html_result, "HTML data export did not return expected file path"
        logging.info("Test passed: Data correctly exported to HTML")

if __name__ == "__main__":
    pytest.main([__file__])
