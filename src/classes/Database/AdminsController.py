from src.classes.database.DatabaseController import DatabaseController

class AdminsController:
    @staticmethod
    def add_admin(user_id: int) -> None:
        query = '''SELECT add_admin(%s)'''
        args = [user_id]
        DatabaseController().execute_query(query=query, args=args)
        
    @staticmethod
    def remove_admin(user_id: int) -> None:
        query = '''SELECT remove_admin(%s)'''
        args = [user_id]
        DatabaseController().execute_query(query=query, args=args)
        
    @staticmethod
    def get_admins(reversed: bool=False) -> list:
        query = '''SELECT * FROM get_admins(%s)'''
        args = [reversed]
        result = DatabaseController().execute_query(query=query, args=args)
        return result