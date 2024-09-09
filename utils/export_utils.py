import os
import pandas as pd
from datetime import datetime

class ExportUtils:
    
    @staticmethod
    def export_to_html(data, command_name):
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"{command_name}_{timestamp}.html"
        file_path = os.path.join("BoundaryObjects", "htmlFiles", file_name)

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
    def log_to_excel(command, url, result):
        file_path = "BoundaryObjects/command_results.xlsx"
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Initialize Excel file if it doesn't exist
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=["Timestamp", "Command", "URL", "Result"])
            df.to_excel(file_path, index=False)
        
        # Append new data
        df = pd.read_excel(file_path)
        new_row = {"Timestamp": timestamp, "Command": command, "URL": url, "Result": result}
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(file_path, index=False)

        return f"Data saved to Excel file ({file_path})."
