from browser_interface import BrowserInterface

def test_browser():
    # Initialize the browser interface
    browser = BrowserInterface()

    # Launch Chrome
    browser.launch_browser()

    # Navigate to a website (example: Google)
    browser.navigate_to_url("https://www.google.com")

    # Close the browser after a short delay
    import time
    time.sleep(5)  # Wait for 5 seconds to see the browser
    browser.close_browser()

if __name__ == "__main__":
    test_browser()
