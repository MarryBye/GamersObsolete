import os

from flask import Flask, request, render_template, redirect, url_for
from src.funcs.database_test import database_test

from src.classes.database.ServersController import ServersController

# database_test()

PATH_TO_WEB = os.path.join("src", "web")
TEMPLATES = os.path.join(PATH_TO_WEB, "templates")
STATIC = os.path.join(PATH_TO_WEB, "static")

app = Flask(
    import_name=__name__, 
    template_folder=TEMPLATES,
    static_folder=STATIC,
)

app.secret_key = "SecretKey"

@app.route("/")
def index():
    servers = ServersController.get_servers()
    return render_template("index.html", page_name="Главная", servers=servers)

@app.route("/news")
def news():
    return render_template("news.html", page_name="Новости")

@app.route("/servers")
def servers():
    return render_template("servers.html", page_name="Сервера")

@app.route("/forum")
def forum():
    return render_template("forum.html", page_name="Форум")

@app.route("/contacts")
def contacts():
    return render_template("contacts.html", page_name="Контакты")

@app.route("/login")
def login():
    return render_template("login.html", page_name="Вход")

@app.route("/register")
def register():
    return render_template("register.html", page_name="Регистрация")

@app.route("/admin")
def admin():
    return render_template("admin.html", page_name="Админ-панель")

app.run()