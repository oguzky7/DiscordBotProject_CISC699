import discord # type: ignore
from discord.ext import tasks, commands # type: ignore

import config
import commands as cmd
import scraper
import logger
import beautifier
import checker
import help

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='?', intents=intents)
        self.channel_id = config.Config.CHANNEL_ID

    async def on_ready(self):
        print(f'{self.user} is now running!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await cmd.print_message(self, message)
        await cmd.handle_message(self, message)

    @tasks.loop(seconds=1.0, count = 1)
    async def send_logs(self):
        channel = self.get_channel(self.channel_id)
        logs = await logger.return_logs()
        await beautifier.log_beautify_and_send(logs,channel)

    @tasks.loop(minutes=120.0)
    async def send_trendyol_fiyat(self):
        change_detected = False
        channel = self.get_channel(self.channel_id)
        data = await scraper.scrape_trendyol()
        await logger.log_data(data, channel)
        logs = await logger.return_logs()

        if len(logs) < 2:
            print("logs has one entry, probably first call")
            await beautifier.trendyol_beautify_and_send(data,channel,change_detected)
        else:
            changed_rows_df = await checker.check_price(data,logs)
            
            if changed_rows_df.empty:
                print("No changes detected.")
            else:
                change_detected = True
                await beautifier.trendyol_beautify_and_send(changed_rows_df,channel,change_detected)
    
    @tasks.loop(seconds=1.0, count = 1)
    async def kosmos_get_max_date(self):
        change_detected = ''
        channel = self.get_channel(self.channel_id)
        data = await scraper.scrape_kosmos_max_date()
        if data is None:
            print("scraper failed, data is empty")
            try:
                response = "olmadı yav"
                await channel.send(response)
            except Exception as e:
                print(e)
        else:
            await logger.log_data_kosmos(data)
            await beautifier.kosmos_beautify_and_send(data,channel,change_detected)
        
    @tasks.loop(seconds=1.0, count = 1)
    async def send_kosmos_logs(self):
        channel = self.get_channel(self.channel_id)
        logs = await logger.return_kosmos_logs()
        await beautifier.kosmos_log_beautify_and_send(logs,channel)

    @tasks.loop(minutes = 60.0)
    async def kosmos_get_max_date_job(self):
        channel = self.get_channel(self.channel_id)
        data = await scraper.scrape_kosmos_max_date()

        await logger.log_data_kosmos(data)
        logs = await logger.return_kosmos_logs()

        if len(logs) < 2:
            print("logs is empty, probably first call")
            #logs.at[0, 'Name'] = '1997-09-14'
        else:
            changed_rows_df = await checker.check_kosmos_max_date(data, logs)
            if changed_rows_df.empty:
                print("No changes detected on kosmos.")
            else:
                change_detected = True
                await beautifier.kosmos_beautify_and_send(changed_rows_df,channel,change_detected)

    @tasks.loop(seconds=1.0, count = 1)
    async def help(self):
        channel = self.get_channel(self.channel_id)
        help_list = help.return_help_list()
        for key, value in help_list.items():
            message_to_send = "**" + key + "** -> " + value
            await channel.send(message_to_send)
        message_to_send = '----------------'
        await channel.send(message_to_send)
        message_to_send = 'şimdilik bu kadar.'
        await channel.send(message_to_send)

bot = MyBot()
bot.run(config.Config.TOKEN)