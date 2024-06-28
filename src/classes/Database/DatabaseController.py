import psycopg2 as psql
import json

from src.classes.Singleton import Singleton

class DatabaseController(metaclass=Singleton):
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def connect(self):
        try:
            with open("config.json", encoding="UTF-8") as config_file:
                self.connection = psql.connect(
                    **json.load(config_file)["database"]
                )
                self.cursor = self.connection.cursor()
        except (psql.Error, IOError, UnicodeDecodeError) as e:
            print(f"Возникла ошибка при подключении к базе данных!\nПричина: {e}")
            
    def disconnect(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
        except psql.Error as e:
            print(f"Возникла ошибка при отключении от базы данных!\nПричина: {e}")
            
    def execute_query(self, query: str, args: list=None):
        try:
            self.connect()
            self.cursor.execute(query, args)
            self.connection.commit()
        except psql.Error as e:
            print(f"Возникла ошибка при выполнении запроса!\nПричина: {e}")
            self.connection.rollback()
        finally:
            self.disconnect()