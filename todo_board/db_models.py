from todo_board import db

class TODO(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text, nullable=False)
    priority = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)