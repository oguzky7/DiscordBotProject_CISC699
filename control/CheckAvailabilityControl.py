from entity.AvailabilityEntity import AvailabilityEntity
from datetime import datetime

class CheckAvailabilityControl:
    def __init__(self, browser_entity):
        self.availability_entity = AvailabilityEntity(browser_entity)  # Initialize entity

    async def check_availability(self, url: str, date_str=None):
        """Handle the availability check and pass results for export."""
        # Get availability info from the entity layer
        availability_info = await self.availability_entity.check_availability(url, date_str)
        # Prepare the result message
        result = f"Checked availability: {availability_info}"

        # Create a DTO (Data Transfer Object) to organize the data for export
        data_dto = {
            "command": "start_monitoring_availability",  # Command executed
            "url": url,  # URL of the availability being monitored
            "result": result,  # Result of the availability check
            "entered_date": datetime.now().strftime('%Y-%m-%d'),  # Current date
            "entered_time": datetime.now().strftime('%H:%M:%S')  # Current time
        }

        # Pass the DTO to AvailabilityEntity to handle export to Excel and HTML
        self.availability_entity.export_data(data_dto)
        return result