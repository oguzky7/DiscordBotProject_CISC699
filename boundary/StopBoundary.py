from discord.ext import commands
from control.StopControl import StopControl

class StopBoundary(commands.Cog):
    def __init__(self):
        self.control = StopControl()  # Initialize control object

    @commands.command(name="stop_bot")
    async def stop_bot(self, ctx):
        await ctx.send("Command recognized, passing data to control.")
        
        # Pass the command to the control object
        commandToPass = "stop_bot"
        result = await self.control.receive_command(commandToPass, ctx)
        print(result)  # Send the result back to the Terminal. since the bot is shut down, it won't be able to send the message back to the user.
        