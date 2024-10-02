import asyncio
from datetime import datetime
from entity.PriceEntity import PriceEntity
from utils.configuration import load_config
from utils.css_selectors import Selectors
from utils.exportUtils import ExportUtils

class PriceControl:
    def __init__(self):
        self.price_entity = PriceEntity()  # Initialize PriceEntity for fetching and export
        self.is_monitoring = False  # Monitoring flag
        self.results = []  # Store monitoring results


    async def receive_command(self, command_data, *args):
        """Handle all price-related commands and process business logic."""
        print("Data received from boundary:", command_data)

        if command_data == "get_price":
            url = args[0] if args else None
            return await self.get_price(url)

        elif command_data == "start_monitoring_price":
            config = load_config()
            price_monitor_frequency = config.get('project_options', {}).get('price_monitor_frequency', 15)
            url = args[0] if args else None
            frequency = args[1] if len(args) > 1 and args[1] not in [None, ""] else price_monitor_frequency
            return await self.start_monitoring_price(url, frequency)

        elif command_data == "stop_monitoring_price":
            return self.stop_monitoring_price()

        else:
            return "Invalid command."


    async def get_price(self, url: str):
        """Handle fetching the price from the entity."""
        print("getting price...")
        try:
            if not url:
                selectors = Selectors.get_selectors_for_url("bestbuy")
                url = selectors.get('priceUrl')
                if not url:
                    return "No URL provided, and default URL for BestBuy could not be found."
                print("URL not provided, default URL for BestBuy is: " + url)

            # Fetch the price from the entity
            
            result = self.price_entity.get_price_from_page(url)
            print(f"Price found: {result}")
        except Exception as e:
            return f"Failed to fetch price: {str(e)}"
            
        try:
            # Call the Excel export method from ExportUtils
            excelResult = ExportUtils.log_to_excel(
                command="check_availability",
                url=url,
                result=result,
                entered_date=datetime.now().strftime('%Y-%m-%d'),  # Pass the optional entered_date
                entered_time=datetime.now().strftime('%H:%M:%S')   # Pass the optional entered_time
            )
            print(excelResult)
            htmlResult = ExportUtils.export_to_html(
                command="check_availability",
                url=url,
                result=result,
                entered_date=datetime.now().strftime('%Y-%m-%d'),  # Pass the optional entered_date
                entered_time=datetime.now().strftime('%H:%M:%S')   # Pass the optional entered_time
            )
            print(htmlResult)

        except Exception as e:
            return f"PriceControl_Error exporting data: {str(e)}"   
             
        return result, excelResult, htmlResult


    async def start_monitoring_price(self, url: str, frequency=10):
        """Start monitoring the price at a given interval."""
        print("Starting price monitoring...")
        try:
            if self.is_monitoring:
                return "Already monitoring prices."
            
            self.is_monitoring = True
            previous_price = None
        
            while self.is_monitoring:
                current_price = await self.get_price(url)
                # Determine price changes and prepare the result
                result = ""
                if current_price:
                    if previous_price is None:
                        result = f"Starting price monitoring. Current price: {current_price}"
                    elif current_price > previous_price:
                        result = f"Price went up! Current price: {current_price} (Previous: {previous_price})"
                    elif current_price < previous_price:
                        result = f"Price went down! Current price: {current_price} (Previous: {previous_price})"
                    else:
                        result = f"Price remains the same: {current_price}"
                    previous_price = current_price
                else:
                    result = "Failed to retrieve the price."

                # Add the result to the results list
                self.results.append(result)
                await asyncio.sleep(frequency)

        except Exception as e:
            self.results.append(f"Failed to monitor price: {str(e)}")


    def stop_monitoring_price(self):
        """Stop the price monitoring loop."""
        print("Stopping price monitoring...")
        result = None
        try:
            if not self.is_monitoring:
                # If no monitoring session is active
                result = "There was no active price monitoring session. Nothing to stop."
            else:
                # Stop monitoring and collect results
                self.is_monitoring = False
                result = "Results for price monitoring:\n"
                result += "\n".join(self.results)
                result = result + "\n" +"\nPrice monitoring stopped successfully!"
                print(result)
        except Exception as e:
            # Handle any error that occurs
            result = f"Error stopping price monitoring: {str(e)}"
        
        return result


