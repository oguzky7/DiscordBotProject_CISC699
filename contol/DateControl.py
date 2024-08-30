from DateEntity import DateEntity
from BrowserControl import BrowserControl
from selenium.webdriver.common.by import By

class DateControl:
    def __init__(self):
        self.date_entity = DateEntity()
        self.browser_control = BrowserControl()

    async def check_availability(self, url, date_str=None, time_slot=None):
        # Launch and navigate using the browser control
        self.browser_control.launch_browser()
        self.browser_control.navigate_to_url(url)

        # Handle the date selection
        if date_str:
            self.date_entity.update_date(date_str)
            date_field = self.browser_control.driver.find_element(By.CSS_SELECTOR, "#restProfileSideBarDtpDayPicker-label")
            date_field.click()
            date_button = self.browser_control.driver.find_element(By.CSS_SELECTOR, f"button[aria-label*='{date_str}']")
            date_button.click()

        # Handle the time slot selection
        if time_slot:
            self.date_entity.update_time_slot(time_slot)
            time_field = self.browser_control.driver.find_element(By.CSS_SELECTOR, "#restProfileSideBartimePickerDtpPicker")
            time_field.send_keys(time_slot)

        # Check availability
        try:
            available_element = self.browser_control.driver.find_element(By.CSS_SELECTOR, 'h3[data-test="select-time-header"]')
            result = "Available"
        except:
            result = "Not Available"

        # Close the browser
        self.browser_control.close_browser()

        return result
