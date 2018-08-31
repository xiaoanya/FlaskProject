from .sqlconfig import db
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20))
    age = db.Column(db.Integer)
    score = db.Column(db.Float)
    sex = db.Column(db.String(5))