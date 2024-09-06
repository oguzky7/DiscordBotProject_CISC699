class HelpText:
    @staticmethod
    def get_help():
        return """
        Here are the commands you can use in this bot:

        1. **!project_help**
           Description: Provides a list of available commands the user can issue.
           Objects Involved: HelpBoundary, HelpControl.

        2. **!chat_with_bot**
           Description: Responds to simple greetings (e.g., "hi", "hello") and provides a welcome message.
           Objects Involved: ChatBoundary, ChatControl.

        3. **!login_to_website**
           Description: Logs into a website using stored credentials (e.g., BestBuy).
           Objects Involved: LoginBoundary, LoginControl, BrowserControl, NavigationControl, AccountEntity.

        4. **!launch_browser**
           Description: Launches the browser, optionally in incognito mode.
           Objects Involved: BrowserBoundary, BrowserControl, BrowserEntity.

        5. **!close_browser**
           Description: Closes the currently open browser session.
           Objects Involved: CloseBrowserBoundary, CloseBrowserControl, BrowserEntity.

        6. **!navigate_to_website**
           Description: Navigates to a specific website URL in the browser.
           Objects Involved: NavigationBoundary, NavigationControl, BrowserEntity.

        7. **!track_price**
           Description: Tracks the price of a product over time and sends notifications if the price changes.
           Objects Involved: ProductTrackingBoundary, ProductTrackingControl, ProductControl, NotificationControl, ProductEntity, TrackingHistoryEntity, NotificationEntity.

        8. **!check_price**
           Description: Manually checks the current price of a product.
           Objects Involved: ProductBoundary, ProductControl, ProductEntity.

        9. **!check_availability**
           Description: Checks the availability of a product or service on a specific date.
           Objects Involved: AvailabilityBoundary, AvailabilityControl, DateEntity.

        10. **!stop_tracking**
            Description: Stops tracking the price or availability of a product.
            Objects Involved: StopTrackingBoundary, StopTrackingControl, TrackingHistoryEntity.

        11. **!receive_notifications**
            Description: Sends notifications when there’s a change in price or availability for tracked products/services.
            Objects Involved: NotificationBoundary, NotificationControl, NotificationEntity, TrackingHistoryEntity.

        12. **!extract_data**
            Description: Extracts the tracked product data and exports it to Excel or HTML format.
            Objects Involved: DataExtractionBoundary, DataExtractionControl, TrackingHistoryEntity, ExcelUtils, HTMLUtils.

        13. **!stop**
            Description: Stops the Discord bot from running.
            Objects Involved: StopBoundary, BotControl.
        """
