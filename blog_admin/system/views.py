from flask_admin.contrib.sqla import ModelView


class SystemInfoView(ModelView):
    page_size = 10
    column_exclude_list = ["is_show", "is_del"]
    form_excluded_columns = ["create", "update", "is_show", "is_del"]

    column_labels = {
        "title": "博客标题", 
        "sub_title": "博客副标题", 
        "slogan": "slogan", 
        "photo": "头像"
    }


class IPInfoView(ModelView):
    page_size = 10
    column_exclude_list = ["is_show", "is_del"]
    form_excluded_columns = ["create", "update", "is_show", "is_del"]

    column_labels = {
        "comments": "评论", 
        "users": "用户"
    }
