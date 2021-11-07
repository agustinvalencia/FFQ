from flask import Blueprint
from flask import render_template, redirect, request
from flask.helpers import url_for
from models import Question, db

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/get-question")
def get_question():
    return render_template("get-question.html")

@views.route("/post-question", methods=['GET', 'POST'])
def post_question():
    if request.method == 'POST':
        # receiving a question
        new_question = Question(author=request.form.get('author'),
                                text=request.form.get('question'))
        # Push to DB
        try:
            db.session.add(new_question)
            db.session.commit()
            return redirect('/post-question')
        except:
            return "There was a problem with your question"
    else:
        # normal landing
        return render_template('post-question.html')

@views.route("/thanks", methods=['POST'])
def thanks():
    author = request.form.get('author')
    question = request.form.get('question')
    return render_template('thanks.html',
                            author=author,
                            question=question)

@views.route("/history", methods=['GET'])
def history():
    questions = Question.query.order_by(Question.date_created)
    return render_template("history.html", questions=questions)