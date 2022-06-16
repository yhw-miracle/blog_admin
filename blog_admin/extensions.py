from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_babelex import Babel

login_manager = LoginManager()
mail = Mail()
db = SQLAlchemy()
admin = Admin(template_mode="bootstrap3")
babel = Babel()


@login_manager.user_loader
def load_user(user_id):
    from blog_admin.user.models import User
    user = User.query.filter_by(id=user_id).first()
    return user


login_manager.login_view = "user.login"
