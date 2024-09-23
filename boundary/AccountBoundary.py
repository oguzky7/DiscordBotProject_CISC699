from discord.ext import commands
from control.AccountControl import AccountControl

class AccountBoundary(commands.Cog):
    def __init__(self):
        self.control = AccountControl()  # Initialize control object

    @commands.command(name="fetch_all_accounts")
    async def fetch_all_accounts(self, ctx):
        await ctx.send("Command recognized, passing data to control.")
        
        # Pass the command to the control object
        commandToPass = "fetch_all_accounts"
        result = self.control.receive_command(commandToPass)

        # Send the result (prepared by control) back to the user
        await ctx.send(result)


    @commands.command(name="fetch_account_by_website")
    async def fetch_account_by_website(self, ctx, website: str):
        await ctx.send(f"Command recognized, passing data to control for website {website}.")
        
        # Pass the command and website to control
        commandToPass = "fetch_account_by_website"
        result = self.control.receive_command(commandToPass, website)

        # Send the result (prepared by control) back to the user
        await ctx.send(result)


    @commands.command(name="add_account")
    async def add_account(self, ctx, username: str, password: str, website: str):
        await ctx.send("Command recognized, passing data to control.")
        
        # Pass the command and account details to control
        commandToPass = "add_account"
        result = self.control.receive_command(commandToPass, username, password, website)

        # Send the result (prepared by control) back to the user
        await ctx.send(result)


    @commands.command(name="delete_account")
    async def delete_account(self, ctx, account_id: int):
        await ctx.send(f"Command recognized, passing data to control to delete account with ID {account_id}.")
        
        # Pass the command and account ID to control
        commandToPass = "delete_account"
        result = self.control.receive_command(commandToPass, account_id)

        # Send the result (prepared by control) back to the user
        await ctx.send(result)
