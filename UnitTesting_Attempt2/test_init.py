# Purpose: This file contains common setup code for all test cases.
import sys, os, discord, logging, unittest
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from unittest.mock import AsyncMock
from utils.MyBot import MyBot

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CustomTextTestResult(unittest.TextTestResult):
    """Custom test result to output 'Unit test passed' instead of 'ok'."""
    def addSuccess(self, test):
        super().addSuccess(test)
        self.stream.write("Unit test passed\n-------------------------------\n")  # Custom success message
        self.stream.flush()

class CustomTextTestRunner(unittest.TextTestRunner):
    """Custom test runner that uses the custom result class."""
    resultclass = CustomTextTestResult

class BaseTestSetup(unittest.IsolatedAsyncioTestCase):
    """Base setup class for initializing bot and mock context for all tests."""
    
    async def asyncSetUp(self):
        """Setup the bot and mock context before each test."""
        logging.info("Setting up the bot and mock context for testing...")
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = MyBot(command_prefix="!", intents=intents)
        self.ctx = AsyncMock()
        self.ctx.send = AsyncMock()
        self.ctx.bot = self.bot  # Mock the bot property in the context
        await self.bot.setup_hook()  # Ensure commands are registered
