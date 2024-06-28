from src.classes.Database.DatabaseController import DatabaseController

class UsersController:
    @staticmethod
    def get_users() -> list:
        query = '''SELECT get_users()'''
        result = DatabaseController().execute_query(query=query)
        return result
    
    @staticmethod
    def add_user(user_login: str, user_password: str, user_email: str):
        query = '''SELECT add_user(%s, %s, %s)'''
        args = [user_login, user_password, user_email]
        DatabaseController().execute_query(query=query, args=args)
            
    @staticmethod   
    def is_admin(user_id: int) -> bool:
        query = '''SELECT check_is_admin(%s)'''
        args = [user_id]
        result = DatabaseController().execute_query(query=query, args=args, fetch_results=1)
        return result[0]
    
    @staticmethod
    def make_admin(user_id: int):
        query = '''SELECT add_admin(%s)'''
        args = [user_id]
        DatabaseController().execute_query(query=query, args=args)