import os
import pandas as pd
from datetime import datetime

class ExcelInterface:

    def __init__(self):
        self.file_path = os.path.join(os.path.dirname(__file__), 'command_results.xlsx')
        if not os.path.exists(self.file_path):
            # Create a new Excel file with the headers
            df = pd.DataFrame(columns=['Timestamp', 'Command', 'URL', 'Result'])
            df.to_excel(self.file_path, index=False)

    def log_result_to_excel(self, command_name, url, result):
        # Load the existing Excel file
        df = pd.read_excel(self.file_path)
        
        # Create a new DataFrame with the new row
        new_row = pd.DataFrame([{
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'Command': command_name,
            'Result': result,
            'URL': url
        }])
        
        # Concatenate the new row with the existing DataFrame
        df = pd.concat([df, new_row], ignore_index=True)
        
        # Save the updated DataFrame back to the Excel file
        df.to_excel(self.file_path, index=False)

        print(f"Result logged to Excel file ({self.file_path}).")
