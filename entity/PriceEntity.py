from selenium.webdriver.common.by import By
from entity.BrowserEntity import BrowserEntity
from utils.exportUtils import ExportUtils  # Import ExportUtils for handling data export
from utils.css_selectors import Selectors  # Import selectors to get CSS selectors for the browser

class PriceEntity:
    """PriceEntity is responsible for interacting with the system (browser) to fetch prices 
    and handle the exporting of data to Excel and HTML."""
    
    def __init__(self):
        self.browser_entity = BrowserEntity()

    def get_price_from_page(self, url: str):        
        # Navigate to the URL using BrowserEntity
        self.browser_entity.navigate_to_website(url)
        selectors = Selectors.get_selectors_for_url(url)
        try:
            # Find the price element on the page using the selector
            price_element = self.browser_entity.driver.find_element(By.CSS_SELECTOR, selectors['price'])
            result = price_element.text
            return result
        except Exception as e:
            return f"Error fetching price: {str(e)}"    
        

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
