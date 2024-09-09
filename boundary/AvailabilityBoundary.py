from control.AvailabilityControl import AvailabilityControl

class AvailabilityBoundary:
    def __init__(self):
        self.control = AvailabilityControl()

    async def check_availability(self, ctx, url, date_str=None, time_slot=None):
        result = await self.control.handle_availability_check(ctx, url, date_str, time_slot)
        await ctx.send(result)
