from blog_admin.models import BaseModel
from blog_admin import db
from blog_admin.utils import generate_hash

class Category(BaseModel):
    """文章分类表"""
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    # 分类名称
    name = db.Column(db.String(100))
    # hash 值
    hash = db.Column(db.String(100))

    articles = db.relationship("Article", back_populates="category")

    def __str__(self) -> str:
        return self.name


class Article(BaseModel):
    """文章表"""
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True)
    # 标题
    title = db.Column(db.String(100))
    # 副标题
    sub_title = db.Column(db.String(100))
    # 分类
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    category = db.relationship("Category", back_populates="articles")
    # 标签
    tags = db.relationship("ContentTag", secondary="article_to_tag", backref="articles")
    # 内容
    content = db.Column(db.Text)
    content_path = db.Column(db.String(100))
    # 作者
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("User", back_populates="articles")
    # 阅读量
    reader = db.Column(db.Integer, default=0)
    # 是否允许评论
    is_comment = db.Column(db.Boolean, default=1)
    # hash 值
    hash = db.Column(db.String(100))

    comments = db.relationship("Comment", back_populates="article")
    
    def __str__(self) -> str:
        return self.title


class ContentTag(BaseModel):
    """标签"""
    __tablename__ = "tag"

    id = db.Column(db.Integer, primary_key=True)
    # 标签名称
    name = db.Column(db.String(100))
    # hash 值
    hash = db.Column(db.String(100))

    def __str__(self) -> str:
        return self.name


class ArticleToTag(BaseModel):
    """文章标签"""

    __tablename__ = "article_to_tag"

    id = db.Column(db.Integer, primary_key=True)
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tag.id"))


class Comment(BaseModel):
    """评论表"""

    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    # 用户名
    username = db.Column(db.String(100))
    # 邮箱
    email = db.Column(db.String(100))
    # 评论内容
    content = db.Column(db.Text)
    # 关联 ip 信息
    ip_info_id = db.Column(db.Integer, db.ForeignKey("ipinfo.id"))
    ip_info = db.relationship("IPInfo", back_populates="comments")
    # 关联文章信息
    article_id = db.Column(db.Integer, db.ForeignKey("article.id"))
    article = db.relationship("Article", back_populates="comments")
    # 是否审核通过
    reviewed = db.Column(db.Boolean, default=1)
    # 回复信息
    reply_id = db.Column(db.Integer, db.ForeignKey("comment.id"))
    replies = db.relationship("Comment", back_populates="replied")
    replied = db.relationship("Comment", back_populates="replies", remote_side=[id])
    # hash 值
    hash = db.Column(db.String(100))

    def __str__(self) -> str:
        return f"{self.username}_{self.content}"
