import os

from flask import Flask, request, render_template, redirect, url_for

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
    return render_template("home.html", page_name="Главная")

app.run()