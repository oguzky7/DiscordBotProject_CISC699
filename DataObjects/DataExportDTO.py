class DataExportDTO:
    def __init__(self, command, url, result, entered_date=None, entered_time=None):
        self.command = command
        self.url = url
        self.result = result
        self.entered_date = entered_date
        self.entered_time = entered_time

    def validate(self):
        """Perform simple validation on the input data."""
        if not self.command or not self.url or not self.result:
            raise ValueError("Command, URL, and Result must all be provided.")
        return True  # If validation passes

    def to_dict(self):
        """Convert the DTO to a dictionary for export utilities like Excel or HTML generation."""
        return {
            "Command": self.command,
            "URL": self.url,
            "Result": self.result,
            "Entered Date": self.entered_date or "N/A",
            "Entered Time": self.entered_time or "N/A"
        }
