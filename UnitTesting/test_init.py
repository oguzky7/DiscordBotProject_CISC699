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

if __name__ == "__main__":
    pytest.main()
