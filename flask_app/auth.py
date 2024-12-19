from flask import session
from bcrypt import checkpw


def is_authenticated() -> bool:
    return 'uid' in session


def get_uid() -> str:
    """
    make sure user is_authenticated() before calling this function
    """
    return session['uid']


def login_user(uid: int) -> None:
    session['uid'] = uid


def logout_user() -> None:
    session.pop('uid')


def check_password(password: str, bcrypt_hash: str) -> bool:
    return checkpw(password.encode(), bcrypt_hash.encode())
