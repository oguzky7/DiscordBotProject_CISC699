import sys, os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.exportUtils import ExportUtils

def test_html_creation():
    # Mock data that simulates the data received from a website
    mock_command = "MOCK_check_availability"
    mock_url = "MOCK_https://www.opentable.com/r/bar-spero-washington/"
    mock_result = "No availability for the selected date."
    
    # Get the current date and time
    mock_entered_date = datetime.now().strftime('%Y-%m-%d')
    mock_entered_time = datetime.now().strftime('%H:%M:%S')

    # Prepare the data as a list of dictionaries for HTML export
    mock_data = [{
        "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "Command": mock_command,
        "URL": mock_url,
        "Result": mock_result,
        "Entered Date": mock_entered_date,
        "Entered Time": mock_entered_time
    }]
    
    # Export data to HTML
    result_message = ExportUtils.export_to_html(
        data=mock_data,
        command_name=mock_command
    )
    
    # Output the result of the HTML file creation
    print(result_message)

if __name__ == "__main__":
    test_html_creation()
