from discord.ext import commands
from control.AvailabilityControl import AvailabilityControl
from DataObjects.global_vars import GlobalState

class AvailabilityBoundary(commands.Cog):

    def __init__(self):
        # Initialize control objects directly
        self.availability_control = AvailabilityControl()  


    @commands.command(name="check_availability")
    async def check_availability(self, ctx):
        await ctx.send("Command recognized, passing data to control.")
            
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables

        command = list[0]  # First element is the command
        url = list[1]  # Second element is the URL
        date_str = list[2]  # Third element is the date

        # Pass the command and data to the control layer using receive_command
        result = await self.availability_control.receive_command(command, url, date_str)
        
        # Send the result back to the user
        await ctx.send(result)


    @commands.command(name="start_monitoring_availability")
    async def start_monitoring_availability(self, ctx):
        await ctx.send("Command recognized, passing data to control.")

        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables

        command = list[0]  # First element is the command
        url = list[1]  # Second element is the URL
        date_str = list[2]  # Third element is the date
        frequency = list[3] # Fourth element is the frequency

        response = await self.availability_control.receive_command(command, url, date_str, frequency)
        
        # Send the result back to the user
        await ctx.send(response)


    @commands.command(name='stop_monitoring_availability')
    async def stop_monitoring_availability(self, ctx):
        """Command to stop monitoring the price."""
        await ctx.send("Command recognized, passing data to control.")

        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables

        command = list[0]  # First element is the command
        
        response = await self.availability_control.receive_command(command)        # Pass the command to the control layer
        await ctx.send(response)
