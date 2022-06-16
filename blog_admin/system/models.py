from blog_admin.models import BaseModel
from blog_admin.extensions import db


class SystemInfo(BaseModel):
    """系统表"""
    __tablename__ = "system_info"

    id = db.Column(db.Integer, primary_key=True)
    # 博客标题
    title = db.Column(db.String(100))
    # 博客副标题
    sub_title = db.Column(db.String(100))
    # 包括 slagon
    slagon = db.Column(db.String(100))
    # 博客头像
    photo = db.Column(db.String(100))

    def __str__(self) -> str:
        return self.title


class IPInfo(BaseModel):
    """IP 信息"""
    __tablename__ = "ipinfo"

    id = db.Column(db.Integer, primary_key=True)
    # ip
    ip = db.Column(db.String(100))
    # long_ip
    long_ip = db.Column(db.String(100))
    # isp
    isp = db.Column(db.String(100))
    # area
    area = db.Column(db.String(100))
    # region_id
    region_id = db.Column(db.String(100))
    # region
    region = db.Column(db.String(100))
    # city_id
    city_id = db.Column(db.String(100))
    # city
    city = db.Column(db.String(100))
    # country_id
    country_id = db.Column(db.String(100))
    # country
    country = db.Column(db.String(100))

    comments = db.relationship("Comment", back_populates="ip_info")

    def __str__(self) -> str:
        country = self.country if self.country else ""
        region = self.region if self.region else ""
        city = self.city if self.city else ""
        return f"{self.ip}_{country}{region}{city}"
