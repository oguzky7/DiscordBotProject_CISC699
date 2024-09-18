from discord.ext import commands
from control.PriceControl import PriceControl

class PriceBoundary(commands.Cog):
    def __init__(self, browser_entity):
        # Initialize control objects directly
        self.price_control = PriceControl()

    @commands.command(name='get_price')
    async def get_price(self, ctx, url: str=None):
        """Command to get the price from the given URL."""
        await ctx.send("Command recognized, passing data to control.")
        # Pass the command to the control layer
        command_to_pass = "get_price"
        result = await self.price_control.receive_command(command_to_pass, url)
        await ctx.send(result)

    @commands.command(name='start_monitoring_price')
    async def start_monitoring_price(self, ctx, url: str = None, frequency: int = 20):
        """Command to monitor price at given frequency."""
        await ctx.send(f"Command recognized, starting price monitoring at {url} every {frequency} second(s).")
        # Pass the command and data to the control layer
        command_to_pass = "monitor_price"
        response = await self.price_control.receive_command(command_to_pass, url, frequency)
        await ctx.send(response)

    @commands.command(name='stop_monitoring_price')
    async def stop_monitoring_price(self, ctx):
        """Command to stop monitoring the price."""
        await ctx.send("Command recognized, passing data to control.")
        # Pass the command to the control layer
        command_to_pass = "stop_monitoring_price"
        response = self.price_control.receive_command(command_to_pass)
        await ctx.send(response)
