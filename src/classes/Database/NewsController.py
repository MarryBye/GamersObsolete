from src.classes.database.DatabaseController import DatabaseController

class NewsController:
    @staticmethod
    def add_news(user_id: int, news_title: str, news_description: str) -> None:
        query = '''SELECT add_news(%s, %s, %s)'''
        args = [user_id, news_title, news_description]
        result = DatabaseController().execute_query(query=query, args=args)
        return result
    
    @staticmethod
    def get_news(reversed: bool=False) -> list:
        query = '''SELECT * FROM get_news(%s)'''
        args = [reversed]
        result = DatabaseController().execute_query(query=query, args=args)
        return result
    
    @staticmethod
    def remove_news(news_id: int, user_id: int) -> None:
        query = '''SELECT remove_news(%s, %s)'''
        args = [news_id, user_id]
        DatabaseController().execute_query(query=query, args=args)
    
    @staticmethod
    def add_comment(news_id: int, user_id: int, comment_text: str) -> None:
        query = '''SELECT add_comment(%s, %s, %s)'''
        args = [news_id, user_id, comment_text]
        DatabaseController().execute_query(query=query, args=args)
        
    @staticmethod
    def get_comments(news_id: int, reversed: bool=False) -> list:
        query = '''SELECT * FROM get_comments(%s)'''
        args = [news_id, reversed]
        result = DatabaseController().execute_query(query=query, args=args)
        return result
    
    @staticmethod
    def remove_comment(comment_id: int, user_id: int) -> None:
        query = '''SELECT remove_comment(%s, %s)'''
        args = [comment_id, user_id]
        DatabaseController().execute_query(query=query, args=args)