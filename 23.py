class Config:
    def __init__(self, config_file):
        self.config_file = config_file
        self.settings = {}
        self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        key, value = line.split('=')
                        self.settings[key.strip()] = value.strip()
        except FileNotFoundError:
            print(f"Config file '{self.config_file}' not found.")
        except Exception as e:
            print(f"Error loading config file '{self.config_file}': {str(e)}")

    def get_setting(self, key):
        return self.settings.get(key)

    def set_setting(self, key, value):
        self.settings[key] = value

# Example usage:
config = Config('config.txt')

# Get a setting
server_address = config.get_setting('server_address')
if server_address:
    print(f"Server address: {server_address}")
else:
    print("Server address not found in config.")

# Set a setting
config.set_setting('port', '8080')

# Save the updated settings back to file (optional for this basic implementation)
# Not implemented in this basic example, but you could extend it to write back to file.