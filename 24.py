import sqlite3

class Database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            print(f"Connected to database: {self.db_file}")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected from database.")

    def execute_query(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def fetch_all(self):
        return self.cursor.fetchall()

    def fetch_one(self):
        return self.cursor.fetchone()

# Example usage:
db = Database('example.db')

# Execute a query
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);
"""
db.execute_query(create_table_query)

# Insert data
insert_query = "INSERT INTO users (name, age) VALUES ('Alice', 30)"
db.execute_query(insert_query)

# Fetch data
select_query = "SELECT * FROM users"
db.execute_query(select_query)
rows = db.fetch_all()
for row in rows:
    print(row)

# Disconnect from the database
db.disconnect()
