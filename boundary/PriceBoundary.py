from discord.ext import commands
from control.PriceControl import PriceControl
from DataObjects.global_vars import GlobalState

class PriceBoundary(commands.Cog):
    def __init__(self):
        # Initialize control objects directly
        self.price_control = PriceControl()

    @commands.command(name='get_price')
    async def get_price(self, ctx):
        """Command to get the price from the given URL."""
        await ctx.send("Command recognized, passing data to control.")

        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        website = list[1]  # Second element is the URL

        result = await self.price_control.receive_command(command, website) # Pass the command to the control layer
        await ctx.send(f"Price found: {result}")


    @commands.command(name='start_monitoring_price')
    async def start_monitoring_price(self, ctx):
        """Command to monitor price at given frequency."""
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        website = list[1]  # Second element is the URL
        frequency = list[2]

        await ctx.send(f"Command recognized, starting price monitoring at {website} every {frequency} second(s).")
        
        response = await self.price_control.receive_command(command, website, frequency)
        await ctx.send(response)


    @commands.command(name='stop_monitoring_price')
    async def stop_monitoring_price(self, ctx):
        """Command to stop monitoring the price."""
        await ctx.send("Command recognized, passing data to control.")

        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command

        response = await self.price_control.receive_command(command)            # Pass the command to the control layer

        await ctx.send(response)
