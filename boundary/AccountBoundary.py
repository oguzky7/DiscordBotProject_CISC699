from discord.ext import commands
from control.AccountControl import AccountControl

class AccountBoundary(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.account_control = AccountControl()


    @commands.command(name='fetch_accounts')
    async def fetch_accounts(self, ctx):
        """Fetch all accounts and display them in Discord."""
        accounts = self.account_control.fetch_accounts()

        if accounts:
            # Create a response message for the fetched accounts
            response = '\n'.join([f"ID: {acc[0]}, Username: {acc[1]}, Password: {acc[2]}" for acc in accounts])
            await ctx.send(response)
        else:
            await ctx.send("No accounts found.")



    @commands.command(name="add_account")
    async def add_account(self, ctx, username: str, password: str):
        """Add a new user account to the database."""
        result = self.account_control.add_account(username, password)
        if result:
            await ctx.send(f"Account for {username} added successfully.")
        else:
            await ctx.send(f"Failed to add account for {username}.")



    @commands.command(name="delete_account")
    async def delete_account(self, ctx, user_id: int):
        """Delete a user account from the database."""
        result = self.account_control.delete_account(user_id)
        if result:
            await ctx.send(f"Account with ID {user_id} deleted successfully.")
        else:
            await ctx.send(f"Failed to delete account with ID {user_id}.")
