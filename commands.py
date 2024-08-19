import time
import asyncio
from browser_interface import BrowserInterface
from config import Config
import logger
from notification import Notification

browser = BrowserInterface()
last_price = None

async def launch_browser(ctx, incognito=False):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('launch_browser', ctx.author)
            browser.launch_browser(incognito=incognito)
            await Notification(ctx.author).send_message(ctx.channel, "Chrome browser launched successfully in incognito mode." if incognito else "Chrome browser launched successfully.")
        except Exception as e:
            logger.log_command_failed('launch_browser', e)
            await Notification(ctx.author).send_error_message(ctx.channel, e)
    else:
        logger.log_wrong_channel('launch_browser', ctx.author)
        await Notification(ctx.author).send_message(ctx.channel, "This command can only be used in the designated channel.")

async def navigate_to_url(ctx, url):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('navigate_to_url', ctx.author)
            if not browser.driver:  # Automatically launch the browser if it's not running
                browser.launch_browser()
            browser.navigate_to_url(url)
            await Notification(ctx.author).send_message(ctx.channel, f"Navigated to URL: {url}")
        except Exception as e:
            logger.log_command_failed('navigate_to_url', e)
            await Notification(ctx.author).send_error_message(ctx.channel, e)
    else:
        logger.log_wrong_channel('navigate_to_url', ctx.author)
        await Notification(ctx.author).send_message(ctx.channel, "This command can only be used in the designated channel.")

async def get_price(ctx, url):
    global last_price
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('get_price', ctx.author)
            if not browser.driver:  # Automatically launch the browser if it's not running
                browser.launch_browser()
            browser.navigate_to_url(url)
            price = browser.get_price(url)
            if price != last_price:
                last_price = price
                await Notification(ctx.author).send_message(ctx.channel, f"The price is: {price}. The price has changed!" if price else "Failed to retrieve the price.")
            else:
                await Notification(ctx.author).send_message(ctx.channel, f"The price is: {price}. No price change detected.")
        except Exception as e:
            logger.log_command_failed('get_price', e)
            await Notification(ctx.author).send_error_message(ctx.channel, e)
    else:
        logger.log_wrong_channel('get_price', ctx.author)
        await Notification(ctx.author).send_message(ctx.channel, "This command can only be used in the designated channel.")

async def login(ctx, url, username, password):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('login', ctx.author)
            if not browser.driver:  # Automatically launch the browser if it's not running
                browser.launch_browser()
            browser.login(url, username, password)
            await Notification(ctx.author).send_message(ctx.channel, f"Logged in to {url} with username: {username}")
        except Exception as e:
            logger.log_command_failed('login', e)
            await Notification(ctx.author).send_error_message(ctx.channel, e)
    else:
        logger.log_wrong_channel('login', ctx.author)
        await Notification(ctx.author).send_message(ctx.channel, "This command can only be used in the designated channel.")

async def close_browser(ctx):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('close_browser', ctx.author)
            browser.close_browser()
            await Notification(ctx.author).send_message(ctx.channel, "Browser closed successfully.")
        except Exception as e:
            logger.log_command_failed('close_browser', e)
            await Notification(ctx.author).send_error_message(ctx.channel, e)
    else:
        logger.log_wrong_channel('close_browser', ctx.author)
        await Notification(ctx.author).send_message(ctx.channel, "This command can only be used in the designated channel.")

async def monitor_price(ctx, url):
    while True:
        response = await get_price(ctx, url)
        await Notification(ctx.author).send_message(ctx.channel, response)
        await asyncio.sleep(600)  # Wait for 10 minutes before checking the price again
