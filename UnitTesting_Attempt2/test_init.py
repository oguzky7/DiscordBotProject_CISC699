# test_init.py
import sys
import os
import unittest
from unittest.mock import patch, AsyncMock
import logging

# Ensure all necessary paths are included for modules that tests need to access
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Setting up logging without timestamp
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

# Import your BrowserControl class and any other common classes
from control.BrowserControl import BrowserControl

class BaseTestCase(unittest.TestCase):
    """Base test class that can be extended by other test modules."""
    
    def setUp(self):
        """Set up BrowserControl and context for each test."""
        self.control = BrowserControl()
        self.ctx = AsyncMock()  # Mocking the context to use in the control object
