from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from views import views

app = Flask(__name__)
app.register_blueprint(views, url_prefix="/")

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.debug = True

db = SQLAlchemy(app)

if __name__ == '__main__':
    db.create_all()
    app.run()
    
