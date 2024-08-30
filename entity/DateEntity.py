class DateEntity:
    def __init__(self, date_str=None, time_slot=None):
        self.date_str = date_str
        self.time_slot = time_slot

    def update_date(self, new_date_str):
        self.date_str = new_date_str

    def update_time_slot(self, new_time_slot):
        self.time_slot = new_time_slot
