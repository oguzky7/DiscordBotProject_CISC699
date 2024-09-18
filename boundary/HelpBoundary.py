from discord.ext import commands
from control.HelpControl import HelpControl

class HelpBoundary(commands.Cog):
    def __init__(self):
        self.control = HelpControl()  # Initialize control object

    @commands.command(name="project_help")
    async def project_help(self, ctx):
        await ctx.send("Command recognized, passing data to control.")
        
        # Pass the command to the control object
        commandToPass = "project_help"
        response = self.control.receive_command(commandToPass)
        
        # Send the response back to the user
        await ctx.send(response)
