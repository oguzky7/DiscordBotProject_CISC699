from datetime import datetime

class ProductEntity:
    def __init__(self, product_id=None, name=None, price=None):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.timestamp = None

    def update_price(self, new_price):
        self.price = new_price
        self.timestamp = datetime.now()
        return self.price

    def get_timestamp(self):
        return self.timestamp
