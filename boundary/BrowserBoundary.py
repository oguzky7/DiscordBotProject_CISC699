from discord.ext import commands
from control.BrowserControl import BrowserControl
from DataObjects.global_vars import GlobalState

class BrowserBoundary(commands.Cog):
    def __init__(self):
        self.browser_control = BrowserControl()  # Initialize Browser control object

    # Browser-related commands
    @commands.command(name='launch_browser')
    async def launch_browser(self, ctx):
        await ctx.send(f"Command recognized, passing to control object.")
        
        list = GlobalState.parse_user_message(GlobalState.user_message)  # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command

        result = self.browser_control.receive_command(command)  # Pass the updated user_message to the control object
        await ctx.send(result)  # Send the result back to the user

    @commands.command(name="close_browser")
    async def close_browser(self, ctx):
        await ctx.send(f"Command recognized, passing to control object.")
        
        list = GlobalState.parse_user_message(GlobalState.user_message)  # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        
        result = self.browser_control.receive_command(command)
        await ctx.send(result)

    # Login-related commands
    @commands.command(name='login')
    async def login(self, ctx):
        await ctx.send("Command recognized, passing data to control.")
        
        list = GlobalState.parse_user_message(GlobalState.user_message)  # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        website = list[1]

        result = await self.browser_control.receive_command(command, website)  # Pass the command and website to control object
        
        # Send the result back to the user
        await ctx.send(result)

    # Navigation-related commands
    @commands.command(name='navigate_to_website')
    async def navigate_to_website(self, ctx):
        await ctx.send("Command recognized, passing the data to control object.")  # Inform the user that the command is recognized
        
        list = GlobalState.parse_user_message(GlobalState.user_message)  # Parse the message into command and up to 6 variables

        command = list[0]  # First element is the command
        website = list[1]  # Second element is the URL
        
        result = self.browser_control.receive_command(command, website)  # Pass the parsed variables to the control object
        await ctx.send(result)  # Send the result back to the user
