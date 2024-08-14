class Report:
    def __init__(self, file_name):
        self.file_name = file_name
        self.data = []
        self.load_data()

    def load_data(self):
        try:
            with open(self.file_name, 'r') as file:
                for line in file:
                    # Assuming each line contains data that needs processing
                    self.data.append(line.strip())
            print(f"Data loaded from file: {self.file_name}")
        except FileNotFoundError:
            print(f"File '{self.file_name}' not found.")
        except IOError as e:
            print(f"Error reading file '{self.file_name}': {e}")

    def generate_report(self):
        if not self.data:
            print("No data to generate report.")
            return
        
        print("Generating report...")
        for line in self.data:
            # Example of processing each line of data
            print(f"Report line: {line}")

# Example usage:
report = Report('data.txt')

# Generate report
report.generate_report()
