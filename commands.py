from browser_interface import BrowserInterface
from config import Config
import logger
import notification
import asyncio
from css_selectors import Selectors

# Initialize the browser interface
browser = BrowserInterface()

async def monitor_price(ctx, url, frequency=1):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('monitor_price', ctx.author)
            previous_price = None
            
            # Notify the user about the monitoring frequency
            await ctx.send(f"Monitoring price every {frequency} minute(s).")

            while True:
                current_price = browser.get_price(url)
                
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
                
                # Convert frequency to seconds
                await asyncio.sleep(frequency * 60)
        
        except Exception as e:
            logger.log_command_failed('monitor_price', e)
            await ctx.send(f"Failed to monitor price: {e}")
    else:
        logger.log_wrong_channel('monitor_price', ctx.author)
        await ctx.send("This command can only be used in the designated channel.")

def launch_browser(ctx, incognito=False):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('launch_browser', ctx.author)
            browser.launch_browser(incognito=incognito)
            return "Chrome browser launched successfully in incognito mode." if incognito else "Chrome browser launched successfully."
        except Exception as e:
            logger.log_command_failed('launch_browser', e)
            return f"Failed to launch browser: {e}"
    else:
        logger.log_wrong_channel('launch_browser', ctx.author)
        return "This command can only be used in the designated channel."

def navigate_to_url(ctx, url):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('navigate_to_url', ctx.author)
            browser.navigate_to_url(url)  
            return f"Navigated to URL: {url}"
        except Exception as e:
            logger.log_command_failed('navigate_to_url', e)
            return f"Failed to navigate: {e}"
    else:
        logger.log_wrong_channel('navigate_to_url', ctx.author)
        return "This command can only be used in the designated channel."

async def get_price(ctx, url):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('get_price', ctx.author)
            browser.navigate_to_url(url)
            price = browser.get_price(url)
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

def close_browser(ctx):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('close_browser', ctx.author)
            browser.close_browser()
            return "Browser closed successfully."
        except Exception as e:
            logger.log_command_failed('close_browser', e)
            return f"Failed to close browser: {e}"
    else:
        logger.log_wrong_channel('close_browser', ctx.author)
        return "This command can only be used in the designated channel."

