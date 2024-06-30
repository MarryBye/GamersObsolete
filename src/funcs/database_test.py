from src.classes.Database.UsersController import UsersController
from src.classes.Database.NewsController import NewsController
from src.classes.Database.AdminsController import AdminsController

def database_test():
    
    for i in range(10):
        UsersController.add_user(
            user_login=f"User{i}", 
            user_password=f"{str(i)*10}",
            user_email=f"aboba{i}@mail.com"
        )

    AdminsController.add_admin(user_id=1)
    AdminsController.add_admin(user_id=5)
    AdminsController.add_admin(user_id=10)

    for user in UsersController.get_users():
        NewsController.add_news(
            user_id=user[0],
            news_title=f"News by user{user[0]}",
            news_description="News description"
        )

    for user in UsersController.get_users():
        for news in NewsController.get_news():
            NewsController.add_comment(
                news_id=news[0],
                user_id=user[0],
                comment_text=f"Comment for news #{news[0]} by user{user[0]}"
            )
        
        