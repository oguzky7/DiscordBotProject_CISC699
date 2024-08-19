import logger

class Notification:
    """
    Handles sending notifications and logging them in the system.
    """

    def __init__(self, user):
        self.user = user

    async def send_message(self, channel, message):
        """
        Send a message to a specific channel and log the action.
        """
        logger.log(f"Sending message to {self.user}: {message}")
        await channel.send(message)

    def log_received_message(self, message):
        """
        Log a received message.
        """
        logger.log_message_received(message)
        print(f"Command/message received '{message.content}' from '{message.author}'")

    def log_recognized_message(self):
        """
        Log a recognized message.
        """
        logger.log_message_recognized()
        print("Message recognized as a command. Processing...")

    def log_not_recognized_message(self):
        """
        Log an unrecognized message.
        """
        logger.log_message_not_recognized()
        print("Message not recognized as a command. Suggest typing '!commands'.")

    async def send_help_message(self, channel):
        """
        Send a help message listing possible commands.
        """
        help_message = (
            "Here are the available commands: `!launch_browser`, `!navigate_to_url`, `!get_price`, "
            "`!login`, `!close_browser`, `!commands`, `!stop`, `!monitor_price`.\n\n"
            "You can also use 'incognito' as an option with `!launch_browser`, `!get_price`, and `!login` commands."
        )
        logger.log(f"Sending help message to {self.user}")
        await channel.send(help_message)

    async def send_greeting_message(self, channel):
        """
        Send a greeting message.
        """
        greeting_message = f"Hello, {self.user.name}! How can I help you? If you want to see what I can do, type `!commands`."
        logger.log(f"Sending greeting message to {self.user}")
        await channel.send(greeting_message)

    async def send_error_message(self, channel, error):
        """
        Send an error message and log the error.
        """
        error_message = f"An error occurred: {error}"
        logger.log_command_failed('error', error)
        await channel.send(error_message)

    async def send_stop_message(self, channel):
        """
        Send a stop message and log the action.
        """
        stop_message = "Stopping the bot. Goodbye!"
        logger.log(f"Bot is stopping as requested by {self.user}.")
        await channel.send(stop_message)

    async def notify_price_change(self, channel, price):
        """
        Send a notification to the Discord channel with the found price.
        """
        price_message = f"The price is: {price}"
        logger.log(f"Notifying {self.user} of price change: {price}")
        await channel.send(price_message)
