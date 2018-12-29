from flask import Flask
from pro.admin.admin import admin
from pro.user.user import user
from pro.models import db
from flask_session import Session
import redis




app = Flask(__name__)

app.register_blueprint(admin,url_prefix="/admin")
app.register_blueprint(user,url_prefix="/user")



app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1:3306/shengTang?charset=utf8'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True


app.config['SESSION_TYPE'] = 'redis'  # session类型为redis
app.config['SESSION_PERMANENT'] = False  # 如果设置为True，则关闭浏览器session就失效。
app.config['SESSION_USE_SIGNER'] = False  # 是否对发送到浏览器上session的cookie值进行加密
app.config['SESSION_KEY_PREFIX'] = 'session:'  # 保存到session中的值的前缀
app.config['SESSION_REDIS'] = redis.Redis(host='192.168.31.60', port='6379')  # 用于连接redis的配置
app.config['PERMANENT_SESSION_LIFETIME'] = 3600 #session长期有效，则设定session生命周期，整数秒，默认大概不到3小时。
Session(app)


db.init_app(app)