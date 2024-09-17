from discord.ext import commands
from control.BrowserControl import BrowserControl

class BrowserBoundary(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        # Initialize the control object
        self.browser_control = BrowserControl()

    @commands.command(name='launch_browser')
    async def launch_browser(self, ctx):
        # Inform the user that the command is recognized
        await ctx.send("Command recognized, passing data to control.")
        
        # Pass data to the control object
        command_data = "launch_browser"
        result = self.browser_control.process_command(command_data)
        
        # Send the result back to the user
        await ctx.send(result)

    
    @commands.command(name="close_browser")
    async def stop_bot(self, ctx):
        # Inform the user that the command is recognized
        await ctx.send("Command recognized, passing data to control.")

        # Pass data to the control object
        command_data = "close_browser"
        result = self.browser_control.process_command(command_data)
        
        # Send the result back to the user
        await ctx.send(result)