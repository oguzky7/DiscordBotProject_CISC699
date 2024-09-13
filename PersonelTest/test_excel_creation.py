import sys, os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.exportUtils import ExportUtils
from DataObjects.DataExportDTO import DataExportDTO  # Importing the DTO

def test_excel_creation():
    # Mock data that simulates the data received from a website
    mock_command = "MOCK_check_availability"
    mock_url = "MOCKURL_https://www.opentable.com/r/bar-spero-washington/"
    mock_result = "MOCK_No availability for the selected date."
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

    # Log data to Excel using the DTO
    result_message = ExportUtils.log_to_excel(
        command=data_dto.command,
        url=data_dto.url,
        result=data_dto.result,
        entered_date=data_dto.entered_date,
        entered_time=data_dto.entered_time
    )
    
    # Output the result of the Excel file creation
    print(result_message)

if __name__ == "__main__":
    test_excel_creation()
