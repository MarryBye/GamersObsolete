import psycopg2 as psql

from src.classes.Database.DatabaseController import DatabaseController
from src.classes.Database.UsersController import UsersController

UsersController().connect(
    host="localhost",
    port="5432",
    database="gmrs_site",
    user="postgres",
    password="58231"
)

print(UsersController().get_users())

UsersController().add_user(
    user_login="Aboba_112333", 
    user_password="83287YEUIWHF8787343h8",
    user_email="abob2@gmail.com"
)

print(UsersController().get_users())

print(UsersController().is_admin(user_id=1))

UsersController().make_admin(user_id=5)
UsersController().make_admin(user_id=6)
UsersController().make_admin(user_id=8)
UsersController().make_admin(user_id=1)
print(UsersController().is_admin(user_id=5))