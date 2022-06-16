from blog_admin.extensions import db
from datetime import datetime


class BaseModel(db.Model):

    __abstract__ = True

    # 创建时间
    create = db.Column(db.DateTime, default=datetime.now)
    # 更新时间
    update = db.Column(db.DateTime)
    # 是否显示
    is_show = db.Column(db.Integer, default=1)
    # 是否删除
    is_del = db.Column(db.Integer, default=0)
    
