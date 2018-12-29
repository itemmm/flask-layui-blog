from pro import app
from flask import render_template,session,request,redirect
from pro import decorator,models,utils



@app.route("/")
def root():
    return redirect("/index")

@app.route("/index",endpoint='index')
@decorator.authentication
def index():
    loginName = session.get("login_name")
    user = models.db.session.query(models.StUser).filter(models.StUser.login_name == loginName,models.StUser.delete_flag == 0).first()
    return render_template("pro/index.html",content=user)



@app.route("/content",methods=["GET"])
def content():
    msg = {}
    msg["data"] = []
    params = request.args
    contentId = params.get("contentId")
    content = models.db.session.query(models.StContent).filter(models.StContent.id == contentId,models.StContent.delete_flag == 0).one()
    user = utils.getUserByUserId(userId=content.author)
    msg = {
        "title":content.title,
        "des": content.des,
        "md_text": content.md_text,
        "author_nickname": user.nickname,
        "author_avatar":user.avatar,
        "create_time": content.create_time
    }
    return render_template("pro/content.html", content=msg)