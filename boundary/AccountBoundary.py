from discord.ext import commands
from control.AccountControl import AccountControl

class AccountBoundary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.control = AccountControl()

    @commands.command(name="fetch_all_accounts")
    async def fetch_all_accounts(self, ctx):
        """Fetch all accounts from the database."""
        await ctx.send("Command recognized, taking action: Fetching all accounts.")
        accounts = self.control.fetch_all_accounts()
        if accounts:
            account_list = "\n".join([f"ID: {acc[0]}, Username: {acc[1]}, Password: {acc[2]}, Website: {acc[3]}" for acc in accounts])
            await ctx.send(f"Accounts:\n{account_list}")
        else:
            await ctx.send("No accounts found.")

    @commands.command(name="fetch_account_by_website")
    async def fetch_account_by_website(self, ctx, website: str):
        """Fetch an account by website."""
        await ctx.send(f"Command recognized, taking action: Fetching account for website {website}.")
        account = self.control.fetch_account_by_website(website)
        if account:
            await ctx.send(f"Account for {website}: Username: {account[0]}, Password: {account[1]}")
        else:
            await ctx.send(f"No account found for website {website}.")

    @commands.command(name="add_account")
    async def add_account(self, ctx, username: str, password: str, website: str):
        """Add a new account."""
        await ctx.send("Command recognized, taking action: Adding a new account.")
        result = self.control.add_account(username, password, website)
        if result:
            await ctx.send(f"Account for {website} added successfully.")
        else:
            await ctx.send(f"Failed to add account for {website}.")

    @commands.command(name="delete_account")
    async def delete_account(self, ctx, account_id: int):
        """Delete an account by ID."""
        await ctx.send(f"Command recognized, taking action: Deleting account with ID {account_id}.")
        result = self.control.delete_account(account_id)
        if result:
            await ctx.send(f"Account with ID {account_id} deleted successfully.")
        else:
            await ctx.send(f"Failed to delete account with ID {account_id}.")

