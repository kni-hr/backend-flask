from . import db
from sqlalchemy.orm import Mapped, mapped_column

class Users(db.Model):
    """
    user types:
    "0" admin,
    "1" hr manager,
    "2" candidate
    """
    __tablename__ = 'users'
    uid: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    email: Mapped[str]
    user_type: Mapped[str]
    bcrypt_hash: Mapped[str]

    def __repr__(self):
        print(f'<{self.name}({self.uid})>')
