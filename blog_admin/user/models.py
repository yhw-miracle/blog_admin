from blog_admin.models import BaseModel
from blog_admin.extensions import db
import hashlib
from flask_login import UserMixin

class User(BaseModel, UserMixin):
    """用户表"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    # 用户名
    username = db.Column(db.String(100), unique=True)
    # 密码
    password = db.Column(db.String(128))
    # 昵称
    email = db.Column(db.String(100))
    # slogan
    slogan = db.Column(db.String(100))
    # last login
    last_login = db.Column(db.DateTime)
    # 头像
    photo = db.Column(db.String(100))
    # 用户 ip 信息
    ip_info = db.relationship("IPInfo", secondary="user_to_ipinfo", backref="users")
    
    articles = db.relationship("Article", back_populates="author")

    def __str__(self) -> str:
        return self.username
    
    @staticmethod
    def generate_password(password):
        sha256_obj = hashlib.sha256()
        sha256_obj.update(password.encode("utf-8"))
        return sha256_obj.hexdigest()

    def set_password(self, password):
        self.password = self.generate_password(password)
        return self.password

    def validate_password(self, password):
        return self.password == self.generate_password(password)


class UserToIpInfo(BaseModel):
    __tablename__ = "user_to_ipinfo"

    id = db.Column(db.Integer, primary_key=True)
    ipinfo_id = db.Column(db.Integer, db.ForeignKey("ipinfo.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
