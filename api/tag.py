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

tag_fields = {
    "name": fields.String,
    "hash": fields.String,
    "articles": fields.List(fields.Nested(article_fields))
}

class TagResource(Resource):
    def get(self):
        data = list()
        tags = ContentTag.query.filter_by(is_show=1, is_del=0)
        for tag in tags:
            data.append(marshal(tag, tag_fields))
        return data
