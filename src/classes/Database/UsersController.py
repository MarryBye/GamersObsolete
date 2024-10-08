from src.classes.database.DatabaseController import DatabaseController

class UsersController:
    @staticmethod
    def get_users(reversed: bool=False) -> list:
        query = '''SELECT * FROM get_users(%s)'''
        args = [reversed]
        result = DatabaseController().execute_query(query=query, args=args)
        return result
    
    @staticmethod
    def add_user(user_login: str, user_password: str, user_email: str) -> None:
        query = '''SELECT add_user(%s, %s, %s)'''
        args = [user_login, user_password, user_email]
        DatabaseController().execute_query(query=query, args=args)
            
    @staticmethod   
    def is_admin(user_id: int) -> bool:
        query = '''SELECT check_is_admin(%s)'''
        args = [user_id]
        result = DatabaseController().execute_query(query=query, args=args, fetch_results=1)
        return result[0]