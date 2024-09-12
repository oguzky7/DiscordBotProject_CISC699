from utils.exportUtils import ExportUtils
from datetime import datetime

class DataExportDTO:
    def __init__(self):
        # Any initialization logic can be placed here (if needed)
        pass

    def save_data(self, command_name, url, result, entered_date=None, entered_time=None):
        """
        Save the data related to availability or price to both Excel and HTML.
        
        Parameters:
        - command_name: The name of the command (e.g., 'check_availability' or 'get_price').
        - url: The URL of the product or service.
        - result: The result of the operation (e.g., the price or availability status).
        - entered_date: The date entered by the user (or default).
        - entered_time: The time entered by the user (or default).
        """
        # Get the current timestamp
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # If date/time not provided, use current timestamp
        entered_date = entered_date or datetime.now().strftime('%Y-%m-%d')
        entered_time = entered_time or datetime.now().strftime('%H:%M:%S')

        # Prepare data for export
        data = [{
            "Timestamp": current_timestamp,
            "Command": command_name,
            "URL": url,
            "Result": result,
            "Entered Date": entered_date,
            "Entered Time": entered_time
        }]

        # Save to Excel
        try:
            excel_msg = ExportUtils.log_to_excel(command_name, url, result, entered_date, entered_time)
            print(excel_msg)
        except Exception as e:
            print(f"Failed to save data to Excel: {e}")

        # Save to HTML
        try:
            html_msg = ExportUtils.export_to_html(data, command_name)
            print(html_msg)
        except Exception as e:
            print(f"Failed to save data to HTML: {e}")
