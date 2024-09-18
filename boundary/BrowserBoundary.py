from discord.ext import commands
from control.BrowserControl import BrowserControl

class BrowserBoundary(commands.Cog):
    def __init__(self):
        self.browser_control = BrowserControl() # Initialize the control object

    @commands.command(name='launch_browser')
    async def launch_browser(self, ctx):
        # Inform the user that the command is recognized
        await ctx.send("Command recognized, passing the data to control object.")
        
        commandToPass = "launch_browser"
        result = self.browser_control.receive_command(commandToPass)    # Pass data to the control object
        await ctx.send(result)  # Send the result back to the user

    @commands.command(name="close_browser")
    async def stop_bot(self, ctx):
        # Inform the user that the command is recognized
        await ctx.send("Command recognized, passing the data to control object.")
        
        commandToPass = "close_browser"
        result = self.browser_control.receive_command(commandToPass)    # Pass data to the control object
        await ctx.send(result)  # Send the result back to the user
