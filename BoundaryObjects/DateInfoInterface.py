import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from CISC699.css_selectors import Selectors
from CISC699.help import get_help_message  # Import the help message function
import asyncio
from selenium.webdriver.common.by import By

availability_stop_event = asyncio.Event()  # Global event to stop availability check

class DateInfoInterface:

    def __init__(self, driver):
        self.driver = driver

    async def select_date(self, date_selector, date):
        date_field = self.driver.find_element(By.CSS_SELECTOR, date_selector)
        date_field.clear()
        date_field.send_keys(date)
        print(f"Selected date: {date}")

    async def select_time(self, time_selector, time_slot):
        time_field = self.driver.find_element(By.CSS_SELECTOR, time_selector)
        time_field.clear()
        time_field.send_keys(time_slot)
        print(f"Selected time: {time_slot}")

    async def check_availability(self, url, date=None, time_slot=None):
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors:
            raise ValueError(f"No selectors found for URL: {url}")

        await self.navigate_to_url(selectors['url'])

        if date:
            await self.select_date(selectors['date_field'], date)
        if time_slot:
            await self.select_time(selectors['time_field'], time_slot)

        find_table_button = self.driver.find_element(By.CSS_SELECTOR, selectors['find_table_button'])
        find_table_button.click()

        await asyncio.sleep(2)  # Wait for the results to load

        availability_result = self.driver.find_element(By.CSS_SELECTOR, selectors['availability_result'])
        availability_text = availability_result.text
        print(f"Availability result: {availability_text}")
        return availability_text
