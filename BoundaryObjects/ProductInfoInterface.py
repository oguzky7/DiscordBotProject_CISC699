import asyncio
from CISC699 import logger
from CISC699.config import Config
from CISC699 import notification
from CISC699.css_selectors import Selectors
from selenium.webdriver.common.by import By
from ExcelInterface import ExcelInterface
from BrowserInterface import BrowserInterface

browser = BrowserInterface()
# Monitoring stop event flag
monitoring_stop_event = False

class ProductInfoInterface:

    def __init__(self):
        self.excel_interface = ExcelInterface()
        self.browser_interface = BrowserInterface()

    @staticmethod
    def stop_monitoring():
        global monitoring_stop_event
        monitoring_stop_event = True

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

    async def get_price(self, ctx, url):
        if ctx.channel.id == Config.CHANNEL_ID:
            try:
                logger.log_command_execution('get_price', ctx.author)
                browser.navigate_to_url(url)
                selectors = Selectors.get_selectors_for_url(url)
                if not selectors:
                    raise ValueError(f"No selectors found for URL: {url}")

                await asyncio.sleep(2)  # Wait for the page to load

                try:
                    price_element = browser.driver.find_element(By.CSS_SELECTOR, selectors['price'])
                    price = price_element.text
                    print(f"Price found: {price}")
                    await ctx.send(f"Price Found! Current price is: {price}")

                    # Log and save the result
                    excel_msg, html_msg = self.excel_interface.log_and_save('get_price', url, price, self.browser_interface)
                    await ctx.send(excel_msg)
                    await ctx.send(html_msg)

                    return price
                except Exception as e:
                    print(f"Error finding price: {e}")
                    await ctx.send(f"Failed to retrieve the price: {e}")
                    raise e
            except Exception as e:
                logger.log_command_failed('get_price', e)
                await ctx.send(f"Failed to get price: {e}")
            finally:
                # Optional: You may close the browser here if you want
                pass
        else:
            logger.log_wrong_channel('get_price', ctx.author)
            await ctx.send("This command can only be used in the designated channel.")
