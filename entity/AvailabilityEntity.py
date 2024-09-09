from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from utils.css_selectors import Selectors

class AvailabilityEntity:
    def __init__(self):
        self.driver = webdriver.Chrome()

    async def check_availability(self, ctx, url, date_str=None, time_slot=None):
        self.driver.get(url)
        time.sleep(3)  # Wait for page to load

        # Get selectors for the given URL
        selectors = Selectors.get_selectors_for_url(url)
        if not selectors:
            return "No valid selectors found for this URL."

        # Date Selection
        if date_str:
            date_field = self.driver.find_element(By.CSS_SELECTOR, selectors['date_field'])
            date_field.click()
            time.sleep(1)
            try:
                date_button = self.driver.find_element(By.CSS_SELECTOR, f"{selectors['date_field']}-wrapper button[aria-label*='{date_str}']")
                date_button.click()
            except Exception as e:
                return f"Failed to select the date: {str(e)}"

        # Time Selection
        if time_slot:
            time_field = self.driver.find_element(By.CSS_SELECTOR, selectors['time_field'])
            time_field.clear()
            time_field.send_keys(time_slot)

        time.sleep(2)  # Wait for updates
        try:
            availability_element = self.driver.find_element(By.CSS_SELECTOR, selectors['availability_result'])
            return f"Date {date_str if date_str else 'current date'} is available!"
        except:
            return "No availability for the selected date."
