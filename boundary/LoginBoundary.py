from discord.ext import commands
from control.LoginControl import LoginControl

class LoginBoundary(commands.Cog):
    def __init__(self):
        self.login_control = LoginControl()  

    @commands.command(name='login')
    async def login(self, ctx, site: str):
        await ctx.send("Command recognized, passing data to control.")

        # Pass the command and site to control
        commandToPass = "login"
        result = await self.login_control.receive_command(commandToPass, site)
        
        # Send the result back to the user
        await ctx.send(result)
