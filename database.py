from flask_script import Manager
from pro import app
from flask_migrate import Migrate, MigrateCommand
from pro.models import db


manager = Manager(app)

# 1. 要使用flask_migrate, 必须绑定app和db
migrate = Migrate(app, db)

# 2. 把MigrateCommand命令添加到manager中
manager.add_command('db', MigrateCommand)


#这个命令会创建migrations文件夹，所有迁移文件都放在里面。
# python3 database.py db init

# 迁移
# python3 database.py db migrate

# 更新数据库
# python3 database.py db upgrade


if __name__ == '__main__':
    manager.run()