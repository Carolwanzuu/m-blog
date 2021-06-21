from flask import redirect, render_template, url_for

from .. import db
from ..models import User
from . import auth
from .forms import RegistrationForm


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    title = "New Account"
    return render_template('auth/register.html',registration_form = form, title = title)


@auth.route('/login')
def login():
    return render_template('auth/login.html')
