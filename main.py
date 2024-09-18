from utils.MyBot import MyBot
from utils.Config import Config 
import discord

intents = discord.Intents.default()
intents.message_content = True  # Enable reading message content

# Initialize and run the bot
if __name__ == "__main__":
    bot = MyBot(command_prefix="!", intents=intents, case_insensitive=True)
    print("Bot is starting...")
    bot.run(Config.DISCORD_TOKEN)  # Run the bot with your token
