from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Quote:
   
    def __init__(self,id,quote,author):
        self.id =id
        self.quote = quote
        self.author = author
        
# class User:
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    blog = db.relationship('Blog', backref = 'users', lazy = 'dynamic')
    comment = db.relationship('Comment', backref = 'users', lazy = 'dynamic')
    pass_secure = db.Column(db.String(255))

    def save_user(self):
        db.session.add(self)
        db.session.commit()
    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

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

        

class Blog(db.Model):
    __tablename = 'blog'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    blog_content = db.Column(db.String(255))
    author = db.Column(db.String(255))
    posted = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'blog',lazy = 'dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()
    def delete_blog(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_blog(cls,user_id):
        blogs = Blog.query.filter_by(user_id=user_id).all()
        return Blog

    def __repr__(self):
       return f'Blog {self.name}'

class Comment(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    comment=db.Column(db.String)
    posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
    blog_id=db.Column(db.Integer,db.ForeignKey('blog.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()
    def delete_comment(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
       return f'Comment{self.comment}'
    @classmethod
    def get_comments(cls,id):
        comment=Comment.query.filter_by(blog_id=id).all()
        return comment

    



