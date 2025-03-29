import sqlalchemy.orm as os
from api import db, bcrypt
from hmac import compare_digest

class User(db.Model):
    id: os.Mapped[int] = os.mapped_column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    username: os.Mapped[str] = os.mapped_column(db.String(128), nullable=False)
    email: os.Mapped[str] = os.mapped_column(db.String(128), nullable=False)
    password: os.Mapped [str] = os.mapped_column(db.String(255), nullable=False)

    def set_password(self, raw_password):
        self.password = bcrypt.generate_password_hash(raw_password).decode('utf-8')

    def check_password(self, input_password):
        return bcrypt.check_password_hash(self.password, input_password)