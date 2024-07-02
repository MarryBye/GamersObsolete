from src.classes.database.DatabaseController import DatabaseController

class ServersController:
    @staticmethod
    def add_server(server_name: str, server_version: str, server_description: str, server_ip: str, server_port: str, user_id: int) -> None:
        query = '''SELECT add_server(%s, %s, %s, %s, %s, %s)'''
        args = [server_name, server_version, server_description, server_ip, server_port, user_id]
        DatabaseController().execute_query(query=query, args=args)
        
    @staticmethod
    def remove_server(server_id: int, user_id: int) -> None:
        query = '''SELECT remove_server(%s, %s)'''
        args = [server_id, user_id]
        DatabaseController().execute_query(query=query, args=args)
        
    @staticmethod
    def get_servers(reversed: bool=False) -> list:
        query = '''SELECT * FROM get_servers(%s)'''
        args = [reversed]
        result = DatabaseController().execute_query(query=query, args=args)
        return result