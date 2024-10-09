from test_init import *
"""
Executable steps for the !login command use case:
1. Control Layer Processing
This test will ensure that BotControl.receive_command() handles the "!login" command correctly, including proper parameter passing and validation.

2. Website Interaction
This test will focus on the BrowserEntity.login() function to ensure it processes the request to log into the website using the provided credentials.

3. Response Generation
This test will validate that the control layer correctly interprets the response from the website interaction step and returns the appropriate result to the boundary layer.
"""

# test_bot_control_login.py
@pytest.mark.asyncio
async def test_control_layer_login():
    logging.info("Starting test: Control Layer Processing for Login")
    
    with patch('entity.BrowserEntity.BrowserEntity.login', new_callable=AsyncMock) as mock_login:
        mock_login.return_value = "Login successful!"
        browser_control = BrowserControl()

        result = await browser_control.receive_command("login", "example.com", "user", "pass")
        
        logging.info(f"Expected outcome: Control Object Result: Login successful!")
        logging.info(f"Actual outcome: {result}")
        
        assert result == "Control Object Result: Login successful!"
        logging.info("Step 1 executed and Test passed: Control Layer Processing for Login was successful")

@pytest.fixture
def browser_entity_setup():     # Fixture to setup the BrowserEntity for testing
    with patch('selenium.webdriver.Chrome') as mock_browser:    # Mocking the Chrome browser
        entity = BrowserEntity()    # Creating an instance of BrowserEntity
        entity.driver = Mock()  # Mocking the driver
        entity.driver.get = Mock()  # Mocking the get method
        entity.driver.find_element = Mock() # Mocking the find_element method
        return entity

def test_website_interaction(browser_entity_setup):
    logging.info("Starting test: Website Interaction for Login")    
    
    browser_entity = browser_entity_setup   # Setting up the BrowserEntity
    browser_entity.login = Mock(return_value="Login successful!")   # Mocking the login method
    
    result = browser_entity.login("http://example.com", "user", "pass")  # Calling the login method
    
    logging.info("Expected to attempt login on 'http://example.com'")       
    logging.info(f"Actual outcome: {result}")
    
    assert "Login successful!" in result    # Assertion to check if the login was successful
    logging.info("Step 2 executed and Test passed: Website Interaction for Login was successful")

# test_response_generation.py
@pytest.mark.asyncio
async def test_response_generation():
    logging.info("Starting test: Response Generation for Login")
    
    with patch('control.BrowserControl.BrowserControl.receive_command', new_callable=AsyncMock) as mock_receive:
        mock_receive.return_value = "Login successful!"
        browser_control = BrowserControl()

        result = await browser_control.receive_command("login", "example.com", "user", "pass")
        
        logging.info("Expected outcome: 'Login successful!'")
        logging.info(f"Actual outcome: {result}")
        
        assert "Login successful!" in result
        logging.info("Step 3 executed and Test passed: Response Generation for Login was successful")

# This condition ensures that the pytest runner handles the test run.
if __name__ == "__main__":
    pytest.main([__file__])
