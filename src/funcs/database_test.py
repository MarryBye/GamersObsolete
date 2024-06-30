from random import choice

from src.classes.Database.UsersController import UsersController
from src.classes.Database.NewsController import NewsController

def database_test():
    
    # Добавление пользователей в БД
    
    for i in range(10):
        UsersController.add_user(f"User{i}", user_password=f"{str(i)*10}", user_email=f"user{i}@mail.com")
        
    UsersController.add_user(f"User1", user_password=f"{str(i)*10}", user_email=f"user{i}@mail.com")
    UsersController.add_user(f"User{i}", user_password=f"{str(i)*10}", user_email=f"user2@mail.com")
    
    all_users = UsersController.get_users()
    print(all_users)
    
    if len(all_users) > 10:
        return False
    
    # Добавление администраторов
    
    for i in range(2):
        UsersController.make_admin(user_id=choice(all_users)[0])
        
    UsersController.make_admin(user_id=999999)
    
    # Добавление новостей
    
    for user in all_users:
        NewsController.add_news(user_id=user[0], news_title=f"News by user{user[0]}", news_description="News description")
        
    if len(NewsController.get_news()) > 2:
        return False
    
    # Добавление комментариев
    
    all_news = NewsController.get_news()
    
    for news in all_news:
        user = choice(all_users)[0]
        NewsController.add_comment(news_id=news[0], user_id=user, comment_text=f"Aboba written by {user}")
    
    for news in all_news:
        print(NewsController.get_comments(news_id=news[0]))
    
    return True 
        
        