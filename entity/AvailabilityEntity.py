import asyncio
from utils.exportUtils import ExportUtils
from entity.BrowserEntity import BrowserEntity
from utils.css_selectors import Selectors
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AvailabilityEntity:
    def __init__(self):
        self.browser_entity = BrowserEntity()


    async def check_availability(self, url: str, date_str=None, timeout=5):
        try:
            # Use BrowserEntity to navigate to the URL
            self.browser_entity.navigate_to_website(url)

            # Get selectors for the given URL
            selectors = Selectors.get_selectors_for_url(url)

            # Perform date selection (optional)
            if date_str:
                try:
                    date_field = self.browser_entity.driver.find_element(By.CSS_SELECTOR, selectors['date_field'])
                    date_field.click()
                    await asyncio.sleep(1)
                    date_button = self.browser_entity.driver.find_element(By.CSS_SELECTOR, f"{selectors['select_date']} button[aria-label*='{date_str}']")
                    date_button.click()
                except Exception as e:
                    return f"Failed to select the date: {str(e)}"

            await asyncio.sleep(2)  # Wait for updates to load

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
                    lambda driver: len(driver.find_elements(By.CSS_SELECTOR, selectors['show_next_available_button'])) > 0
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
            
        except Exception as e:
            return f"Failed to check availability: {str(e)}"


    def export_data(self, dto):
        """Export price data to both Excel and HTML using ExportUtils.
        
        dto: This is a Data Transfer Object (DTO) that contains the command, URL, result, date, and time.
        """
        # Extract the data from the DTO
        command = dto.get('command')
        url = dto.get('url')
        result = dto.get('result')
        entered_date = dto.get('entered_date')  # Optional, could be None
        entered_time = dto.get('entered_time')  # Optional, could be None

        # Call the Excel export method from ExportUtils
        excelResult = ExportUtils.log_to_excel(
            command=command,
            url=url,
            result=result,
            entered_date=entered_date,  # Pass the optional entered_date
            entered_time=entered_time   # Pass the optional entered_time
        )
        print(excelResult)

        # Call the HTML export method from ExportUtils
        htmlResult = ExportUtils.export_to_html(
            command=command,
            url=url,
            result=result,
            entered_date=entered_date,  # Pass the optional entered_date
            entered_time=entered_time   # Pass the optional entered_time
        )
        print(htmlResult)

