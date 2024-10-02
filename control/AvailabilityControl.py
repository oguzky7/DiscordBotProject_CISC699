import asyncio
from entity.AvailabilityEntity import AvailabilityEntity
from datetime import datetime
from utils.css_selectors import Selectors
from utils.exportUtils import ExportUtils

class AvailabilityControl:
    def __init__(self):
        self.availability_entity = AvailabilityEntity()  # Initialize the entity
        self.is_monitoring = False  # Monitor state
        self.results = []  # List to store monitoring results

    async def receive_command(self, command_data, *args):
        """Handle all commands related to availability."""
        print("Data received from boundary:", command_data)

        if command_data == "check_availability":
            url = args[0]
            date_str = args[1] if len(args) > 1 else None
            return await self.check_availability(url, date_str)

        elif command_data == "start_monitoring_availability":
            url = args[0]
            date_str = args[1] if len(args) > 1 else None
            frequency = args[2] if len(args) > 2 and args[2] not in [None, ""] else 15
            return await self.start_monitoring_availability(url, date_str, frequency)

        elif command_data == "stop_monitoring_availability":
            return self.stop_monitoring_availability()

        else:
            print("Invalid command.")
            return "Invalid command."


    async def check_availability(self, url: str, date_str=None):
        """Handle availability check and export results."""
        print("Checking availability...")
        # Call the entity to check availability
        try:
            if not url:
                selectors = Selectors.get_selectors_for_url("opentable")
                url = selectors.get('availableUrl')
                if not url:
                    return "No URL provided, and default URL for openTable could not be found."
                print("URL not provided, default URL for openTable is: " + url)
                
            availability_info = await self.availability_entity.check_availability(url, date_str)

        # Prepare the result
            result = f"Checked availability: {availability_info}"
        except Exception as e:
            result = f"Failed to check availability: {str(e)}"
        print(result)

        # Create a DTO (Data Transfer Object) for export
        data_dto = {
            "command": "check_availability",
            "url": url,
            "result": result,
            "entered_date": datetime.now().strftime('%Y-%m-%d'),
            "entered_time": datetime.now().strftime('%H:%M:%S')
        }
        try:
            # Call the Excel export method from ExportUtils
            excelResult = ExportUtils.log_to_excel(data_dto)
            print(excelResult)
            htmlResult = ExportUtils.export_to_html(data_dto)
            print(htmlResult)

        except Exception as e:
            return f"AvailabilityControl_Error exporting data: {str(e)}"        
        return result, excelResult, htmlResult


    async def start_monitoring_availability(self, url: str, date_str=None, frequency=15):
        """Start monitoring availability at a specified frequency."""
        print("Monitoring availability")
        if self.is_monitoring:
            result = "Already monitoring availability."
            print(result)
            return result

        self.is_monitoring = True  # Set monitoring to active
        try:
            while self.is_monitoring:
                # Call entity to check availability
                result = await self.check_availability(url, date_str)
                self.results.append(result) # Store the result in the list
                await asyncio.sleep(frequency)  # Wait for the specified frequency before checking again

        except Exception as e:
            error_message = f"Failed to monitor availability: {str(e)}"
            print(error_message)
            return error_message

        return self.results


    def stop_monitoring_availability(self):
        """Stop monitoring availability."""
        print("Stopping availability monitoring...")
        result = None
        try:
            if not self.is_monitoring:
                # If no monitoring session is active
                result = "There was no active availability monitoring session. Nothing to stop."
            else:
                # Stop monitoring and collect results
                self.is_monitoring = False
                result = "Results for availability monitoring:\n"
                result += "\n".join(self.results)
                result = result + "\n" + "\nMonitoring stopped successfully!"
                print(result)
        except Exception as e:
            # Handle any error that occurs
            result = f"Error stopping availability monitoring: {str(e)}"
        
        return result

