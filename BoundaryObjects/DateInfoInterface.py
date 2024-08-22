import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from CISC699 import logger
from CISC699.config import Config
from selenium.webdriver.common.by import By
from ProductInfoInterface import browser
import time
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException

class DateInfoInterface:

    async def check_availability(ctx, url: str, date_str: str = None, time_slot: str = None):
        """
        Checks availability for a specific date and time on OpenTable and returns whether the date is available.
        If date_str or time_slot is not provided, it will use the current defaulted date/time on the website.
        """
        try:
            logger.log_command_execution('check_availability', ctx.author)
            
            # Navigate to the restaurant's page
            browser.navigate_to_url(url)
            time.sleep(3)  # Wait for the page to load

            # If date_str is provided, select the date
            if date_str:
                # Open the date picker
                date_field = browser.driver.find_element(By.CSS_SELECTOR, "#restProfileSideBarDtpDayPicker-label")
                date_field.click()
                time.sleep(1)  # Wait for the calendar to open

                try:
                    date_button = browser.driver.find_element(By.CSS_SELECTOR, f"#restProfileSideBarDtpDayPicker-wrapper button[aria-label*='{date_str}']")
                    date_button.click()
                    print(f"Clicked on the date: {date_str}")
                except (NoSuchElementException, ElementNotInteractableException) as e:
                    await ctx.send(f"Failed to click the date {date_str}: {str(e)}")
                    return
            else:
                print("No date provided, using the website's default date.")

            # If time_slot is provided, select the time
            if time_slot:
                time_field = browser.driver.find_element(By.CSS_SELECTOR, "#restProfileSideBartimePickerDtpPicker")
                time_field.clear()
                time_field.send_keys(time_slot)
                print(f"Selected time: {time_slot}")
            else:
                print("No time slot provided, using the website's default time.")

            time.sleep(2)  # Wait for the page to load after selecting the date/time

            # Check for availability
            try:
                # Look for the "Select a time" header to confirm availability
                available_element = browser.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="select-time-header"]')
                await ctx.send(f"Date {date_str if date_str else 'current date'} is available!")
            except NoSuchElementException:
                # If not found, check for the "no availability" message
                no_availability_element = browser.driver.find_element(By.CSS_SELECTOR, "div._8ye6OVzeOuU- span")
                if no_availability_element:
                    await ctx.send(f"No availability for the selected date {date_str if date_str else 'current date'}.")
                else:
                    await ctx.send(f"Date {date_str if date_str else 'current date'} is available!")

        except Exception as e:
            logger.log_command_failed('check_availability', e)
            await ctx.send(f"Failed to check availability: {e}")