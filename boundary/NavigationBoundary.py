from discord.ext import commands
from control.NavigationControl import NavigationControl
from DataObjects.global_vars import GlobalState

class NavigationBoundary(commands.Cog):

    def __init__(self):
        self.navigation_control = NavigationControl()                                   # Initialize the control object

    @commands.command(name='navigate_to_website')
    async def navigate_to_website(self, ctx):
        await ctx.send("Command recognized, passing the data to control object.")       # Inform the user that the command is recognized
        
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables

        command = list[0]  # First element is the command
        url = list[1]  # Second element is the URL
        print("Parsed command: ", command)
        print("Parsed URL: ", url)
        
        result = self.navigation_control.receive_command(command, url) # Pass the parsed variables to the control object
        await ctx.send(result)                                                          # Send the result back to the user
