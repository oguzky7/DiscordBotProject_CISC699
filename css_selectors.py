class Selectors:
    SELECTORS = {
        "trendyol": {
            "price": ".featured-prices .prc-dsc"  # Selector for Trendyol price
        },
        "shein": {
            "url": "https://www.shein.com/user/auth/login",
            "email_field": "[aria-label*='Email Address:']",
            "continue_button": ".login-point_button .page__login_mainButton",
            "password_field": "[aria-label*='Password:']",
            "login_button": "span[data-v-0d926f8f]",
            "price": ".from.original span"  # CSS selector for Shein price
        },
        "opentable": {
            "url": "https://www.opentable.com/",
            "date_field": "#restProfileSideBarDtpDayPicker-label", 
            "time_field": "#restProfileSideBartimePickerDtpPicker",  
            "find_table_button": ".find-table-button",  # Example selector for the Find Table button
            "availability_result": ".availability-result",  # Example selector for availability results
            "show_next_available_button": "button[data-test='multi-day-availability-button']",  # Show next available button
            "available_dates": "ul[data-test='time-slots'] > li",  # Available dates and times
            "no_availability": "div._8ye6OVzeOuU- span"
        }
    }

    @staticmethod
    def get_selectors_for_url(url):
        for keyword, selectors in Selectors.SELECTORS.items():
            if keyword in url.lower():
                return selectors
        return None  # Return None if no matching selectors are found
