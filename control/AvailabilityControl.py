import asyncio
from entity.AvailabilityEntity import AvailabilityEntity
from datetime import datetime

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

        elif command_data == "monitor_availability":
            print(f"Monitoring availability at {url} every {frequency} second(s).")
            url = args[0]
            date_str = args[1] if len(args) > 1 else None
            frequency = args[2] if len(args) > 2 else 15
            return await self.start_monitoring_availability(url, date_str, frequency)

        elif command_data == "stop_monitoring_availability":
            return self.stop_monitoring()

        else:
            return "Invalid command."


    async def check_availability(self, url: str, date_str=None):
        """Handle availability check and export results."""
        # Call the entity to check availability
        availability_info = await self.availability_entity.check_availability(url, date_str)

        # Prepare the result
        try:
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

        # Export data to Excel/HTML via the entity
        self.availability_entity.export_data(data_dto)
        return result


    async def start_monitoring_availability(self, url: str, date_str=None, frequency=15):
        """Start monitoring availability at a specified frequency."""
        if self.is_monitoring:
            result = "Already monitoring availability."
            print(result)
            return result

        self.is_monitoring = True  # Set monitoring to active
        try:
            while self.is_monitoring:
                # Call entity to check availability
                availability_info = await self.availability_entity.check_availability(url, date_str)

                # Prepare and log the result
                result = f"Checked availability: {availability_info}"
                print(result)
                self.results.append(result)

                # Create a DTO (Data Transfer Object) for export
                data_dto = {
                    "command": "start_monitoring_availability",
                    "url": url,
                    "result": result,
                    "entered_date": datetime.now().strftime('%Y-%m-%d'),
                    "entered_time": datetime.now().strftime('%H:%M:%S')
                }

                # Export data to Excel/HTML via the entity
                self.availability_entity.export_data(data_dto)

                # Wait for the specified frequency before checking again
                await asyncio.sleep(frequency)

        except Exception as e:
            error_message = f"Failed to monitor availability: {str(e)}"
            print(error_message)
            self.results.append(error_message)
            return error_message

        return self.results


    def stop_monitoring_availability(self):
        """Stop monitoring availability."""
        self.is_monitoring = False  # Set monitoring to inactive
            
        try:
            result = "Monitoring stopped. Collected results:" if self.results else "No data collected."
        except Exception as e:
            result = f"Failed to stop monitoring: {str(e)}"
        print(result)
        return self.results if self.results else [result]
