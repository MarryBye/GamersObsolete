from src.classes.Database.UsersController import UsersController


UsersController.add_user(user_login="abo2b", user_password="log2323", user_email="abobbbbb@gmail.com")
print(UsersController.get_users())
print(UsersController.is_admin(55))
UsersController.make_admin(user_id=1)
print(UsersController.is_admin(1))