import psycopg2
from psycopg2 import OperationalError
from dotenv import load_dotenv
import os
from contextlib import contextmanager

class Connection():
    def __init__(self):
        load_dotenv() # Load environment variables from .env file
        # Retrieve database connection parameters from environment variables
        self.host = os.getenv("POSTGRESQL_HOST")
        self.port = os.getenv("POSTGRESQL_PORT")
        self.user = os.getenv("POSTGRESQL_USER")
        self.password = os.getenv("POSTGRESQL_PASSWORD")
        self.db = os.getenv("POSTGRESQL_DB")
        # Initialize connection and cursor to None
        self._connection = None
        self._cursor = None
    
    @property
    def connection(self):
        if not self._connection or self._connection.closed != 0:
            self.open_connection()
        return self._connection

    @property
    def cursor(self):
        if not self._cursor or self._connection.closed != 0:
            self.open_connection()
            self._cursor = self._connection.cursor()
        return self._cursor

    # Open a connection to the PostgreSQL database
    def open_connection(self):
        try:
            self._connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                dbname=self.db
            )
            if self._connection and self._connection.closed == 0:
                print(f'Connected to PostgreSQL.')
                self._cursor = self._connection.cursor() # Initialize cursor
                return True
            else:
                print('Failed to connect')
                return False
        except OperationalError as e:
            print(f"Error connecting to the database: {e}")
            return False
        
    # Close the database connection and cursor
    def close_connection(self):
        if self._cursor:
            self._cursor.close()
            print('Cursor has been closed')
        if self._connection and self._connection.closed == 0:
            self._connection.close()
            print('Connection has been closed')

    # Context manager to handle database transactions
    @contextmanager
    def get_cursor(self):
        try:
            yield self.cursor
            self.connection.commit()  # Commit any changes if needed
        except Exception as e:
            self.connection.rollback()  # Rollback in case of error
            print(f"An error occurred: {e}")
            raise e
        
_connection = Connection() # This is a singleton instance of the Connection class