from flask_restful import Resource, fields, marshal_with, marshal
from blog_admin.article.models import Article, Category, ContentTag

user_fields = {
    "username": fields.String
}

article_fields = {
    "title": fields.String,
    "hash": fields.String,
    "sub_title": fields.String,
    "create": fields.DateTime(dt_format="blog_date"),
    "update": fields.DateTime(dt_format="blog_date"),
    "author": fields.Nested(user_fields),
    "reader": fields.Integer,
    "is_comment": fields.Boolean,
}


class ReadingNotesResource(Resource):
    def get(self):
        data = list()
        categories = Category.query.filter_by(name="读书笔记", is_show=1, is_del=0)
        category = categories[0]
        if category:
            articles = Article.query.filter_by(category=category, is_show=1, is_del=0).order_by(Article.create.desc())
            for article in articles:
                data.append(marshal(article, article_fields))
        return data
