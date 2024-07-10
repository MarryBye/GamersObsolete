import os

from flask import Flask, request, render_template, redirect, url_for, session
from src.funcs.database_test import database_test

from src.classes.database.ServersController import ServersController
from src.classes.database.NewsController import NewsController
# прикол
# database_test()

PATH_TO_WEB = os.path.join("src", "web")
TEMPLATES = os.path.join(PATH_TO_WEB, "templates")
STATIC = os.path.join(PATH_TO_WEB, "static")

app = Flask(
    import_name=__name__, 
    template_folder=TEMPLATES,
    static_folder=STATIC,
)
app.permanent_session_lifetime = True


app.secret_key = "SecretKey"

@app.route("/")
def index():
    servers = ServersController.get_servers()
    last_news = NewsController.get_news(reversed=True)[0]
    return render_template(
        template_name_or_list="index.html", 
        page_name="Главная", 
        page_content={"servers": servers, "last_news": last_news}
    )

@app.route("/news")
def news():
    servers = ServersController.get_servers()
    news = NewsController.get_news(reversed=True)
    print(news)
    return render_template(
        template_name_or_list="news.html", 
        page_name="Новости", 
        page_content={"servers": servers, "last_news": news[0], "all_news": news}
    )

@app.route("/servers")
def servers():
    servers = ServersController.get_servers()
    last_news = NewsController.get_news(reversed=True)[0]
    return render_template(
        template_name_or_list="servers.html", 
        page_name="Сервера", 
        page_content={"servers": servers, "last_news": last_news}
    )

@app.route("/forum")
def forum():
    servers = ServersController.get_servers()
    last_news = NewsController.get_news(reversed=True)[0]
    return render_template(
        template_name_or_list="forum.html", 
        page_name="Форум", 
        page_content={"servers": servers, "last_news": last_news}
    )

@app.route("/contacts")
def contacts():
    servers = ServersController.get_servers()
    last_news = NewsController.get_news(reversed=True)[0]
    return render_template(
        template_name_or_list="contacts.html", 
        page_name="Контакты", 
        page_content={"servers": servers, "last_news": last_news}
    )

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