import psycopg2 as psql

from src.classes.Database.DatabaseController import DatabaseController

class UsersController(DatabaseController):
    def get_users(self) -> list:
        self.cursor.execute(
            '''
            SELECT get_users()            
            '''
        )
        return self.cursor.fetchall()
    
    def add_user(self, user_login: str, user_password: str, user_email: str):
        try:
            self.cursor.execute(
                '''
                SELECT add_user(%s, %s, %s)
                ''', (user_login, user_password, user_email)
            )
            self.connection.commit()
        except psql.errors.UniqueViolation:
            print("Ошибка! Пользователь с такими данными уже существует!")
            self.connection.rollback()
            
    def is_admin(self, user_id: int) -> bool:
        self.cursor.execute(
            '''
            SELECT check_is_admin(%s)
            ''', (user_id, )
        )
        return self.cursor.fetchone()[0]
    
    def make_admin(self, user_id: int):
        try:
            self.cursor.execute(
                '''
                SELECT add_admin(%s)
                ''', (user_id, )
            )
            self.connection.commit()
        except psql.errors.UniqueViolation:
            print("Ошибка! Невозможно данного пользователя превратить в админа!")
            self.connection.rollback()
        except psql.errors.ForeignKeyViolation:
            print("Ошибка! Такой пользователь не существует!")
            self.connection.rollback()