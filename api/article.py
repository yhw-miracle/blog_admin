from flask_restful import Resource, fields, marshal_with, marshal
from flask import request
from blog_admin.article.models import Article, Category, ContentTag
from blog_admin.extensions import db
from datetime import datetime

category_fields = {
    "name": fields.String
}

tag_fields = {
    "name": fields.String
}

user_fields = {
    "username": fields.String
}

comment_fields = {
    "username": fields.String,
    "content": fields.String
}

articles_fields = {
    "title": fields.String,
    "hash": fields.String,
    "sub_title": fields.String,
    "category": fields.Nested(category_fields),
    "tags": fields.List(fields.Nested(tag_fields)),
    "create": fields.DateTime(dt_format="blog_date"),
    "update": fields.DateTime(dt_format="blog_date"),
    "author": fields.Nested(user_fields),
    "reader": fields.Integer,
    "is_comment": fields.Boolean,
    "comments": fields.List(fields.Nested(comment_fields))
}

article_fields = {
    "title": fields.String,
    "hash": fields.String,
    "sub_title": fields.String,
    "category": fields.Nested(category_fields),
    "tags": fields.List(fields.Nested(tag_fields)),
    "create": fields.DateTime(dt_format="blog_date"),
    "update": fields.DateTime(dt_format="blog_date"),
    "content": fields.String,
    "author": fields.Nested(user_fields),
    "reader": fields.Integer,
    "is_comment": fields.Boolean,
    "comments": fields.List(fields.Nested(comment_fields))
}


class ArticlesResource(Resource):
    def get(self):
        currentPage = int(request.args.get("currentPage", 1))
        pageSize = int(request.args.get("pageSize", 10))
        by_year = request.args.get("by_year", False)
        articles = Article.query.filter_by(is_show=1, is_del=0).order_by(Article.create.desc())
        if by_year:
            data = dict()
            for article in articles:
                year = article.create.year
                if year not in data.keys():
                    data[year] = list()
                data[year].append(marshal(article, articles_fields))
            return [ {"year": k, "articles": v} for k, v in data.items()]
        else:
            data = list()
            for article in articles[(currentPage - 1)*pageSize: currentPage*pageSize]:
                data.append(marshal(article, articles_fields))
            return {"articles": data, "count": articles.count()}


class ArticleResource(Resource):
    def get(self):
        article_hash = request.args.get("id", "")
        articles = Article.query.filter_by(is_show=1, is_del=0, hash=article_hash)
        
        data = dict()
        if articles:
            article = articles[0]
            article.reader += 1
            db.session.commit()
            data = marshal(article, article_fields)
        return data
