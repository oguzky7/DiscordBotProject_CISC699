import pandas as pd
from datetime import datetime
import os

class ExcelInterface:

    def __init__(self):
        self.file_path = "BoundaryObjects/command_results.xlsx"
        self.initialize_excel()

    def initialize_excel(self):
        # Create a new Excel file with headers if it doesn't exist
        if not os.path.exists(self.file_path):
            df = pd.DataFrame(columns=["Timestamp", "Command", "URL", "Result"])
            df.to_excel(self.file_path, index=False)

    def log_result_to_excel(self, command, url, result):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        df = pd.read_excel(self.file_path)
        new_row = {"Timestamp": timestamp, "Command": command, "URL": url, "Result": result}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(self.file_path, index=False)
        return f"Result logged to Excel file ({self.file_path})."

    def log_and_save(self, command_name, url, result, browser_interface):
        # Log result to Excel
        excel_msg = self.log_result_to_excel(command_name, url, result)
        # Generate and save HTML
        html_msg = browser_interface.display_data_in_html([{
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'URL': url,
            'Result': result
        }], command_name)
        return excel_msg, html_msg
