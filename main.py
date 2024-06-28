from src.classes.Database.UsersController import UsersController
from src.classes.Database.NewsController import NewsController

#UsersController.add_user(user_login="Aboba", user_password="3RtyH&hui3", user_email="aboba@gmail.com")

print(UsersController.get_users())
print(UsersController.is_admin(1))

NewsController.add_news(user_id=1, news_title="Абобы атакуют", news_description="Абобы вчера вечером атаковали пиздец как сильно мы все в ахуях сидели, но справились, это пиздец просто ребята я ахуел нахуй блять это ебать его в рот бляяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяяять.")

#UsersController.make_admin(user_id=1)

print(NewsController.get_news())