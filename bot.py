import discord
from discord.ext import commands
import commands as cmd 
import help
import logger
from config import Config
from css_selectors import Selectors
from selenium.webdriver.common.by import By
import time
from browser_interface import BrowserInterface 
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

# Define the intents your bot will use
intents = discord.Intents.default()
intents.message_content = True  # This enables the bot to read message content

# Initialize the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)
browser = BrowserInterface()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages from the bot itself

    # Log the received message
    logger.log_message_received(message)
    
    # Let the user know the message is recognized
    if message.content.startswith('!'):
        await message.channel.send(f"Message recognized: {message.content}. Processing...")

        # Process the command
        recognized = True
        await bot.process_commands(message)
        logger.log_message_recognized()

        # After processing, confirm that the command was executed
        await message.channel.send(f"Command '{message.content}' has been executed successfully.")

    else:
        logger.log_message_not_recognized()
        await message.channel.send("Message not recognized as a command. Type `!commands` to see possible actions.")

@bot.command(name='launch_browser')
async def launch_browser(ctx, *args):
    incognito = "incognito" in args
    response = cmd.launch_browser(ctx, incognito=incognito)
    await ctx.send(response)

@bot.command(name='navigate_to_url')
async def navigate_to_url(ctx, url: str):
    response = cmd.navigate_to_url(ctx, url)
    await ctx.send(response)

@bot.command(name='get_price')
async def get_price(ctx, url: str):
    response = await cmd.get_price(ctx, url)
    # No need to send the response here, since it's handled within get_price

@bot.command(name='monitor_price')
async def monitor_price(ctx, url: str, frequency: int = 1):
    await cmd.monitor_price(ctx, url, frequency)  # Pass the frequency to the function

@bot.command(name='close_browser')
async def close_browser(ctx):
    response = cmd.close_browser(ctx)
    await ctx.send(response)

@bot.command(name='commands')
async def commands_command(ctx):
    await ctx.send(help.get_help_message())

@bot.command(name='stop')
async def stop_command(ctx):
    if ctx.channel.id == Config.CHANNEL_ID:
        await ctx.send("Stopping the bot. Goodbye!")
        await bot.close()  # Gracefully close the bot instead of using sys.exit()
    else:
        logger.log_wrong_channel('stop', ctx.author)
        await ctx.send("This command can only be used in the designated channel.")

@bot.command(name="check_availability")
async def check_availability(ctx, url: str, date_str: str):
    """
    Checks availability for a specific date on OpenTable and returns whether the date is available.
    """
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('check_availability', ctx.author)
            
            # Navigate to the restaurant's page
            browser.navigate_to_url(url)
            time.sleep(3)  # Wait for the page to load
            
            # Open the date picker
            date_field = browser.driver.find_element(By.CSS_SELECTOR, "#restProfileSideBarDtpDayPicker-label")
            date_field.click()
            time.sleep(1)  # Wait for the calendar to open
            
            # Search for the date in the current month
            try:
                date_button = browser.driver.find_element(By.CSS_SELECTOR, f"#restProfileSideBarDtpDayPicker-wrapper button[aria-label*='{date_str}']")
                # Ensure the element is interactable
                #browser.driver.execute_script("arguments[0].scrollIntoView(true);", date_button)
                date_button.click()
                print(f"Clicked on the date: {date_str}")
            except (NoSuchElementException, ElementNotInteractableException) as e:
                await ctx.send(f"Failed to click the date {date_str}: {str(e)}")
                return

            time.sleep(2)  # Wait for the page to load after clicking the date

            # Check for availability
            try:
                # Look for the "Select a time" header to confirm availability
                available_element = browser.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="select-time-header"]')
                await ctx.send(f"Date {date_str} is available!")
            except NoSuchElementException:
                # If not found, check for the "no availability" message
                no_availability_element = browser.driver.find_element(By.CSS_SELECTOR, "div._8ye6OVzeOuU- span")
                if no_availability_element:
                    await ctx.send(f"No availability for the selected date {date_str}.")
                else:
                    await ctx.send(f"Date {date_str} is available!")

        except Exception as e:
            logger.log_command_failed('check_availability', e)
            await ctx.send(f"Failed to check availability: {e}")
    else:
        logger.log_wrong_channel('check_availability', ctx.author)
        await ctx.send("This command can only be used in the designated channel.")

@bot.command(name='login')
async def login(ctx, site: str, *args):
    if ctx.channel.id == Config.CHANNEL_ID:
        try:
            logger.log_command_execution('login', ctx.author)

            # Get the appropriate selectors and credentials based on the site
            selectors = Selectors.get_selectors_for_url(site)
            if not selectors:
                await ctx.send(f"No selectors found for {site}.")
                return
            
            username = getattr(Config, f"{site.upper()}_USERNAME", None)
            password = getattr(Config, f"{site.upper()}_PASSWORD", None)
            if not username or not password:
                await ctx.send(f"Credentials for {site} are not configured.")
                return

            # Determine incognito mode and retries
            incognito = "incognito" in args
            retries = next((int(arg) for arg in args if arg.isdigit()), 1)

            # Call the login method from BrowserInterface
            response = browser.login(selectors['url'], username, password, incognito=incognito, retries=retries)
            await ctx.send(response)

        except Exception as e:
            logger.log_command_failed('login', e)
            await ctx.send(f"Failed to log in to {site}: {e}")
    else:
        logger.log_wrong_channel('login', ctx.author)
        await ctx.send("This command can only be used in the designated channel.")

# Run the bot with the token from config.py
bot.run(Config.DISCORD_TOKEN)