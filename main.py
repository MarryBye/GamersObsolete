from src.funcs.database_test import database_test

from src.classes.Database.AdminsController import AdminsController
from src.classes.Database.NewsController import NewsController
from src.classes.Database.UsersController import UsersController

database_test()

print(NewsController.get_news())
print(NewsController.get_comments(news_id=1))

NewsController.remove_comment(comment_id=1, user_id=1)
NewsController.remove_news(news_id=1, user_id=1)

print(NewsController.get_news())
print(NewsController.get_comments(news_id=1))