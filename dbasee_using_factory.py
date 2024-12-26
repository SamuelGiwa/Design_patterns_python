import sqlite3
import os

class DatabaseFactory:
    """Factory class to create, manage, and remove a SQLite database."""

    @staticmethod
    def create_database(db_name):
        """
        Factory method to create a SQLite database connection.
        
        Parameters:
            db_name (str): The name of the database file to create or connect to.
        
        Returns:
            sqlite3.Connection: The SQLite database connection object.
        """
        try:
            # Establish connection
            connection = sqlite3.connect(db_name)
            print(f"Database '{db_name}' created or connected successfully.")
            return connection
        except sqlite3.Error as e:
            print(f"Error creating database: {e}")
            return None

    @staticmethod
    def remove_database(db_name):
        """
        Removes the SQLite database file from the filesystem.
        
        Parameters:
            db_name (str): The name of the database file to delete.
        
        Returns:
            bool: True if the file was removed successfully, False otherwise.
        """
        try:
            if os.path.exists(db_name):
                os.remove(db_name)
                print(f"Database '{db_name}' removed successfully.")
                return True
            else:
                print(f"Database '{db_name}' does not exist.")
                return False
        except Exception as e:
            print(f"Error removing database: {e}")
            return False


# Example usage of the factory methods
if __name__ == "__main__":
    # Define database name
    db_name = "example_factory_method.db"
    
    # Create or connect to the database
    connection = DatabaseFactory.create_database(db_name)
    
    if connection:
        # Example: Create a table
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        print("Table 'users' created successfully.")
        
        # Close the connection
        connection.close()
        print("Database connection closed.")
    
    # Remove the database
    success = DatabaseFactory.remove_database(db_name)
    if success:
        print("Database has been successfully removed.")
