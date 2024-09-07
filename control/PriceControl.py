import asyncio
from entity.PriceEntity import PriceEntity
from Config import Config
import logging

class PriceControl:
    def __init__(self):
        self.price_entity = PriceEntity()
        self.logger = logging.getLogger("PriceControl")

    async def get_price(self, ctx, url):
        """Fetch the current price from the given URL."""
        if ctx.channel.id == Config.CHANNEL_ID:
            try:
                price = self.price_entity.get_price(url)
                if price:
                    return f"The current price is: {price}"
                else:
                    return "Failed to retrieve the price."
            except Exception as e:
                self.logger.error(f"Failed to get price for {url}: {e}")
                return f"Error getting price: {e}"
        else:
            return "This command can only be used in the designated channel."
