from discord.ext import commands
from control.AvailabilityControl import AvailabilityControl

class AvailabilityBoundary(commands.Cog):
    def __init__(self):
        # Initialize control objects directly
        self.availability_control = AvailabilityControl()  

    @commands.command(name="check_availability")
    async def check_availability(self, ctx, url: str = None, date_str=None):
        await ctx.send("Command recognized, passing data to control.")
        
        # Pass the command and data to the control layer using receive_command
        command_to_pass = "check_availability"
        result = await self.availability_control.receive_command(command_to_pass, url, date_str)
        
        # Send the result back to the user
        await ctx.send(result)


    @commands.command(name="start_monitoring_availability")
    async def start_monitoring_availability(self, ctx, url: str = None, date_str=None, frequency: int = 15):
        await ctx.send("Command recognized, passing data to control.")
        
        # Pass the command and data to the control layer using receive_command
        command_to_pass = "start_monitoring_availability"
        response = await self.availability_control.receive_command(command_to_pass, url, date_str, frequency)
        
        # Send the result back to the user
        await ctx.send(response)


    @commands.command(name='stop_monitoring_availability')
    async def stop_monitoring_availability(self, ctx):
        """Command to stop monitoring the price."""
        await ctx.send("Command recognized, passing data to control.")
        # Pass the command to the control layer
        command_to_pass = "stop_monitoring_availability"
        response = await self.availability_control.receive_command(command_to_pass)
        await ctx.send(response)
