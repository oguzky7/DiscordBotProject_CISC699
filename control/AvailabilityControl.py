from utils.export_utils import ExportUtils

class AvailabilityControl:
    async def handle_availability_check(self, ctx, url, date_str=None, time_slot=None):
        # Perform availability check (call the entity)
        availability_info = await self.entity.check_availability(ctx, url, date_str, time_slot)

        # Example of logging results to HTML and Excel
        data = [{'Timestamp': '2024-09-09', 'URL': url, 'Result': availability_info}]
        html_msg = ExportUtils.export_to_html(data, "check_availability")
        excel_msg = ExportUtils.log_to_excel("check_availability", url, availability_info)
        
        # Return availability info and export results
        return availability_info, html_msg, excel_msg
