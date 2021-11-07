from app import db
from datetime import datetime

class Question():
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    author = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Question {id}> {self.author}'