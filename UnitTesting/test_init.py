"""
test_init.py
The primary objective is to consolidate all necessary imports in one place. 
We avoid the redundancy of importing modules and dependencies repeatedly 
in each test file. This helps streamline the test setup, making the individual 
test files cleaner and easier to maintain, as they can focus purely on the logic 
being tested rather than handling multiple import statements. This approach also 
helps ensure consistency across all tests by having a single source for the 
required libraries and modules.
"""
import sys, os, pytest, logging, asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch, AsyncMock, MagicMock, Mock

from control.AvailabilityControl import AvailabilityControl
from control.PriceControl import PriceControl
from control.BrowserControl import BrowserControl
from control.BotControl import BotControl

from entity.BrowserEntity import BrowserEntity
from entity.DataExportEntity import ExportUtils
from entity.PriceEntity import PriceEntity
from entity.AvailabilityEntity import AvailabilityEntity
from entity.EmailEntity import send_email_with_attachments

# Define a function to globally patch everything needed
def apply_global_patches():
    patches = [
        patch('entity.PriceEntity.PriceEntity.get_price_from_page', new_callable=AsyncMock, return_value="100.00"),
        patch('entity.DataExportEntity.ExportUtils.log_to_excel', new_callable=AsyncMock, return_value="Data saved to Excel file at path.xlsx"),
        patch('entity.DataExportEntity.ExportUtils.export_to_html', new_callable=AsyncMock, return_value="Data exported to HTML file at path.html"),
        patch('entity.EmailEntity.send_email_with_attachments', new_callable=AsyncMock, return_value="Mock email sent"),
        patch('control.PriceControl.PriceControl.get_price', new_callable=AsyncMock, return_value=("100.00", "Data saved to Excel file at path.xlsx", "Data exported to HTML file at path.html")),
        patch('control.PriceControl.PriceControl.receive_command', new_callable=AsyncMock, return_value=("100.00", "Data saved to Excel file at path.xlsx", "Data exported to HTML file at path.html")),
        patch('control.AvailabilityControl.AvailabilityControl.receive_command', new_callable=AsyncMock, return_value="Monitoring started"),
        patch('entity.AvailabilityEntity.AvailabilityEntity.check_availability', new_callable=AsyncMock, return_value=("Availability confirmed", "Data saved to Excel file at path.xlsx", "Data exported to HTML file at path.html")),
        patch('entity.BrowserEntity.BrowserEntity.login', new_callable=AsyncMock, return_value="Login successful!"),
        patch('entity.BrowserEntity.BrowserEntity.navigate_to_website', new_callable=AsyncMock, return_value="Navigation successful"),
        patch('entity.BrowserEntity.BrowserEntity.close_browser', new_callable=AsyncMock, return_value="Browser closed successfully."),
        patch('selenium.webdriver.Chrome', new_callable=MagicMock)
]


    # Start all patches and return them so that they can be stopped later if necessary
    applied_patches = [p.start() for p in patches]
    
    # Add a finalizer to stop patches when pytest session ends
    @pytest.fixture(autouse=True, scope="session")
    def stop_patches():
        yield
        for p in applied_patches:
            p.stop()

    return applied_patches

# Apply the global patches when this file is imported
apply_global_patches()


if __name__ == "__main__":
    pytest.main()