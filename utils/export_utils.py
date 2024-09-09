import os
import pandas as pd
from datetime import datetime

class ExportUtils:
    
    @staticmethod
    def export_to_html(data, command_name):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"{command_name}_{timestamp}.html"
        file_path = os.path.join("ExportedFiles", "htmlFiles", file_name)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        html_content = "<html><head><title>Command Data</title></head><body>"
        html_content += f"<h1>Results for {command_name}</h1><table border='1'>"
        html_content += "<tr><th>Timestamp</th><th>URL</th><th>Result</th></tr>"

        for row in data:
            html_content += f"<tr><td>{row['Timestamp']}</td><td>{row['URL']}</td><td>{row['Result']}</td></tr>"
        
        html_content += "</table></body></html>"

        with open(file_path, "w") as file:
            file.write(html_content)

        return f"HTML file saved as {file_path}."

    @staticmethod
    def log_to_excel(command, url, result, entered_date=None, entered_time=None):
        # Determine the file path for the Excel file
        file_path = os.path.join("ExportedFiles", "excelFiles", "command_results.xlsx")
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Timestamp for current run
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # If date/time not entered, use current timestamp
        entered_date = entered_date or datetime.now().strftime('%Y-%m-%d')
        entered_time = entered_time or datetime.now().strftime('%H:%M:%S')

        # Check if the file exists and create the structure if it doesn't
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=["Timestamp", "Command", "URL", "Result", "Entered Date", "Entered Time", "Date Entered?", "Time Entered?"])
            df.to_excel(file_path, index=False)

        # Load existing data from the Excel file
        df = pd.read_excel(file_path)

        # Determine whether date and time were entered
        date_entered = "Yes" if entered_date else "No"
        time_entered = "Yes" if entered_time else "No"

        # Append the new row
        new_row = {
            "Timestamp": timestamp,
            "Command": command,
            "URL": url,
            "Result": result,
            "Entered Date": entered_date,
            "Entered Time": entered_time,
            "Date Entered?": date_entered,
            "Time Entered?": time_entered
        }

        # Add the new row to the existing data and save it back to Excel
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(file_path, index=False)

        return f"Data saved to Excel file ({file_path})."
