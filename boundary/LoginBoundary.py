from discord.ext import commands
from control.LoginControl import LoginControl
from DataObjects.global_vars import GlobalState

class LoginBoundary(commands.Cog):
    def __init__(self):
        self.login_control = LoginControl()  

    @commands.command(name='login')
    async def login(self, ctx):
        await ctx.send("Command recognized, passing data to control.")

        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        website = list[1]

        result = await self.login_control.receive_command(command, website)
        
        # Send the result back to the user
        await ctx.send(result)
