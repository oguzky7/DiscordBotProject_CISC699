import asyncio
from utils.exportUtils import ExportUtils
from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AvailabilityEntity:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity

    def export_to_html(self, dto):
        """Export the data to HTML using ExportUtils."""
        return ExportUtils.export_to_html(
            command=dto["command"],
            url=dto["url"],
            result=dto["result"],
            entered_date=dto["entered_date"],
            entered_time=dto["entered_time"]
        )

    def export_to_excel(self, dto):
        """Export the data to Excel using ExportUtils."""
        return ExportUtils.log_to_excel(
            command=dto["command"],
            url=dto["url"],
            result=dto["result"],
            entered_date=dto["entered_date"],
            entered_time=dto["entered_time"]
        )


    async def check_availability(self, url: str, date_str=None, timeout=5):
        # Use BrowserEntity to navigate to the URL
        self.browser_entity.navigate_to_url(url)

        # Get selectors for the given URL
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors:
            return "No valid selectors found for this URL."
        print("debug")
        # Perform date and time selection (optional)
        if date_str:
            print("debug2")
            try:
                print("debug3")
                date_field = self.browser_entity.driver.find_element(By.CSS_SELECTOR, selectors['date_field'])
                date_field.click()
                await asyncio.sleep(1)
                date_button = self.browser_entity.driver.find_element(By.CSS_SELECTOR, f"{selectors['select_date']} button[aria-label*='{date_str}']")
                date_button.click()
            except Exception as e:
                return f"Failed to select the date: {str(e)}"

        await asyncio.sleep(2)  # Wait for updates (adjust this time based on page response)

        # Initialize flags for select_time and no_availability elements
        select_time_seen = False
        no_availability_seen = False
        print("debug4")
        try:
            print("debug5")
            # Check if 'select_time' is available within the given timeout
            WebDriverWait(self.browser_entity.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, selectors['select_time']))
            )
            select_time_seen = True  # If found, set the flag to True
        except:
            select_time_seen = False  # If not found within timeout

        print("debug6")
        try:
            # Check if 'no_availability' is available within the given timeout
            WebDriverWait(self.browser_entity.driver, timeout).until(
                lambda driver: len(driver.find_elements(By.CSS_SELECTOR, selectors['show_next_available_button'])) > 0
            )
            no_availability_seen = True  # If found, set the flag to True
            print("debug7")
        except:
            print("debug8")
            no_availability_seen = False  # If not found within timeout

        # Logic to determine availability
        if select_time_seen:
            return f"Selected or default date {date_str if date_str else 'current date'} is available for booking."
        elif no_availability_seen:
            return "No availability for the selected date."
        else:
            return "Unable to determine availability. Please try again."

