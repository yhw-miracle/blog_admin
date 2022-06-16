from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    page_size = 10
    column_exclude_list = ["password", "is_show", "is_del"]
    form_excluded_columns = ["password", "update", "is_show", "is_del"]

    column_labels = {
        "username": "用户名", 
        "email": "邮箱",
        "slogan": "slogan",
        "last_login": "上次登录",
        "photo": "用户头像",
        "articles": "文章",
        "ip_info": "用户登录IP"
    }
