class AvailabilityCheckControl:
    """
    Manages the process of checking the availability of dates.
    """

    def __init__(self, dates):
        # Initialize with a list of dates and set the initial availability status to False
        self.__availability_status = False
        self.__dates = dates  # List of Date objects

    def check_availability(self, date):
        """
        Check the availability of the provided date.
        Returns True if the date is available, otherwise False.
        """
        if date in self.__dates:
            self.__availability_status = True
            print(f"Date {date} is available.")
            return True
        else:
            print(f"Date {date} is not available.")
            return False
