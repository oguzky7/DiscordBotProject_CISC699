import logger
from config import Config  # Import the configuration file to get credentials

class Account:
    """
    Represents a user account in the system.
    """

    def __init__(self):
        self.username = Config.USERNAME
        self.password = Config.PASSWORD
        self.email = Config.EMAIL  # Assuming email is also in config

    def update_password(self, new_password):
        """
        Update the account password.
        """
        self.password = new_password
        logger.log(f"Password updated for user {self.username}")

    def get_account_info(self):
        """
        Retrieve account information.
        """
        return {
            "username": self.username,
            "email": self.email,
        }

    def validate_credentials(self, input_password):
        """
        Validate the account credentials.
        """
        is_valid = self.password == input_password
        logger.log(f"Credentials validation for user {self.username}: {'Valid' if is_valid else 'Invalid'}")
        return is_valid
