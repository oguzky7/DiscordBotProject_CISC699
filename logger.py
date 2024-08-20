import logging

# Configure the logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

def log(message):
    """
    Log a general message.
    """
    logging.info(message)

def log_message_received(message):
    """
    Log when a message is received.
    """
    logging.info(f"Message received: {message.content} from {message.author}")

def log_message_recognized():
    """
    Log when a message is recognized as a valid command.
    """
    logging.info("Message recognized as a command.")

def log_message_not_recognized():
    """
    Log when a message is not recognized as a valid command.
    """
    logging.info("Message not recognized.")

def log_command_execution(command_name, user):
    """
    Log the execution of a command.
    """
    logging.info(f"Executing command: {command_name} from '{user}'")

def log_command_failed(command_name, error):
    """
    Log when a command fails.
    """
    logging.error(f"Failed to execute command: {command_name}. Error: {error}")

def log_wrong_channel(command_name, user):
    """
    Log when a command is used in the wrong channel.
    """
    logging.warning(f"User '{user}' tried to execute command '{command_name}' in a non-designated channel.")
