from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-question")
def get_question():
    return render_template("get-question.html")

@app.route("/post-question")
def post_question():
    return render_template("post-question.html")

@app.route("/who-am-i")
def who_am_i():
    return render_template("who-am-i.html")

if __name__ == '__main__':
    app.run()
    
