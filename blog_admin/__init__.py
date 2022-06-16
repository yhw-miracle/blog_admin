import logging
import logging.config
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
import click
from blog_admin import settings
from blog_admin.utils import create_folder, get_ipinfo
from flask import Flask, current_app, redirect, render_template, request
from blog_admin.extensions import login_manager, mail, db, admin, babel
from blog_admin.user.models import User
from blog_admin.system.models import SystemInfo, IPInfo
from blog_admin.article.models import Category, Article, ContentTag, ArticleToTag, Comment
from datetime import datetime

def register_logging(app):
    class RequestFormatter(logging.Formatter):
        def format(self, record):
            record.url = request.url
            record.remote_addr = request.remote_addr
            return super(RequestFormatter, self).format(record)

    request_formatter = RequestFormatter("%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s] [%(remote_addr)s] -> [%(url)s]: %(message)s")
    mail_handler = SMTPHandler(mailhost=settings.MAIL_SERVER, fromaddr=settings.MAIL_USERNAME, toaddrs=["admin"], subject="blog", credentials=(settings.MAIL_USERNAME, settings.MAIL_PASSWORD))
    mail_handler.setLevel(logging.ERROR)
    mail_handler.setFormatter(request_formatter)

    file_handler = RotatingFileHandler(filename=os.path.join(settings.LOG_DIR, "demo1.log"), maxBytes=1024 * 1024 * 10, backupCount=10)
    format = logging.Formatter("%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]: %(message)s")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(format)

    app.logger.addHandler(mail_handler)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    
    logging.config.dictConfig(settings.LOGGING)
    

def regsiter_extensions(app):
    # bootstrap4.init_app(app)
    # ckeditor.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    # moment.init_app(app)
    db.init_app(app)
    # csrf.init_app(app)
    # migrate.init_app(app, db)
    admin.init_app(app)
    babel.init_app(app)


def register_errors(app):
    @app.errorhandler(400)
    def bad_reequest(e):
        return render_template(template_name_or_list="errors/400.html"), 400
    
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template(template_name_or_list="errors/404.html"), 404
    
    @app.errorhandler(500)
    def server_error(e):
        return render_template(template_name_or_list="errors/500.html"), 500
    
    # @app.errorhandler(CSRFError)
    # def handle_csrf_error(e):
    #     return render_template(template_name_or_list="errors/400.html", description=e.description), 400

def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(db=db)

def regsiter_templater_context(app):
    @app.context_processor
    def make_template_context():
        system_info = SystemInfo.query.filter_by(is_show=1, is_del=0).order_by(SystemInfo.update.desc()).first()
        return dict(system_info=system_info)

def register_commands(app):
    @app.cli.command(help="初始化数据库")
    @click.option("--drop", default=True, help="重置数据库")
    def initdb(drop):
        if drop:
            click.confirm("需要先删除数据库再重新新建数据库?", abort=True)
            db.drop_all()
            click.echo("已删除数据库")
        db.create_all()
        click.echo("初始化数据库")

    @app.cli.command(help="初始化数据")
    def initdata():
        from datetime import datetime
        system_info = SystemInfo(title="yhw-miracle", slagon="每一个人的生命中，都有最艰难的那一年，将人生变得美好而辽阔。", update=datetime.now())
        ip_info = IPInfo(
            ip="47.114.156.255",
            long_ip="796040447",
            isp="阿里云",
            area="华东",
            region_id="330000",
            region="浙江",
            city_id="330100",
            city="杭州",
            country_id="CN",
            country="中国",
            update=datetime.now()
        )
        db.session.add(system_info)
        db.session.add(ip_info)
        db.session.commit()

def handle_request(app):
    @app.before_request
    def handler_before_request():
        current_app.logger.info(request.url)
        current_app.logger.info(request.path)
        current_app.logger.info(request.remote_addr)
        remote_addr = request.remote_addr
        logger = logging.getLogger("blog")
        logger.info(remote_addr)
        # remote_addr = "47.114.156.255"
        ip_info = IPInfo.query.filter_by(ip=remote_addr).first()
        if ip_info is None:
            content = get_ipinfo(remote_addr)
            if content:
                ip_info = IPInfo(
                    ip=content["data"]["ip"],
                    long_ip=content["data"]["long_ip"],
                    isp=content["data"]["isp"],
                    area=content["data"]["area"],
                    region_id=content["data"]["region_id"],
                    region=content["data"]["region"],
                    city_id=content["data"]["city_id"],
                    city=content["data"]["city"],
                    country_id=content["data"]["country_id"],
                    country=content["data"]["country"],
                    update=datetime.now()
                )
            else:
                ip_info = IPInfo(ip=remote_addr, update=datetime.now())
            db.session.add(ip_info)
            db.session.commit()

    @app.after_request
    def handler_after_request(response):
        app.logger.info(response.content_type)
        app.logger.info(response.is_json)
        response.headers["Access-Control-Allow-Origin"] = settings.blog_frontend_url
        return response


def handle_admin():
    from blog_admin.article.views import ArticleView, CategoryView, TagsView, CommentView
    from blog_admin.user.views import UserView
    from blog_admin.system.views import SystemInfoView, IPInfoView
    admin.add_view(ArticleView(Article, db.session, "文章"))
    admin.add_view(CategoryView(Category, db.session, "分类"))
    admin.add_view(TagsView(ContentTag, db.session, "标签"))
    admin.add_view(CommentView(Comment, db.session, "评论"))
    admin.add_view(UserView(User, db.session, "用户"))
    admin.add_view(IPInfoView(IPInfo, db.session, "IP"))
    admin.add_view(SystemInfoView(SystemInfo, db.session, "系统配置"))

def handle_api(app):
    from api import api
    api.init_app(app)


def create_app():
    app = Flask("blog_admin", template_folder="templates", static_folder="static", static_url_path="")
    create_folder(os.path.join(settings.BASE_DIR, app.name, "templates"))
    create_folder(os.path.join(settings.BASE_DIR, app.name, "static"))
    app.config.from_object(settings)

    # 注册日志处理器
    register_logging(app)
    # 注册扩展
    regsiter_extensions(app)
    # 注册错误处理函数
    # register_errors(app)
    # 注册 shell 上下文处理函数
    # register_shell_context(app)
    # 注册模板上下文处理函数
    regsiter_templater_context(app)
    # 注册自定义 shell 命令
    register_commands(app)
    # 请求处理
    handle_request(app)
    
    handle_admin()
    
    handle_api(app)

    return app
