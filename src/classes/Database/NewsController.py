from src.classes.Database.DatabaseController import DatabaseController

class NewsController:
    @staticmethod
    def add_news(user_id: int, news_title: str, news_description: str):
        query = '''SELECT add_news(%s, %s, %s)'''
        args = [user_id, news_title, news_description]
        result = DatabaseController().execute_query(query=query, args=args)
        return result
    
    @staticmethod
    def get_news():
        query = '''SELECT get_news()'''
        result = DatabaseController().execute_query(query=query)
        return result
    
    @staticmethod
    def add_comment(news_id: int, user_id: int, comment_text: str):
        query = '''SELECT add_comment(%s, %s, %s)'''
        args = [news_id, user_id, comment_text]
        DatabaseController().execute_query(query=query, args=args)