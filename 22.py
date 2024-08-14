class Log:
    def __init__(self, log_file):
        self.log_file = log_file

    def write_error(self, message):
        with open(self.log_file, 'a') as file:
            file.write(f"ERROR: {message}\n")


log = Log('error_log.txt')
log.write_error('This is an error message.')
