from entity.AvailabilityEntity import AvailabilityEntity
from datetime import datetime

class CheckAvailabilityControl:
    def __init__(self, browser_entity):
        self.availability_entity = AvailabilityEntity(browser_entity)  # Initialize entity

    async def check_availability(self, url: str, date_str=None):
        """Handle the availability check and pass results for export."""
        # Get availability info from the entity layer
        availability_info = await self.availability_entity.check_availability(url, date_str)

        # Get current timestamp
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Use current date/time if not provided
        entered_date = date_str if date_str else datetime.now().strftime('%Y-%m-%d')
        entered_time = datetime.now().strftime('%H:%M:%S')

        # Export results to HTML and Excel
        data_dto = {
            "command": "check_availability",
            "url": url,
            "result": availability_info,
            "entered_date": entered_date,
            "entered_time": entered_time
        }

        # Call the export methods from the entity layer
        html_msg = self.availability_entity.export_to_html(data_dto)
        excel_msg = self.availability_entity.export_to_excel(data_dto)

        # Return the availability result, along with HTML and Excel export messages
        return availability_info, html_msg, excel_msg
