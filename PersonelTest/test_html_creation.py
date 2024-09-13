import sys, os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from DataObjects.DataExportDTO import DataExportDTO  # Importing the DTO
from utils.exportUtils import ExportUtils

def test_html_creation():
    # Mock data that simulates the data received from a website
    mock_command = "MOCK_check_availability"
    mock_url = "MOCK_https://www.opentable.com/r/bar-spero-washington/"
    mock_result = "No availability for the selected date."
    
    # Get the current date and time
    mock_entered_date = datetime.now().strftime('%Y-%m-%d')
    mock_entered_time = datetime.now().strftime('%H:%M:%S')

    # Create DTO object
    data_dto = DataExportDTO(
        command=mock_command,
        url=mock_url,
        result=mock_result,
        entered_date=mock_entered_date,
        entered_time=mock_entered_time
    )

    # Validate the DTO
    try:
        data_dto.validate()
    except ValueError as ve:
        print(f"Validation Error: {ve}")
        return

    # Prepare the data for HTML export
    mock_data = [data_dto.to_dict()]
    
    # Export data to HTML using the DTO
    result_message = ExportUtils.export_to_html(
        data=mock_data,
        command_name=data_dto.command
    )
    
    # Output the result of the HTML file creation
    print(result_message)

if __name__ == "__main__":
    test_html_creation()
