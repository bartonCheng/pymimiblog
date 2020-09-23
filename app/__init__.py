from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
# from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

# app.wsgi_app = ProxyFix(app.wsgi_app, num_proxies=1)
# 倒入配置文件
app.config.from_object('config')
from app import routes