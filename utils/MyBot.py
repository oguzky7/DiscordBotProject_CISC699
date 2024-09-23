import discord
from discord.ext import commands
from boundary.BrowserBoundary import BrowserBoundary
from boundary.NavigationBoundary import NavigationBoundary
from boundary.HelpBoundary import HelpBoundary
from boundary.StopBoundary import StopBoundary
from boundary.LoginBoundary import LoginBoundary
from boundary.AccountBoundary import AccountBoundary
from boundary.AvailabilityBoundary import AvailabilityBoundary
from boundary.PriceBoundary import PriceBoundary

# Bot initialization
intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

class MyBot(commands.Bot):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_message(self, message):
        if message.author == self.user:  # Prevent the bot from replying to its own messages
            return
        
        print(f"Message received: {message.content}")
        user_message = message.content.lower()
        if user_message in ["hi", "hey", "hello"]:
            await message.channel.send("Hi, how can I help you?")  
        else:
            await message.channel.send("I'm sorry, I didn't understand that. Type !project_help to see the list of commands.")
          
        await self.process_commands(message)

    async def setup_hook(self):
        await self.add_cog(BrowserBoundary())  # Add your boundary objects
        await self.add_cog(NavigationBoundary())
        await self.add_cog(HelpBoundary())
        await self.add_cog(StopBoundary())
        await self.add_cog(LoginBoundary())
        await self.add_cog(AccountBoundary())
        await self.add_cog(AvailabilityBoundary())
        await self.add_cog(PriceBoundary())

    async def on_ready(self):
        print(f"Logged in as {self.user}")
        channel = discord.utils.get(self.get_all_channels(), name="general")  # Adjust the channel name if needed
        if channel:
            await channel.send("Hi, I'm online! Type '!project_help' to see what I can do.")

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            print("Command not recognized:")
            print(error)

# Initialize the bot instance
bot = MyBot(command_prefix="!", intents=intents, case_insensitive=True)

def start_bot(token):
    """Run the bot with the provided token."""
    bot.run(token)
