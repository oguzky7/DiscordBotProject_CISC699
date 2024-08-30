import os
from datetime import datetime

class HTMLUtils:
    @staticmethod
    def save_data_to_html(data, command_name):
        # Use a timestamp to create a unique filename
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"{command_name}_{timestamp}.html"
        file_path = os.path.join("BoundaryObjects", "htmlFiles", file_name)

        # Create an HTML page to display the data
        html_content = "<html><head><title>Command Data</title></head><body>"
        html_content += f"<h1>Results for {command_name}</h1><table border='1'>"
        html_content += "<tr><th>Timestamp</th><th>URL</th><th>Result</th></tr>"

        for row in data:
            html_content += f"<tr><td>{row['Timestamp']}</td><td>{row['URL']}</td><td>{row['Result']}</td></tr>"

        html_content += "</table></body></html>"

        # Save the HTML content to a file
        with open(file_path, "w") as file:
            file.write(html_content)

        return f"HTML file saved as {file_path}."
