from utils.export_utils import ExportUtils
from entity.AvailabilityEntity import AvailabilityEntity  # Fixing this import
from datetime import datetime  # Importing datetime module

class AvailabilityControl:
    def __init__(self):
        self.availability_entity = AvailabilityEntity()  # Initialize the entity

    async def handle_availability_check(self, ctx, url, date_str=None, time_slot=None, command_name="NameNotProvided"):
        # Perform availability check by calling the entity
        availability_info = await self.availability_entity.check_availability(ctx, url, date_str, time_slot)

        # Get the current timestamp
        current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # If date and time were entered, populate them; otherwise, use current timestamp
        entered_date = date_str if date_str else datetime.now().strftime('%Y-%m-%d')
        entered_time = time_slot if time_slot else datetime.now().strftime('%H:%M:%S')

        # Log results to HTML and Excel
        data = [{'Timestamp': current_timestamp, 'Command': command_name, 'URL': url, 
                 'Result': availability_info, 'Entered Date': entered_date, 'Entered Time': entered_time}]
        
        html_msg = ""
        excel_msg = ""

        try:
            html_msg = ExportUtils.export_to_html(data, command_name)
        except Exception as e:
            html_msg = f"Failed to export to HTML: {str(e)}"

        try:
            excel_msg = ExportUtils.log_to_excel(command_name, url, availability_info)
        except Exception as e:
            excel_msg = f"Failed to export to Excel: {str(e)}"
        
        # Return availability info and export results
        return availability_info, html_msg, excel_msg
