class NotificationControl:
    """
    Manages notifications for users.
    """

    def __init__(self):
        # Initialize with an empty list of notifications
        self.__notifications = []

    def send_notification(self, notification):
        """
        Send a notification to the user and add it to the list of notifications.
        """
        if notification:
            self.__notifications.append(notification)
            print(f"Notification sent: {notification.get_content()}")
        else:
            raise ValueError("Notification cannot be null.")

    def get_notifications(self):
        """
        Return the list of sent notifications.
        """
        return self.__notifications
