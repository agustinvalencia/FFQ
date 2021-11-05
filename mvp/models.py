from app import db

class users(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column("name", db.String(128))
    email = db.Column("email", db.String(128))

    def __init__(self, name, email):
        self.name = name
        self.email = email