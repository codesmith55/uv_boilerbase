from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(50), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    typeDetails = db.Column(db.String(50), nullable=False)