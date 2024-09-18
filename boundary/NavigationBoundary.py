from discord.ext import commands
from control.NavigationControl import NavigationControl

class NavigationBoundary(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.navigation_control = NavigationControl()                                   # Initialize the control object

    @commands.command(name='navigate_to_website')
    async def navigate_to_website(self, ctx, url: str=None):
        await ctx.send("Command recognized, passing the data to control object.")       # Inform the user that the command is recognized
        
        commandToPass = "navigate_to_website"
        result = self.navigation_control.receive_command(commandToPass, url)            # Pass the command and URL to the control object
        await ctx.send(result)                                                          # Send the result back to the user
