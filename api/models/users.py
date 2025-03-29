import sqlalchemy.orm as os
from api import db, brcrypt
from hmac import compare_digest

class User(db.Model):
    id: os.Mapped[int] = os.mapped_column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    username: os.Mapped[str] = os.mapped_column(db.String(128), nullable=False)
    email: os.Mapped[str] = os.mapped_column(db.String(128), nullable=False)
    password: os.Mapped [str] = os.mapped_column(db.String(255), nullable=False)

    def check_password(self, password):
        return compare_digest(password, "password")