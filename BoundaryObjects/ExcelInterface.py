import pandas as pd
from datetime import datetime

class ExcelInterface:
    """
    Handles data extraction to and from Excel files.
    """

    def __init__(self, file_path):
        # Initialize with the file path where the Excel file will be saved
        self.__file_path = file_path

    def save_data_to_excel(self, data):
        # Save the data to an Excel file with additional details
        if data:
            df = pd.DataFrame(data)
            df['Timestamp'] = datetime.now()  # Add a timestamp column
            df.to_excel(self.__file_path, index=False)
            print(f"Data saved to {self.__file_path}")
        else:
            raise ValueError("Data must not be null.")

    def load_data_from_excel(self):
        # Load data from an Excel file
        try:
            data = pd.read_excel(self.__file_path).to_dict(orient="records")
            print(f"Data loaded from {self.__file_path}")
            return data
        except Exception as e:
            print(f"Failed to load data from Excel: {e}")
            return None
