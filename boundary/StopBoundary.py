from discord.ext import commands
from control.StopControl import StopControl
from DataObjects.global_vars import GlobalState

class StopBoundary(commands.Cog):
    def __init__(self):
        self.control = StopControl()  # Initialize control object

    @commands.command(name="stop_bot")
    async def stop_bot(self, ctx):
        await ctx.send("Command recognized, passing data to control.")
        
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        
        result = await self.control.receive_command(command, ctx)
        print(result)  # Send the result back to the Terminal. since the bot is shut down, it won't be able to send the message back to the user.
        