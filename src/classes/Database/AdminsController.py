from src.classes.Database.DatabaseController import DatabaseController

class AdminsController:
    @staticmethod
    def add_admin(user_id: int):
        query = '''SELECT add_admin(%s)'''
        args = [user_id]
        DatabaseController().execute_query(query=query, args=args)
        
    @staticmethod
    def remove_admin(user_id: int):
        query = '''SELECT remove_admin(%s)'''
        args = [user_id]
        DatabaseController().execute_query(query=query, args=args)