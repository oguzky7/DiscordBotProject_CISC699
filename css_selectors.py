class Selectors:
    SELECTORS = {
        "trendyol": {
            "price": ".featured-prices .prc-dsc"  # Selector for Trendyol price
        },
        "bestbuy": {
            "url": "https://www.bestbuy.com/signin/",
            "email_field": "#fld-e",
            #"continue_button": ".cia-form__controls  button",
            "password_field": "#fld-p1",
            "SignIn_button": ".cia-form__controls  button",
            "price": "[data-testid='customer-price'] span",  # CSS selector for BestBuy price
            "homePage": ".v-p-right-xxs.line-clamp"
        },
        "opentable": {
            "url": "https://www.opentable.com/",
            "date_field": "#restProfileSideBarDtpDayPicker-label", 
            "time_field": "#restProfileSideBartimePickerDtpPicker",  
            #"find_table_button": ".find-table-button",  # Example selector for the Find Table button
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
