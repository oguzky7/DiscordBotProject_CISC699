import asyncio
from control.BotControl import BotControl
from Config import Config

async def main():
    bot_control = BotControl()
    await bot_control.start(Config.DISCORD_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
