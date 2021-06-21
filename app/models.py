from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


# class User:
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

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



