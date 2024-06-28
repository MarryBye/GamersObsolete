import psycopg2 as psql

from src.classes.Database.DatabaseController import DatabaseController
from src.classes.Database.UsersController import UsersController

DatabaseController().connect(
    host="localhost",
    port="5432",
    database="gmrs_site",
    user="postgres",
    password="58231"
)

UsersController.add_user(user_login="abob", user_password="log2323", user_email="abobbbbb@gmail.com")
print(UsersController.get_users())
print(UsersController.is_admin(2))
UsersController.make_admin(user_id=55)
print(UsersController.is_admin(1))