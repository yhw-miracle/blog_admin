import os
from urllib.parse import urlparse, urljoin
from flask import request, current_app, redirect, url_for
import requests
import hashlib
import json
from datetime import datetime


def create_folder(folder):
    if os.path.exists(folder) is False:
        os.makedirs(folder)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ("host", "hosts") and ref_url.netloc == test_url.netloc


def redirect_back(default="article.articles", **kwargs):
    for target in request.args.get("next"), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def allow_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1] in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]


def get_ipinfo(remote_addr):
    current_app.logger.info(current_app.config.get("IPADDRESSAPIHOST"))
    current_app.logger.info(current_app.config.get("IPADDRESSAPICODE"))
    url = f'{current_app.config.get("IPADDRESSAPIHOST")}/ip?ip={remote_addr}'
    headers = {"Authorization": f"APPCODE {current_app.config.get('IPADDRESSAPICODE')}"}
    response = requests.get(url=url, headers=headers)
    if response.content:
        content = json.loads(response.content, encoding="utf-8")
        current_app.logger.info(content)
        if content.get("ret", "") == 200:
            return content


def generate_hash(content):
    sha256_obj = hashlib.sha256()
    sha256_obj.update(content.encode("utf-8"))
    return sha256_obj.hexdigest()


def create_article_file(title, content, article_create=None):
    from blog_admin.settings import BASE_DIR
    if article_create is None:
        article_create = datetime.now()
    article_folder = os.path.join(BASE_DIR, "articles", str(article_create.year), str(article_create.month))
    create_folder(article_folder)
    article_filepath = os.path.join(article_folder, f"{article_create.strftime('%Y-%m-%d')}-{title}.md")
    with open(article_filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return os.path.abspath(article_filepath)
