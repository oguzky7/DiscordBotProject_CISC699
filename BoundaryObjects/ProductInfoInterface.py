import sys
import os
import asyncio
import time
from CISC699 import logger
from CISC699.config import Config
from CISC699 import notification
from CISC699.css_selectors import Selectors
from BrowserInterface import BrowserInterface
from selenium.webdriver.common.by import By

# Initialize global objects
monitoring_stop_event = asyncio.Event()
browser = BrowserInterface()

class ProductInfoInterface:

    async def monitor_price(ctx, url, frequency=1):
        if ctx.channel.id == Config.CHANNEL_ID:
            try:
                logger.log_command_execution('monitor_price', ctx.author)
                previous_price = None

                await ctx.send(f"Monitoring price every {frequency} minute(s).")

                while not monitoring_stop_event.is_set():
                    current_price = ProductInfoInterface.get_price(url)

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

                    await asyncio.sleep(frequency * 60)

            except Exception as e:
                logger.log_command_failed('monitor_price', e)
                await ctx.send(f"Failed to monitor price: {e}")
        else:
            logger.log_wrong_channel('monitor_price', ctx.author)
            await ctx.send("This command can only be used in the designated channel.")

    async def get_price(ctx, url):
        if ctx.channel.id == Config.CHANNEL_ID:
            try:
                logger.log_command_execution('get_price', ctx.author)
                browser.navigate_to_url(url)

                selectors = Selectors.get_selectors_for_url(url)
                if not selectors:
                    raise ValueError(f"No selectors found for URL: {url}")

                time.sleep(2)  # Wait for the page to load

                try:
                    price_element = browser.driver.find_element(By.CSS_SELECTOR, selectors['price'])
                    price = price_element.text
                    print(f"Price found: {price}")
                except Exception as e:
                    print(f"Error finding price: {e}")
                    price = None

                if price:
                    await notification.Notification(ctx.author).notify_price_change(ctx.channel, price)
                else:
                    await ctx.send("Failed to retrieve the price.")
            except Exception as e:
                logger.log_command_failed('get_price', e)
                await ctx.send(f"Failed to get price: {e}")
        else:
            logger.log_wrong_channel('get_price', ctx.author)
            await ctx.send("This command can only be used in the designated channel.")
