from flask_admin.contrib.sqla import ModelView
from blog_admin.article.models import Article


class ArticleView(ModelView):
    page_size = 10
    column_exclude_list = ["content", "hash", "is_show", "is_del"]
    # form_excluded_columns = ["content_path", "reador", "comments", "hash", "create", "update", "is_show", "is_del"]
    form_excluded_columns = ["content_path", "reador", "comments", "hash", "update", "is_show", "is_del"]

    column_labels = {
        "category": "分类", 
        "tags": "标签", 
        "title": "标题", 
        "sub_title": "副标题",
        "content": "内容",
        "author": "作者",
        "is_comment": "是否允许评论"
    }

    def get_query(self):
        return Article.query.filter_by(is_show=1, is_del=0).order_by(Article.create.desc())


class CategoryView(ModelView):
    page_size = 10
    column_exclude_list = ["hash", "is_show", "is_del"]
    form_excluded_columns = ["hash", "update", "is_show", "is_del"]

    column_labels = {
        "name": "分类名称", 
        "articles": "文章列表"
    }


class TagsView(ModelView):
    page_size = 10
    column_exclude_list = ["hash", "is_show", "is_del"]
    form_excluded_columns = ["hash", "update", "is_show", "is_del"]

    column_labels = {
        "name": "标签名称", 
        "articles": "文章列表"
    }


class CommentView(ModelView):
    page_size = 10
    column_exclude_list = ["hash", "is_show", "is_del"]
    form_excluded_columns = ["hash", "create", "update", "is_show", "is_del"]

    column_labels = {
        "username": "用户名", 
        "email": "邮箱",
        "content": "评论内容",
        "ip_info": "评论人 ip 信息",
        "article": "文章",
        "reviewed": "是否审核",
        "replies": "被回复用户",
        "replied": "回复用户"
    }
