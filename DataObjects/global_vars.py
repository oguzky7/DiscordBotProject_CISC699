import re

class GlobalState:
    user_message = 'default'

    @classmethod
    def reset_user_message(cls):
        """Reset the global user_message variable to None."""
        cls.user_message = None

    @classmethod
    def parse_user_message(cls, message):
        """
        Parses a user message by splitting it into command and up to 6 variables.
        Handles quoted substrings so that quoted parts (e.g., "October 2") remain intact.
        """
        print(f"User_message before parsing: {message}")
        message = message.replace("!", "").strip()  # Remove "!" and strip spaces
        #print(f"User_message after replacing '!' with empty string: {message}")

        # Simple split by spaces, keeping quoted substrings intact
        parts = re.findall(r'\"[^\"]+\"|\S+', message)
        #print(f"Parts after splitting: {parts}")

         # Ensure we always return 6 variables (command + 5 parts), even if some are empty
        result = [parts[i].strip('"') if len(parts) > i else "" for i in range(6)]  # List comprehension to handle missing parts
        
        #print(f"Result: {result}")
        return result  # Return the list (or tuple if needed)
