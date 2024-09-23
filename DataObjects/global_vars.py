# global_vars.py

class GlobalState:
    user_message = None

    @classmethod
    def reset_user_message(cls):
        """Reset the global user_message variable to None."""
        cls.user_message = None
