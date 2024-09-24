from discord.ext import commands
from control.HelpControl import HelpControl
from DataObjects.global_vars import GlobalState

class HelpBoundary(commands.Cog):
    def __init__(self):
        self.control = HelpControl()  # Initialize control object

    @commands.command(name="project_help")
    async def project_help(self, ctx):
        await ctx.send("Command recognized, passing data to control.")
        
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command

        response = self.control.receive_command(command)
        
        # Send the response back to the user
        await ctx.send(response)
