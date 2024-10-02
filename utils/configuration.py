import json

#class configuration:
def load_config():
    """Loads the configuration file and returns the settings."""
    try:
        with open('config.json', 'r') as config_file:
            config_data = json.load(config_file)
            return config_data
    except FileNotFoundError:
        print("Configuration file not found. Using default settings.")
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the format of your config.json file.")
        return {}
