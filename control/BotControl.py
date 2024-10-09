import discord
from entity.EmailEntity import send_email_with_attachments

class BotControl:
    async def receive_command(self, command_data, *args):
        """Handle commands related to help and stopping the bot."""
        print("Data received from boundary:", command_data)

        # Handle help commands
        if command_data == "project_help":
            try:
                help_message = (
                    "Here are the available commands:\n"
                    "!project_help - Get help on available commands.\n"
                    "!fetch_all_accounts - Fetch all stored accounts.\n"
                    "!add_account 'username' 'password' 'website' - Add a new account to the database.\n"
                    "!fetch_account_by_website 'website' - Fetch account details by website.\n"
                    "!delete_account 'account_id' - Delete an account by its ID.\n"
                    "!launch_browser - Launch the browser.\n"
                    "!close_browser - Close the browser.\n"
                    "!navigate_to_website 'url' - Navigate to a specified website.\n"
                    "!login 'website' - Log in to a website (e.g., !login bestbuy).\n"
                    "!get_price 'url' - Check the price of a product on a specified website.\n"
                    "!start_monitoring_price 'url' 'frequency' - Start monitoring a product's price at a specific interval (frequency in minutes).\n"
                    "!stop_monitoring_price - Stop monitoring the product's price.\n"
                    "!check_availability 'url' - Check availability for a restaurant or service.\n"
                    "!start_monitoring_availability 'url' 'frequency' - Monitor availability at a specific interval.\n"
                    "!stop_monitoring_availability - Stop monitoring availability.\n"
                    "!stop_bot - Stop the bot.\n"
                )
                return help_message
            except Exception as e:
                error_msg = f"Error handling help command: {str(e)}"
                print(error_msg)
                return error_msg

        # Handle stop bot commands
        elif command_data == "stop_bot":
            try:
                ctx = args[0] if args else None
                bot = ctx.bot  # Get the bot instance from the context
                await ctx.send("The bot is shutting down...")
                print("Bot is shutting down...")
                await bot.close()  # Close the bot
                result = "Bot has been shut down."
                print(result)
                return result
            except Exception as e:
                error_msg = f"Error shutting down the bot: {str(e)}"
                print(error_msg)
                return error_msg


        # Handle receive email commands
        elif command_data == "receive_email":
            try:
                file_name = args[0] if args else None
                if file_name:
                    print(f"Sending email with the file '{file_name}'...")
                    result = send_email_with_attachments(file_name)
                    print(result)
                else:
                    result = "Please specify a file to send, e.g., !receive_email monitor_price.html"
                return result
            except Exception as e:
                error_msg = f"Error shutting down the bot: {str(e)}"
                print(error_msg)
                return error_msg


        # Default response for invalid commands
        else:
            try:
                return "Invalid command."
            except Exception as e:
                error_msg = f"Error handling invalid command: {str(e)}"
                print(error_msg)
                return error_msg
