from flask import Blueprint
from flask import render_template

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/get-question")
def get_question():
    return render_template("get-question.html")

@views.route("/post-question")
def post_question():
    return render_template("post-question.html")

@views.route("/history")
def history():
    return render_template("history.html")