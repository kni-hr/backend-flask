from . import db
from .models import Users
from .auth import check_password


def validate_registration(name: str, email: str, password1: str, password2: str, user_type: str) -> str:
    """
    function responds with "" or an error code:
    "1" blank fields,
    "2" passwords don't match,
    "3" invalid user type
    "4" email is in use
    """
    if not all([name, email, password1, password2, user_type]):
        return "1"
    if password1 != password2:
        return "2"
    if user_type != "1" and user_type != "2":
        return "3"
    if db.session.query(Users).filter_by(email=email).count():
        return "4"

    return ""


def validate_login(email: str, password: str) -> str:
    """
    returns "" or an error code:
    "1" blank fields,
    "2" invalid credentials
    """
    if not all([email, password]):
        return "1"

    user = Users.query.filter_by(email=email).first()
    if not user or not check_password(password, user.bcrypt_hash):
        return "2"
    return ""
