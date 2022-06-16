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

category_fields = {
    "name": fields.String,
    "hash": fields.String,
    "articles": fields.List(fields.Nested(article_fields))
}

class CategoryResource(Resource):
    def get(self):
        data = list()
        categories = Category.query.filter_by(is_show=1, is_del=0)
        for category in categories:
            data.append(marshal(category, category_fields))
        return data
