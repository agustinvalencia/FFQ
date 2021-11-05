from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

db = SQLAlchemy(app)

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String(128))
    email = db.Column("email", db.String(128))

    def __init__(self, name, email):
        self.name = name
        self.email = email


if __name__ == '__main__':
    db.create_all()
    app.run()
    
