import pandas as pd

class ExcelExportControl:
    """
    Manages the export of data to Excel files.
    """

    def __init__(self, file_path):
        # Initialize with the file path where the Excel file will be saved
        self.__file_path = file_path
        self.__users = []  # Placeholder for the list of users

    def export_to_excel(self, data):
        """
        Export the provided data to an Excel file.
        """
        if data:
            df = pd.DataFrame(data)
            df.to_excel(self.__file_path, index=False)
            print(f"Data exported to {self.__file_path}")
        else:
            raise ValueError("Data must not be null.")
