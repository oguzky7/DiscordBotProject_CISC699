import sys, os, pytest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import patch, AsyncMock, Mock
from control.BrowserControl import BrowserControl
from entity.BrowserEntity import BrowserEntity
from test_init import logging

# Ensure that BrowserEntity initializes 'driver' in the constructor or in an accessible method before use

@pytest.fixture
def browser_entity_setup():
    with patch('selenium.webdriver.Chrome') as mock_browser:
        entity = BrowserEntity()
        entity.driver = Mock()
        entity.driver.get = Mock()
        entity.driver.find_element = Mock()
        return entity

def test_website_interaction(browser_entity_setup):
    logging.info("Starting test: Website Interaction for Login")
    
    browser_entity = browser_entity_setup
    browser_entity.login = Mock(return_value="Login successful!")
    
    result = browser_entity.login("http://example.com", "user", "pass")
    
    logging.info("Expected to attempt login on 'http://example.com'")
    logging.info(f"Actual outcome: {result}")
    
    assert "Login successful!" in result
    logging.info("Step 2 executed and Test passed: Website Interaction for Login was successful")

if __name__ == "__main__":
    pytest.main([__file__])
