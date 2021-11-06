from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap

from views import views

db_name = 'tmp/test.db'
app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")
app.config['SECRET_KEY'] = 'testpass'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.debug = True

db = SQLAlchemy(app)
# Bootstrap(app)

if __name__ == '__main__':
    # db.create_all()
    app.run()
    
