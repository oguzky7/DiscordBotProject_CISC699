import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.exportUtils import ExportUtils
from datetime import datetime

def test_excel_creation():
    # Mock data that simulates the data received from a website
    mock_command = "check_availability"
    mock_url = "MOCKURL_https://www.opentable.com/r/bar-spero-washington/"
    mock_result = "MOCK_No availability for the selected date."
    mock_entered_date = datetime.now().strftime('%Y-%m-%d')
    mock_entered_time = datetime.now().strftime('%H:%M:%S')
    
    # Log data to Excel
    result_message = ExportUtils.log_to_excel(
        command=mock_command,
        url=mock_url,
        result=mock_result,
        entered_date=mock_entered_date,
        entered_time=mock_entered_time
    )
    
    # Output the result of the Excel file creation
    print(result_message)

if __name__ == "__main__":
    test_excel_creation()
