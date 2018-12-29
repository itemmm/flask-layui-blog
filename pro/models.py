from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class StContent(db.Model):
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True,nullable=False)
    title = db.Column(db.VARCHAR(255))
    des = db.Column(db.VARCHAR(255))
    author = db.Column(db.INTEGER)
    category_id = db.Column(db.INTEGER)
    md_text = db.Column(db.TEXT)
    html_text = db.Column(db.TEXT)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)
    delete_flag = db.Column(db.INTEGER,default=0,nullable=False)
    show_flag = db.Column(db.INTEGER,default=0,nullable=False)


class StUser(db.Model):
    id = db.Column(db.INTEGER,primary_key=True,autoincrement=True,nullable=False)
    login_name = db.Column(db.VARCHAR(255))
    password = db.Column(db.VARCHAR(255))
    nickname = db.Column(db.VARCHAR(255))
    avatar = db.Column(db.VARCHAR(255))
    level = db.Column(db.INTEGER)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)
    delete_flag = db.Column(db.INTEGER, default=0, nullable=False)


class StContentCategory(db.Model):
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True, nullable=False)
    category_name = db.Column(db.VARCHAR(255))
    category_des = db.Column(db.VARCHAR(255))
    category_img = db.Column(db.VARCHAR(255))
    user_id = db.Column(db.INTEGER)
    create_time = db.Column(db.DATETIME)
    update_time = db.Column(db.DATETIME)
    delete_flag = db.Column(db.INTEGER, default=0, nullable=False)