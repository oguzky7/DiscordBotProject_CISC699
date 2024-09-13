import asyncio
from datetime import datetime
from entity.PriceEntity import PriceEntity
from utils.css_selectors import Selectors 

class MonitorPriceControl:
    """MonitorPriceControl handles the business logic of monitoring the price over time 
    and instructs PriceEntity to fetch prices and export data."""
    
    def __init__(self, browser_entity):
        self.price_entity = PriceEntity(browser_entity)  # Initialize PriceEntity for data fetching and export
        self.is_monitoring = False  # Control flag for monitoring state
        self.results = []  # List to store results during monitoring

    async def start_monitoring_price(self, ctx, url: str = None, frequency=20):
        """Start monitoring the price at a given interval and provide updates to the user via Discord.

        ctx: Context from Discord command.
        url: URL of the product page to monitor.
        frequency: Time interval (in seconds) between price checks.
        """
        if self.is_monitoring:
            return "Already monitoring prices."
        self.is_monitoring = True  # Set monitoring state to true
        previous_price = None  # Track the last price fetched

        try:
            while self.is_monitoring:
                # Fetch the current price from PriceEntity
                if not url:
                    selectors = Selectors.get_selectors_for_url("bestbuy")
                    url = selectors.get('priceUrl')  # Get the price URL
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

                # Create a DTO (Data Transfer Object) to organize the data for export
                data_dto = {
                    "command": "start_monitoring_price",  # Command executed
                    "url": url,  # URL of the product being monitored
                    "result": result,  # Result of the price check
                    "entered_date": datetime.now().strftime('%Y-%m-%d'),  # Current date
                    "entered_time": datetime.now().strftime('%H:%M:%S')  # Current time
                }
                
                # Pass the DTO to PriceEntity to handle export to Excel and HTML
                self.price_entity.export_data(data_dto)

                await asyncio.sleep(frequency)  # Wait for the next check based on frequency

        except Exception as e:
            self.results.append(f"Failed to monitor price: {str(e)}")

    def stop_monitoring(self):
        """Stop the price monitoring loop."""
        self.is_monitoring = False  # Set monitoring state to false
        # Return the full list of results gathered during monitoring
        return self.results if self.results else ["No data collected."]
