import psycopg2 as psql

from src.classes.Singleton import Singleton

class DatabaseController(metaclass=Singleton):
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def connect(self, **kwargs):
        try:
            self.connection = psql.connect(
                **kwargs
            )
            self.cursor = self.connection.cursor()
        except:
            print("Error while connection to database!")
            
    def disconnect(self):
        try:
            self.connection.close()
            self.cursor.close()
        except:
            print("Error while disconnecting from database!")