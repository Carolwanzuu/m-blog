from flask import abort, redirect, render_template, request, url_for
from flask_login import login_required,current_user,login_user,logout_user

from .. import db, photos
from ..models import User,Blog
from . import main
from .forms import ReviewForm, UpdateProfile,BlogForm


#.....

@main.route('/')
def index():
    all_business = Blog.query.filter_by().all()
    return render_template('index.html',all_blog=all_blog)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

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
        posted= form.posted.data
        

        
        blog = Blog(title=title,blog_content=blog_content,author=author,posted=posted)
        blog.save_blog()
        return redirect(url_for('main.index'))
    return render_template('upload_blog.html',form=form,title='Add Blog',legend='Add Blog')
    