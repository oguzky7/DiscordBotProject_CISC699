from discord.ext import commands
from control.NavigationControl import NavigationControl

class NavigationBoundary(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.navigation_control = NavigationControl() # Initialize the control object

    @commands.command(name='navigate_to_website')
    async def navigate_to_website(self, ctx, url: str=None):
        # Inform the user that the command is recognized
        await ctx.send("Command recognized, passing data to control.")
        
        # Pass the command and URL to the control object
        command_data = "navigate_to_website"
        result = self.navigation_control.process_command(command_data, url)
        
        # Send the result back to the user
        await ctx.send(result)
