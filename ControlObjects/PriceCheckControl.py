class PriceCheckControl:
    """
    Manages the process of checking product prices.
    """

    def __init__(self, products):
        # Initialize with a list of products and set the current price to None
        self.__current_price = None
        self.__products = products  # List of Product objects

    def check_price(self, product_url):
        """
        Check the price of the product at the provided URL.
        Returns the price if found, otherwise raises an exception.
        """
        for product in self.__products:
            if product.get_url() == product_url:
                self.__current_price = self.fetch_price_from_url(product_url)
                print(f"Price checked: {self.__current_price} for URL: {product_url}")
                return self.__current_price
        raise ValueError(f"Product not found for URL: {product_url}")

    def fetch_price_from_url(self, product_url):
        """
        Simulates fetching the price from a URL. In a real scenario, this would involve web scraping.
        """
        # Placeholder logic for price fetching
        return 123.45  # Example price

    def get_current_price(self):
        """
        Return the current price of the product.
        """
        return self.__current_price
