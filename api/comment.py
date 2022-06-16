from flask_restful import Resource, fields, marshal_with, marshal
from blog_admin.article.models import Article, Category, ContentTag, Comment

user_fields = {
    "username": fields.String
}

article_fields = {
    "title": fields.String,
    "sub_title": fields.String,
    "content": fields.String,
    "author": fields.Nested(user_fields),
    "reador": fields.Integer,
    "is_comment": fields.Boolean
}

ip_info_fields = {
    "ip": fields.String,
    "country": fields.String,
    "region": fields.String,
    "city": fields.String
}

comment_fields = {
    "username": fields.String,
    "email": fields.String,
    "content": fields.String,
    "ip_info": fields.Nested(ip_info_fields),
    "article": fields.Nested(article_fields),
    "reviewed": fields.Boolean
}

class CommentResource(Resource):
    def get(self):
        data = list()
        comments = Comment.query.filter_by(is_show=1, is_del=0)
        for comment in comments:
            data.append(marshal(comment, comment_fields))
        return data
