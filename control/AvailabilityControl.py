from utils.export_utils import ExportUtils
from entity.AvailabilityEntity import AvailabilityEntity  # Fixing this import
from datetime import datetime  # Importing datetime module

class AvailabilityControl:
    def __init__(self):
        self.availability_entity = AvailabilityEntity()  # Initialize the entity

    async def handle_availability_check(self, ctx, url, date_str=None, time_slot=None):
        # Perform availability check by calling the entity
        availability_info = await self.availability_entity.check_availability(ctx, url, date_str, time_slot)

        # Get the current timestamp
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Log results to HTML and Excel
        data = [{'Timestamp': current_timestamp, 'URL': url, 'Result': availability_info}]
        
        try:
            html_msg = ExportUtils.export_to_html(data, "check_availability")
        except Exception as e:
            html_msg = f"Failed to export to HTML: {str(e)}"

        try:
            excel_msg = ExportUtils.log_to_excel("check_availability", url, availability_info)
        except Exception as e:
            excel_msg = f"Failed to export to Excel: {str(e)}"
        
        # Return availability info and export results
        return availability_info, html_msg, excel_msg
