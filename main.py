from utils.MyBot import start_bot
from utils.Config import Config

# Initialize and run the bot
if __name__ == "__main__":
    print("Bot is starting...")
    start_bot(Config.DISCORD_TOKEN)  # Start the bot using the token from config
