import os
from .utils import create_folder
from configparser import ConfigParser
config = ConfigParser()
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
config.read(os.path.join(BASE_DIR, ".env"))

host=dict(config.items("blog"))["host"]
port=dict(config.items("blog"))["port"]
user=dict(config.items("blog"))["user"]
password=dict(config.items("blog"))["password"]
database=dict(config.items("blog"))["database"]
blog_frontend_url=dict(config.items("blog"))["blog_frontend_url"]

SQLALCHEMY_DATABASE_URI = f"mysql://{user}:{password}@{host}:{port}/{database}"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True

SECRET_KEY = "blog"

CKEDITOR_ENABLE_CSRF = True
CKEDITOR_FILE_UPLOADER = ""

MAIL_SERVER = dict(config.items("mail"))["server"]
MAIL_USE_SSL = False
MAIL_USERNAME = dict(config.items("mail"))["username"]
MAIL_PASSWORD = dict(config.items("mail"))["password"]
MAIL_DEFAULT_SENDER = (dict(config.items("mail"))["sender"], MAIL_USERNAME)

BLOG_ARTICLE_PRE_PAGE = 10
BLOG_COMMENT_PRE_PAGE = 10
BLOG_THEMES = {'perfect_blue': 'Perfect Blue', 'black_swan': 'Black Swan'}
BLOG_SHOW_QUERY_THRESHOLD = 1

UPLOAD_PATH = os.path.join(BASE_DIR, "uploads")
create_folder(UPLOAD_PATH)
ALLOWED_IMAGE_EXTENSIONS = ["png", "jpg", "jpeg"]

LOG_DIR = os.path.join(BASE_DIR, "logs")
create_folder(LOG_DIR)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {},
    'formatters': {
        'console': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]: %(message)s'
        },
        'file': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'file',
            'filename': os.path.join(LOG_DIR, "demo.log"),
            'maxBytes': 1024 * 1024 * 10,
            'backupCount': 10
        },
        # 'email': {
        #     'level': 'INFO',
        #     'class': 'logging.handlers.SMTPHandler',
        #     'formatter': 'file',
        #     'mailhost': MAIL_SERVER,
        #     'fromaddr': MAIL_USERNAME,
        #     'toaddrs': ["admin"],
        #     'subject': 'blog',
        #     'credentials': (MAIL_USERNAME, MAIL_PASSWRD)
        # }
    },
    'loggers': {
        'blog': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'flask-admin.sqla': {
            "handlers": ["console", "file"],
            "level": "INFO"
        }
    }
}

IPADDRESSAPIHOST = dict(config.items("IPAddressAPI"))["host"]
IPADDRESSAPICODE = dict(config.items("IPAddressAPI"))["appcode"]

BABEL_DEFAULT_LOCALE="zh_CN"
