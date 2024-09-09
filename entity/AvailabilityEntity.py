import asyncio
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.css_selectors import Selectors
from entity.BrowserEntity import BrowserEntity  # Import BrowserEntity

class AvailabilityEntity:
    def __init__(self):
        self.browser_entity = BrowserEntity()  # Initialize BrowserEntity

    async def check_availability(self, ctx, url, date_str=None, time_slot=None, timeout=5):
        # Use BrowserEntity to navigate to the URL
        self.browser_entity.navigate_to_url(url)

        # Wait for page to load (you can tweak the sleep time based on your page loading behavior)
        await asyncio.sleep(3)

        # Get selectors for the given URL
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors:
            return "No valid selectors found for this URL."

        # Ensure select_time and no_availability exist in selectors
        if 'select_time' not in selectors or 'no_availability' not in selectors:
            return "Missing required selectors for availability check."

        # Perform date and time selection (optional)
        if date_str:
            try:
                date_field = self.browser_entity.driver.find_element(By.CSS_SELECTOR, selectors['date_field'])
                date_field.click()
                await asyncio.sleep(1)
                date_button = self.browser_entity.driver.find_element(By.CSS_SELECTOR, f"{selectors['select_date']} button[aria-label*='{date_str}']")
                date_button.click()
            except Exception as e:
                return f"Failed to select the date: {str(e)}"

        if time_slot:
            try:
                time_field = self.browser_entity.driver.find_element(By.CSS_SELECTOR, selectors['time_field'])
                time_field.clear()
                time_field.send_keys(time_slot)
            except Exception as e:
                return f"Failed to select the time: {str(e)}"

        await asyncio.sleep(2)  # Wait for updates (adjust this time based on page response)

        # Initialize flags for select_time and no_availability elements
        select_time_seen = False
        no_availability_seen = False

        try:
            # Check if 'select_time' is available within the given timeout
            WebDriverWait(self.browser_entity.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selectors['select_time']))
            )
            select_time_seen = True  # If found, set the flag to True
        except:
            select_time_seen = False  # If not found within timeout

        try:
            # Check if 'no_availability' is available within the given timeout
            WebDriverWait(self.browser_entity.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selectors['no_availability']))
            )
            no_availability_seen = True  # If found, set the flag to True
        except:
            no_availability_seen = False  # If not found within timeout

        # Logic to determine availability
        if select_time_seen:
            return f"Selected or default date {date_str if date_str else 'current date'} is available for booking."
        elif no_availability_seen:
            return "No availability for the selected date."
        else:
            return "Unable to determine availability. Please try again."
