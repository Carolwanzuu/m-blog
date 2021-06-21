from . import db
from datetime import datetime

# class User:
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Blog:
    __tablename = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    blog_content = db.Column(db.String(255))
    author = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'blog',lazy = 'dynamic')



