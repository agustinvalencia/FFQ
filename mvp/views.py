from flask import Blueprint
from flask import render_template, redirect, request
from flask.helpers import url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/get-question")
def get_question():
    return render_template("get-question.html")

@views.route("/post-question", methods=['GET', 'POST'])
def post_question():
    return render_template('post-question.html')

@views.route("/thanks", methods=['POST'])
def thanks():
    author = request.form.get('author')
    question = request.form.get('question')
    return render_template('thanks.html',
                            author=author,
                            question=question)

@views.route("/history")
def history():
    return render_template("history.html")