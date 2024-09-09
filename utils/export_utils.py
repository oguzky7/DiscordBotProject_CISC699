import os
import pandas as pd
from datetime import datetime

class ExportUtils:

    @staticmethod
    def log_to_excel(command, url, result, entered_date=None, entered_time=None):
        # Determine the file path for the Excel file
        file_name = f"{command}.xlsx"
        file_path = os.path.join("ExportedFiles", "excelFiles", file_name)
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Timestamp for current run
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # If date/time not entered, use current timestamp
        entered_date = entered_date or datetime.now().strftime('%Y-%m-%d')
        entered_time = entered_time or datetime.now().strftime('%H:%M:%S')

        # Check if the file exists and create the structure if it doesn't
        if not os.path.exists(file_path):
            df = pd.DataFrame(columns=["Timestamp", "Command", "URL", "Result", "Entered Date", "Entered Time"])
            df.to_excel(file_path, index=False)

        # Load existing data from the Excel file
        df = pd.read_excel(file_path)

        # Append the new row
        new_row = {
            "Timestamp": timestamp,
            "Command": command,
            "URL": url,
            "Result": result,
            "Entered Date": entered_date,
            "Entered Time": entered_time
        }

        # Add the new row to the existing data and save it back to Excel
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_excel(file_path, index=False)

        return f"Data saved to Excel file ({file_path})."



    @staticmethod
    def export_to_html(data, command_name):
        # Define file path for HTML
        file_name = f"{command_name}.html"  # Only one HTML file per command, will be appended
        file_path = os.path.join("ExportedFiles", "htmlFiles", file_name)
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Debug: Print data being passed to HTML
        print(f"Data being exported to HTML: {data}")

        # Check if the file already exists and append rows
        if os.path.exists(file_path):
            # Open the file and append rows
            with open(file_path, "r+", encoding="utf-8") as file:
                content = file.read()
                # Look for the closing </table> tag and append new rows before it
                if "</table>" in content:
                    new_rows = ""
                    for row in data:
                        # Ensure all necessary keys are in the row dictionary
                        new_rows += f"<tr><td>{row.get('Timestamp', 'N/A')}</td><td>{row.get('Command', 'N/A')}</td><td>{row.get('URL', 'N/A')}</td><td>{row.get('Result', 'N/A')}</td><td>{row.get('Entered Date', 'N/A')}</td><td>{row.get('Entered Time', 'N/A')}</td></tr>\n"
                    
                    # Insert new rows before </table>
                    content = content.replace("</table>", new_rows + "</table>")
                    file.seek(0)  # Move pointer to the start
                    file.write(content)
                    file.truncate()  # Truncate any remaining content
                    file.flush()  # Flush the buffer to ensure it's written
                    print(f"Appended new rows to existing HTML file at {file_path}.")
        else:
            # If the file doesn't exist, create a new one with table headers
            with open(file_path, "w", encoding="utf-8") as file:
                html_content = "<html><head><title>Command Data</title></head><body>"
                html_content += f"<h1>Results for {command_name}</h1><table border='1'>"
                html_content += "<tr><th>Timestamp</th><th>Command</th><th>URL</th><th>Result</th><th>Entered Date</th><th>Entered Time</th></tr>"
                for row in data:
                    # Ensure all necessary keys are in the row dictionary
                    html_content += f"<tr><td>{row.get('Timestamp', 'N/A')}</td><td>{row.get('Command', 'N/A')}</td><td>{row.get('URL', 'N/A')}</td><td>{row.get('Result', 'N/A')}</td><td>{row.get('Entered Date', 'N/A')}</td><td>{row.get('Entered Time', 'N/A')}</td></tr>\n"
                html_content += "</table></body></html>"
                file.write(html_content)
                file.flush()  # Ensure content is written to disk
                print(f"Created new HTML file at {file_path}.")

        return f"HTML file saved and updated at {file_path}."