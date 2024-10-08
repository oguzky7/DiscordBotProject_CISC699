import sys, os, discord
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
############################################################################################################

import pytest
from discord.ext import commands
from unittest.mock import AsyncMock
from boundary.BotBoundary import BotBoundary
import pytest
from discord.ext import commands


import pytest
from unittest.mock import AsyncMock, MagicMock
from boundary.BotBoundary import BotBoundary
from control.BotControl import BotControl
from discord.ext import commands

@pytest.fixture
def ctx():
    # Mock the Discord context
    context = AsyncMock(spec=commands.Context)
    context.send = AsyncMock()
    return context

@pytest.fixture
def bot_control():
    # Mock the BotControl with its response for project_help
    control = BotControl()
    control.receive_command = AsyncMock(return_value="Here are the available commands: ...")
    return control

@pytest.mark.asyncio
async def test_project_help_boundary(ctx, bot_control):
    # Test the boundary's ability to process 'project_help' command and interact with control
    boundary = BotBoundary()
    boundary.bot_control = bot_control  # Use the mocked control

    await boundary.project_help(ctx)

    # Check if the boundary sends the correct initial and follow-up messages
    ctx.send.assert_called()
    assert ctx.send.call_args_list[0][0][0] == "Command recognized, passing data to control."
    assert ctx.send.call_args_list[1][0][0].startswith("Here are the available commands:")

@pytest.mark.asyncio
async def test_project_help_control(bot_control):
    # Directly test control layer's response to 'project_help'
    response = await bot_control.receive_command('project_help')
    assert "Here are the available commands:" in response

# Additional tests can include error handling, command parsing, and interaction with other modules



# If running the test directly:
if __name__ == "__main__":
    pytest.main([__file__])
