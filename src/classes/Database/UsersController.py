import psycopg2 as psql

from src.classes.Database.DatabaseController import DatabaseController

class UsersController():
    @staticmethod
    def get_users() -> list:
        DatabaseController().cursor.execute(
            '''
            SELECT get_users()            
            '''
        )
        return DatabaseController().cursor.fetchall()
    
    def add_user(user_login: str, user_password: str, user_email: str):
        try:
            DatabaseController().cursor.execute(
                '''
                SELECT add_user(%s, %s, %s)
                ''', (user_login, user_password, user_email)
            )
            DatabaseController().connection.commit()
        except psql.errors.UniqueViolation:
            print("Ошибка! Пользователь с такими данными уже существует!")
            DatabaseController().connection.rollback()
            
    def is_admin(user_id: int) -> bool:
        DatabaseController().cursor.execute(
            '''
            SELECT check_is_admin(%s)
            ''', (user_id, )
        )
        return DatabaseController().cursor.fetchone()[0]
    
    def make_admin(user_id: int):
        try:
            DatabaseController().cursor.execute(
                '''
                SELECT add_admin(%s)
                ''', (user_id, )
            )
            DatabaseController().connection.commit()
        except psql.errors.UniqueViolation:
            print("Ошибка! Невозможно данного пользователя превратить в админа!")
            DatabaseController().connection.rollback()
        except psql.errors.ForeignKeyViolation:
            print("Ошибка! Такой пользователь не существует!")
            DatabaseController().connection.rollback()