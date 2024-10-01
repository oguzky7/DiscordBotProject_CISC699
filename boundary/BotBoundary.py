from discord.ext import commands
from control.BotControl import BotControl
from DataObjects.global_vars import GlobalState

class BotBoundary(commands.Cog):
    def __init__(self):
        self.bot_control = BotControl()  # Initialize control object

    @commands.command(name="project_help")
    async def project_help(self, ctx):
        """Handle help command by sending available commands to the user."""
        await ctx.send("Command recognized, passing data to control.")
        try:
            list = GlobalState.parse_user_message(GlobalState.user_message)  # Parse the message into command and up to 6 variables
            command = list[0]  # First element is the command

            response = await self.bot_control.receive_command(command)  # Call control layer
            await ctx.send(response)  # Send the response back to the user
        except Exception as e:
            error_msg = f"Error in HelpBoundary: {str(e)}"
            print(error_msg)
            await ctx.send(error_msg)

    @commands.command(name="stop_bot")
    async def stop_bot(self, ctx):
        """Handle stop bot command by shutting down the bot."""
        await ctx.send("Command recognized, passing data to control.")
        try:
            list = GlobalState.parse_user_message(GlobalState.user_message)  # Parse the message into command and up to 6 variables
            command = list[0]  # First element is the command

            result = await self.bot_control.receive_command(command, ctx)  # Call control layer to stop the bot
            print(result)  # Send the result to the terminal since the bot will shut down
        except Exception as e:
            error_msg = f"Error in StopBoundary: {str(e)}"
            print(error_msg)
            await ctx.send(error_msg)

           
    @commands.command(name="receive_email")
    async def receive_email(self, ctx):
        await ctx.send("Command recognized, passing data to control.")

        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        file_name = list[1]  # Second element is the fileName

        result = await self.bot_control.receive_command(command, file_name) # Pass the command to the control layer
        await ctx.send(result)

