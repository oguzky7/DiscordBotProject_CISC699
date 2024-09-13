from entity.BrowserEntity import BrowserEntity
from control.AccountControl import AccountControl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.css_selectors import Selectors 
import asyncio

class LoginControl:
    def __init__(self, browser_entity):
        self.browser_entity = browser_entity  # Manages browser state
        self.account_control  = AccountControl()  # Manages account data

    
    async def login(self, site: str):
        # Step 1: Fetch account credentials from the entity object
        account_info = self.account_control.fetch_account_by_website(site)
        if not account_info:
            return f"No account found for {site}"

        # account_info is a tuple (username, password), so access it by index
        username, password = account_info[0], account_info[1]
        print(f"Username: {username}, Password: {password}")

        # Step 3: Get the URL from the CSS selectors
        url = Selectors.get_selectors_for_url(site).get('url')
        print(url)
        if not url:
            return f"URL for {site} not found."

        # Step 4: Navigate to the URL and perform login (handled by the entity object)
        result = await self.browser_entity.perform_login(url, username, password)
        return result