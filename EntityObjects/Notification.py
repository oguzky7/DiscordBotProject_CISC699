class Notification:
    """
    Represents a notification sent to the user.
    """

    def __init__(self, notif_type, content, timestamp):
        # Initialize notification with type, content, and timestamp
        self.type = notif_type
        self.content = content
        self.timestamp = timestamp

    def get_type(self):
        # Return the type of the notification
        return self.type

    def get_content(self):
        # Return the notification content
        return self.content

    def get_timestamp(self):
        # Return when the notification was sent
        return self.timestamp

    def info_notification(self):
        # Print detailed information about the notification
        print(f"Notification Type: {self.type}")
        print(f"Content: {self.content}")
        print(f"Timestamp: {self.timestamp}")
