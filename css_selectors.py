class Selectors:
    SELECTORS = {
        "trendyol": {
            "price": ".featured-prices .prc-dsc"  # Selector for Trendyol price
        },
        "shein": {
            #input[aria-label*='Password:'][type='password'][class='sui-input__inner sui-input__inner-suffix']
            "url": "https://www.shein.com/user/auth/login",
            "email_field": "[aria-label*='Email Address:']",
            "continue_button": ".login-point_button .page__login_mainButton",
            "password_field": "[aria-label*='Password:']",
            "login_button": "span[data-v-0d926f8f]",
            "price": ".from.original span"  # CSS selector for Shein price
        }
    }

    @staticmethod
    def get_selectors_for_url(url):
        for keyword, selectors in Selectors.SELECTORS.items():
            if keyword in url.lower():
                return selectors
        return None  # Return None if no matching selectors are found
    