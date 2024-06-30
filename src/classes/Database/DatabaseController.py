import psycopg2 as psql
import json

from src.classes.Singleton import Singleton
from src.classes.Debug import Debug

class DatabaseController(metaclass=Singleton):
    def __init__(self):
        self.connection = None
        
    def connect(self):
        try:
            with open("config.json", encoding="UTF-8") as config_file:
                config = json.load(config_file)["database"]
                self.connection = psql.connect(**config)
                Debug.debug_print("Соединение с базой данных настроено!")
        except (psql.Error, IOError, UnicodeDecodeError) as e:
            Debug.debug_print(f"Возникла ошибка при подключении к базе данных!\nПричина: {Debug.TerminalColors.FAIL}{e}")
            
    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                Debug.debug_print("Соединение с базой данных закрыто!")
        except psql.Error as e:
            Debug.debug_print(f"Возникла ошибка при отключении от базы данных!\nПричина: {Debug.TerminalColors.FAIL}{e}")
            
    def execute_query(self, query: str, args: list=None, fetch_results: int=-1):
        try:
            self.connect()
            with self.connection, self.connection.cursor() as cursor:
                cursor.execute(query, args)
                result = cursor.fetchall() if fetch_results == -1 else cursor.fetchone() if fetch_results == 1 else cursor.fetchmany(fetch_results)
                self.connection.commit()
                Debug.debug_print("Запрос выполнен успешно!")
                return result
        except psql.errors.ForeignKeyViolation as e:
            Debug.debug_print(f"Возникла ошибка при выполнении запроса!\nПричина: {Debug.TerminalColors.FAIL}Сделано обращение к несуществующему ключу!\n{e}")
            self.connection.rollback()
        except psql.errors.UniqueViolation as e:
            Debug.debug_print(f"Возникла ошибка при выполнении запроса!\nПричина: {Debug.TerminalColors.FAIL}Повторяется одно из уникальных значений!\n{e}")
            self.connection.rollback()
        except psql.Error as e:
            Debug.debug_print(f"Возникла ошибка при выполнении запроса!\nПричина: {Debug.TerminalColors.FAIL}{e}")
            self.connection.rollback()
        finally:
            self.connection.close()