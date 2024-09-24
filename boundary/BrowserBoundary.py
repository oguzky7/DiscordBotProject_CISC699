from discord.ext import commands
from control.BrowserControl import BrowserControl
from DataObjects.global_vars import GlobalState 

class BrowserBoundary(commands.Cog):
    def __init__(self):
        self.browser_control = BrowserControl()  # Initialize the control object

    @commands.command(name='launch_browser')
    async def launch_browser(self, ctx):
        await ctx.send(f"Command recognized, passing to control object.")
        
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command

        result = self.browser_control.receive_command(command)     # Pass the updated user_message to the control object
        await ctx.send(result)                                                      # Send the result back to the user

    @commands.command(name="close_browser")
    async def stop_bot(self, ctx):
        await ctx.send(f"Command recognized, passing to control object.")
        
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        
        result = self.browser_control.receive_command(command)
        await ctx.send(result)
