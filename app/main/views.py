from flask import abort, redirect, render_template, request, url_for
from flask_login import login_required,current_user,login_user,logout_user

from .. import db, photos
from ..models import Comment, User,Blog
from . import main
from .forms import ReviewForm, UpdateProfile,BlogForm, CommentsForm
from ..request import get_quotes


#.....

@main.route('/')
def index():
    quotes = get_quotes()
    blog_list = Blog.query.all()

    return render_template('index.html',blog=blog_list,quotes=quotes)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    blogs = Blog.query.filter_by(user_id=current_user.id).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, blogs = blogs)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>/blog',methods= ['POST','GET'])
@login_required
def upload_blog(uname):
    user = User.query.filter_by(username = uname).first()
    form = BlogForm()
    if user is None:
        abort(404)

    if form.validate_on_submit():
        title= form.title.data
        blog_content = form.blog_content.data
        author = form.author.data

@main.route('/<int:blog_id>/delete',methods=['POST','GET'])
@login_required
def delete_blog(blog_id):
    blog=Blog.query.get(blog_id)
    if blog.user != current_user:
        abort(403)
    
    db.session.delete(blog)
    db.session.commit()

    return redirect(url_for('main.profile',uname=blog.user.username))
        
@main.route("/comment/<int:blog_id>",methods=["POST","GET"])
@login_required
def comment_blog(blog_id):
    form = CommentsForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.get_comments(blog_id)
    if form.validate_on_submit():
        new_comment = form.comment.data
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        comment_object = Comment(comment=new_comment,user_id=user_id,blog_id=blog_id)
        comment_object.save_comment()
        return redirect(url_for(".comment_blog",blog_id=blog_id))
        return render_template("comments.html",comment_form=form,blog=blog,all_comments=all_comments)
        
        # blog = Blog(title=title,blog_content=blog_content,author=author)
        # blog.save_blog()
        # return redirect(url_for('main.index'))
        # return render_template('upload_blog.html',form=form,title='Add Blog',legend='Add Blog')
    