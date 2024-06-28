import psycopg2 as psql
import json

from src.classes.Singleton import Singleton

class DatabaseController(metaclass=Singleton):
    def __init__(self):
        self.connection = None
        
    def connect(self):
        try:
            with open("config.json", encoding="UTF-8") as config_file:
                config = json.load(config_file)["database"]
                self.connection = psql.connect(**config)
        except (psql.Error, IOError, UnicodeDecodeError) as e:
            print(f"Возникла ошибка при подключении к базе данных!\nПричина: {e}")
            
    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
        except psql.Error as e:
            print(f"Возникла ошибка при отключении от базы данных!\nПричина: {e}")
            
    def execute_query(self, query: str, args: list=None):
        try:
            self.connect()
            with self.connection, self.connection.cursor() as cursor:
                cursor.execute(query, args)
                self.connection.commit()
        except psql.errors.ForeignKeyViolation:
            print("Возникла ошибка при выполнении запроса!\nСделано обращение к несуществующему ключу!")
            self.connection.rollback()
        except psql.errors.UniqueViolation:
            print("Возникла ошибка при выполнении запроса!\nПовторяется одно из уникальных значений!")
            self.connection.rollback()
        except psql.Error as e:
            print(f"Возникла ошибка при выполнении запроса!\nПричина: {e}")
            self.connection.rollback()
        finally:
            self.disconnect()