import asyncio
from entity.AvailabilityEntity import AvailabilityEntity
from datetime import datetime

class MonitorAvailabilityControl:
    def __init__(self, browser_entity):
        self.availability_entity = AvailabilityEntity(browser_entity)  # Reuse check control logic
        self.is_monitoring = False  # Store the running task
        self.results = [] 

    async def start_monitoring_availability(self, ctx, url: str, date_str=None, frequency=15):
        """Start monitoring availability at the given frequency."""
        if self.is_monitoring:
            return "Already monitoring prices."
        self.is_monitoring = True  # Set monitoring state to true
        try:
            while self.is_monitoring:
                availability_info  = await self.availability_entity.check_availability(ctx, url, date_str)

                # Prepare the result message
                result = f"Checked availability: {availability_info}"

                # Append the result to the results list
                self.results.append(result)

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

                # Sleep for the specified frequency before the next check
                await asyncio.sleep(frequency)

        except Exception as e:
            self.results.append(f"Failed to monitor availability: {str(e)}")
            return f"Error: {str(e)}"
        return self.results

    def stop_monitoring(self):
        """Stop the availability monitoring loop."""
        self.is_monitoring = False  # Set monitoring state to false
        # Return all the results collected during the monitoring period
        return self.results if self.results else ["No data collected."]