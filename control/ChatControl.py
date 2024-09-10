
# ChatControl in control/ChatControl.py
class ChatControl:
    def process_non_prefixed_message(self, message):
        """Process non-prefixed messages like 'hi', 'hello'."""
        if message.lower() in ["hi", "hello"]:
            return "Hello! How can I assist you today? Type !project_help for assistance."
        else:
            return "I didn't recognize that. Type !project_help to see available commands."

    def handle_unrecognized_command(self):
        """Handle unrecognized command from on_command_error."""
        return "I didn't recognize that command. Type !project_help for assistance."