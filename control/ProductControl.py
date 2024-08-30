from entity.ProductEntity import ProductEntity
from control.BrowserControl import BrowserControl
from selenium.webdriver.common.by import By
from utils.ExcelUtils import ExcelUtils
from utils.HTMLUtils import HTMLUtils
import asyncio
from Config import Config

class ProductControl:
    def __init__(self):
        self.product_entity = ProductEntity()
        self.browser_control = BrowserControl()

    async def get_price(self, url):
        # Launch and navigate using the browser control
        self.browser_control.launch_browser()
        self.browser_control.navigate_to_url(url)

        # Now use the browser to interact with the web page
        price_element = self.browser_control.driver.find_element(By.CSS_SELECTOR, "CSS_SELECTOR_FOR_PRICE")
        price = price_element.text

        # Update the product entity with the new price
        self.product_entity.update_price(price)

        # Close the browser
        self.browser_control.close_browser()

        # Save the result to Excel and HTML
        ExcelUtils.save_data_to_excel([{
            'Timestamp': self.product_entity.get_timestamp(),
            'URL': url,
            'Result': price
        }], 'price_result')

        HTMLUtils.save_data_to_html([{
            'Timestamp': self.product_entity.get_timestamp(),
            'URL': url,
            'Result': price
        }], 'price_result')

        return price

    async def monitor_price(self, url, frequency=1):
        # Monitoring logic, calling get_price periodically
        pass


    async def monitor_price(self, ctx, url, frequency=1):
        global monitoring_stop_event
        if ctx.channel.id == Config.CHANNEL_ID:
            try:
                logger.log_command_execution('monitor_price', ctx.author)
                previous_price = None

                await ctx.send(f"Monitoring price every {frequency} minute(s).")
                while not monitoring_stop_event:
                    print("Monitoring loop started...")  # Debug print statement
                    await ctx.send("Monitoring loop started...")
                    current_price = await self.get_price(ctx, url)

                    if current_price:
                        if previous_price is None:
                            await ctx.send(f"Starting price monitoring. Current price is: {current_price}")
                        else:
                            if current_price > previous_price:
                                await ctx.send(f"Price went up! Current price: {current_price} (Previous: {previous_price})")
                            elif current_price < previous_price:
                                await ctx.send(f"Price went down! Current price: {current_price} (Previous: {previous_price})")
                            else:
                                await ctx.send(f"Price remains the same: {current_price}")

                        previous_price = current_price
                    else:
                        await ctx.send("Failed to retrieve the price.")

                    # Log and save the result after each check
                    excel_msg, html_msg = self.excel_interface.log_and_save('monitor_price', url, current_price, self.browser_interface)
                    await ctx.send(excel_msg)
                    await ctx.send(html_msg)

                    await asyncio.sleep(frequency * 60)
                await ctx.send("Monitoring loop stopped...")
                print("Monitoring loop stopped...")  # Debug print statement
                
                monitoring_stop_event = False  # Reset the flag for future monitoring
            except Exception as e:
                logger.log_command_failed('monitor_price', e)
                await ctx.send(f"Failed to monitor price: {e}")
        else:
            logger.log_wrong_channel('monitor_price', ctx.author)
            await ctx.send("This command can only be used in the designated channel.")


    def stop_monitoring(self):
        # Logic to stop monitoring (this can be more complex based on your actual requirements)
        global monitoring_stop_event
        monitoring_stop_event = True
