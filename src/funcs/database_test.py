from src.classes.database.UsersController import UsersController
from src.classes.database.NewsController import NewsController
from src.classes.database.AdminsController import AdminsController
from src.classes.database.ServersController import ServersController

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
        
    for i, user in enumerate(UsersController.get_users(), 1):
        ServersController.add_server(
            server_name=f"Server #{i}",
            server_version=f"1.2{i}.{i - 1}",
            server_description=f"Информация про сервер #{i}",
            server_ip=f"177.{i}{i+1}.185.{i-1}",
            server_port=f"{i}{i}{i}{i}{i}",
            user_id=user[0]
        )
        