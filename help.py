def get_help_message():
    """
    Returns a detailed help message listing all available commands and their usage.
    """

    help_message = (
        "Here are the available commands:\n\n"
        "**!launch_browser [incognito]**\n"
        "Launches the Chrome browser. Optionally, you can include 'incognito' to launch the browser in incognito mode.\n"
        "Example: `!launch_browser incognito` or `!launch_browser`\n\n"
        
        "**!navigate_to_url <url> [incognito]**\n"
        "Navigates to the specified URL in the browser. The browser must be launched first. "
        "You can also include 'incognito' to perform the navigation in incognito mode.\n"
        "Example: `!navigate_to_url https://www.google.com incognito` or `!navigate_to_url https://www.google.com`\n\n"
        
        "**!get_price <url> [incognito]**\n"
        "Fetches the price from the specified URL. The browser must be launched and the URL must match a supported website with known selectors. "
        "You can also include 'incognito' to fetch the price in incognito mode.\n"
        "Example: `!get_price URL incognito` or `!get_price URL`\n\n"
        
        "**!login <url> [incognito]**\n"
        "Logs into the specified website using the stored credentials in the account configuration. "
        "You can include 'incognito' to perform the login in incognito mode.\n"
        "Example: `!login URL incognito` or `!login URL`\n\n"
        
        "**!close_browser**\n"
        "Closes the browser if it is currently open.\n"
        "Example: `!close_browser`\n\n"
        
        "**!commands**\n"
        "Lists all available commands. This is the command you are using now.\n\n"
        
        "**!stop**\n"
        "Stops the bot and terminates the session.\n"
        "Example: `!stop`\n\n"
    )

    return help_message
