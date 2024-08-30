import pandas as pd
from datetime import datetime

class ExcelUtils:
    @staticmethod
    def save_data_to_excel(data, command_name):
        # Convert the data to a DataFrame
        df = pd.DataFrame(data)

        # Use a timestamp to create a unique filename
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        file_name = f"{command_name}_{timestamp}.xlsx"

        # Save the DataFrame to an Excel file
        file_path = f"BoundaryObjects/{file_name}"
        df.to_excel(file_path, index=False)

        return f"Excel file saved as {file_path}."
