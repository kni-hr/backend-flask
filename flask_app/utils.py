from .import db
from .models import Users
from bcrypt import hashpw, gensalt
from sqlalchemy.exc import DatabaseError, InterfaceError


def create_user(name: str, email: str, password: str, user_type: str) -> bool:
    bcrypt_hash = hashpw(password.encode(), gensalt())
    new_user = Users(name=name, email=email, bcrypt_hash=bcrypt_hash.decode(), user_type=user_type)
    try:
        db.session.add(new_user)
        db.session.commit()
    except (DatabaseError, InterfaceError):
        return False
    return True
