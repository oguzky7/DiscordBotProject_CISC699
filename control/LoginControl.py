from control.NavigationControl import NavigationControl
from control.AccountControl import AccountControl
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.css_selectors import Selectors 
import asyncio

class LoginControl:
    def __init__(self):
        self.navigation_control = NavigationControl()
        self.account_control = AccountControl()  # Fetch credentials using AccountControl


    async def login(self, website: str):
        """Fetch credentials and log in to the website."""
        try:
            # Log the start of login process
            print(f"Starting login process for {website}...")

            # Fetch account by website from the database
            account = self.account_control.fetch_account_by_website(website)
            if not account:
                print(f"No account found for {website}.")
                return f"No account found for website {website}. Please add an account first."
            else:
                print(f"Account found for {website}: {account}")

            username, password = account

            # Ensure the browser is launched
            browser_status = self.navigation_control.browser_control.launch_browser()
            print(f"Browser status: {browser_status}")

            # Get the URL and selectors for the website
            url = Selectors.get_selectors_for_url(website)['url']
            print(f"Navigating to URL: {url}")

            # Navigate to the URL
            self.navigation_control.navigate_to_url(url)
            await asyncio.sleep(3)

            # Get the driver
            driver = self.navigation_control.browser_control.browser_entity.get_driver()

            # Enter the email address
            email_field = driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(website)['email_field'])
            email_field.send_keys(username)
            print(f"Entered username: {username}")

            # Enter the password
            password_field = driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(website)['password_field'])
            password_field.send_keys(password)
            print(f"Entered password")

            # Click the login button
            sign_in_button = driver.find_element(By.CSS_SELECTOR, Selectors.get_selectors_for_url(website)['SignIn_button'])
            sign_in_button.click()
            print(f"Clicked login button")

            # Wait for homepage
            WebDriverWait(driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, Selectors.get_selectors_for_url(website)['homePage'])))
            
            return f"{browser_status}\nLogged in to {url} successfully with username: {username}"
        except Exception as e:
            print(f"Login failed: {e}")
            return f"Failed to log in: {e}"
