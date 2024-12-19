from . import app, db
from .auth import login_user, is_authenticated, get_uid, logout_user
from .validators import validate_registration, validate_login
from .utils import create_user
from .models import Users
from flask import render_template, request


@app.get('/')
def get_home_dev():
    if is_authenticated():
        return f'hello, {get_uid()}'
    return 'hello world'


@app.get('/register')
def get_register_dev():
    return render_template('register.html')


@app.get('/login')
def get_login_dev():
    return render_template('login.html')


@app.post('/register')
def post_register():
    """
    responds with:
    "" success,
    error code from .validators.validate_registration,
    "-1" failure in .utils.create_user
    """
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    user_type = request.form.get('user-type')
    print(name, email, password1, password2, user_type)
    code = validate_registration(name, email, password1, password2, user_type)
    if code: return code
    print(code)
    if not create_user(name, email, password1, user_type):
        return "100"
    return ""

@app.post('/login')
def post_login():
    """
    responds with:
    "" success,
    error code from .validators.validate_login
    :return:
    """
    email = request.form.get('email')
    password = request.form.get('password')
    code = validate_login(email, password)
    if code: return code
    uid = db.session.query(Users).filter_by(email=email).first().uid
    login_user(uid)
    return ""

@app.get('/logout')
def get_logout():
    logout_user()
    return ""
