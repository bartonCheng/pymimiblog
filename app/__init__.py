from flask import Flask
app = Flask(__name__)

# 倒入配置文件
app.config.from_object('config')
from app import routes