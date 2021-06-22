from . import main
from .. import db
from flask import render_template,request,redirect,url_for,abort
from ..models import User
from flask_login import login_required

#.....
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
