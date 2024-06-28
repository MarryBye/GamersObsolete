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
            print("Ошибка! Не получилось подключиться к базе данных!")
            
    def disconnect(self):
        try:
            self.cursor.close()
            self.connection.close()
        except:
            print("Ошибка! Не получилось отключиться от базы данных!")