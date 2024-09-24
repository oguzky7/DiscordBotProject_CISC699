from discord.ext import commands
from control.AccountControl import AccountControl
from DataObjects.global_vars import GlobalState

class AccountBoundary(commands.Cog):
    def __init__(self):
        self.control = AccountControl()  # Initialize control object

    @commands.command(name="fetch_all_accounts")
    async def fetch_all_accounts(self, ctx):
        await ctx.send("Command recognized, passing data to control.")

        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command

        result = self.control.receive_command(command)

        # Send the result (prepared by control) back to the user
        await ctx.send(result)


    @commands.command(name="fetch_account_by_website")
    async def fetch_account_by_website(self, ctx):
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        website = list[1]  # Second element is the URL

        await ctx.send(f"Command recognized, passing data to control for website {website}.")

        result = self.control.receive_command(command, website)

        # Send the result (prepared by control) back to the user
        await ctx.send(result)


    @commands.command(name="add_account")
    async def add_account(self, ctx):
        await ctx.send("Command recognized, passing data to control.")
        
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        username = list[1]  # Second element is the username
        password = list[2]  # Third element is the passwrod
        website = list[3]  # Third element is the website

        result = self.control.receive_command(command, username, password, website)

        # Send the result (prepared by control) back to the user
        await ctx.send(result)


    @commands.command(name="delete_account")
    async def delete_account(self, ctx):
        
        list = GlobalState.parse_user_message(GlobalState.user_message) # Parse the message into command and up to 6 variables
        command = list[0]  # First element is the command
        account_id = list[1]  # Second element is the account_id

        await ctx.send(f"Command recognized, passing data to control to delete account with ID {account_id}.")

        result = self.control.receive_command(command, account_id)

        # Send the result (prepared by control) back to the user
        await ctx.send(result)
