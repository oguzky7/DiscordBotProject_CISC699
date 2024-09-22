import asyncio
from datetime import datetime
from entity.PriceEntity import PriceEntity
from utils.css_selectors import Selectors

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

        elif command_data == "monitor_price":
            url = args[0] if args else None
            frequency = args[1] if len(args) > 1 else 20
            return await self.start_monitoring_price(url, frequency)

        elif command_data == "stop_monitoring_price":
            return self.stop_monitoring()

        else:
            return "Invalid command."

    async def get_price(self, url: str):
        """Handle fetching the price from the entity."""
        try:
            if not url:
                selectors = Selectors.get_selectors_for_url("bestbuy")
                url = selectors.get('priceUrl')
                if not url:
                    return "No URL provided, and default URL for BestBuy could not be found."
                print("URL not provided, default URL for BestBuy is: " + url)

            # Fetch the price from the entity
            
                result = self.price_entity.get_price_from_page(url)
        except Exception as e:
            result = f"Failed to fetch price: {str(e)}"

        data_dto = {
                    "command": "monitor_price",
                    "url": url,
                    "result": result,
                    "entered_date": datetime.now().strftime('%Y-%m-%d'),
                    "entered_time": datetime.now().strftime('%H:%M:%S')
                }

                # Pass the DTO to PriceEntity to handle export
        self.price_entity.export_data(data_dto)
        return result


    async def start_monitoring_price(self, url: str = None, frequency=20):
        """Start monitoring the price at a given interval."""
        if self.is_monitoring:
            return "Already monitoring prices."
        
        self.is_monitoring = True
        previous_price = None

        try:
            while self.is_monitoring:
                # Fetch the current price
                if not url:
                    selectors = Selectors.get_selectors_for_url("bestbuy")
                    url = selectors.get('priceUrl')
                    if not url:
                        return "No URL provided, and default URL for BestBuy could not be found."
                    print("URL not provided, default URL for BestBuy is: " + url)

                current_price = self.price_entity.get_price_from_page(url)

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

                # Create a DTO (Data Transfer Object) for export
                data_dto = {
                    "command": "monitor_price",
                    "url": url,
                    "result": result,
                    "entered_date": datetime.now().strftime('%Y-%m-%d'),
                    "entered_time": datetime.now().strftime('%H:%M:%S')
                }

                # Pass the DTO to PriceEntity to handle export
                self.price_entity.export_data(data_dto)

                await asyncio.sleep(frequency)

        except Exception as e:
            self.results.append(f"Failed to monitor price: {str(e)}")


    def stop_monitoring(self):
        """Stop monitoring the price."""
        try:
            self.is_monitoring = False
            self.results
            result = "Monitoring stopped."
        except Exception as e:
            result = f"Failed to stop monitoring: {str(e)}"
        return result
