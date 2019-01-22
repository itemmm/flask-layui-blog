from pro.admin import admin,contentCategory
from flask import request,render_template,jsonify,session,redirect
from pro import models,decorator,utils
import time






# 打开编辑器界面
@admin.route("/editor",endpoint="editor")
@decorator.authentication
def editor():
    params = request.args
    categoryId = params.get("categoryId")
    category = utils.getCategoryByCategoryId(categoryId=categoryId)
    # 判断是否存在该分类Id
    if category:
        loginName = session.get("login_name")
        user = utils.getUserByLoginName(loginName=loginName)
        if category.user_id == user.id:
            return render_template("admin/editor.html",content=category)
        else:
            return redirect("/index")
    else:
        return redirect("/index")



# 保存编辑器提交的文本内容
@admin.route("/saveContent",methods=["POST"],endpoint='saveContent')
@decorator.authentication
def saveContent():
    msg = {}
    loginName = session.get("login_name")
    user = utils.getUserByLoginName(loginName=loginName)
    params = request.form
    title = params.get("title")
    des = params.get("des")
    mdText = params.get("md_text")
    htmlText = params.get("html_text")
    nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
    categoryId = params.get("categoryId")
    if title and des and mdText and htmlText:
        newContent = models.StContent(title=title,des=des,author=user.id,category_id=categoryId,md_text=mdText,html_text=htmlText,create_time=nowTime,update_time=nowTime)
        models.db.session.add(newContent)
        models.db.session.commit()
        msg["code"] = 0
        msg["data"] = []
        msg["msg"] = "保存成功！"
    else:
        msg["code"] = 1001
        msg["msg"] = "必填项不能为空！"
    return jsonify(msg)


# 展示文章列表
@admin.route("/contentList",methods=["GET"],endpoint="contentList")
@decorator.authentication
def contentList():
    msg = {}
    msg["data"] = []
    params = request.args
    page = int(params.get("page"))
    limit = int(params.get("limit"))
    # 统计总数
    count = models.db.session.query(models.StContent).filter(models.StContent.delete_flag==0).count()
    msg["count"] = count
    contents = models.StContent.query.filter(models.StContent.delete_flag==0).order_by(models.StContent.id.desc()).paginate(page=page,per_page=limit,error_out=False)
    totalPage = contents.pages
    currentPage = contents.page
    if currentPage > totalPage:
        msg["code"] = 1001
        msg["msg"] = "已无更多数据！"
        return jsonify(msg)
    for content in contents.items:
        author = content.author
        user = utils.getUserByUserId(userId=author)
        appendInfo = {
            "id": content.id,
            "author_name": user.nickname,
            "avatar": user.avatar,
            "title": content.title,
            "des": content.des,
            "html_text": content.html_text,
            "create_time": str(content.create_time)
        }
        msg["data"].append(appendInfo)
    msg["code"] = 0
    msg["msg"] = "请求成功！"
    return jsonify(msg)


# 查看文章详情
@admin.route("/contentDetail",methods=["GET"],endpoint="contentDetail")
@decorator.authentication
def contentDetail():
    msg = {}
    msg["data"] = []
    params = request.args
    contentId = params.get("contentId")
    contentInfo = models.db.session.query(models.StContent).filter(models.StContent.id==contentId,models.StContent.delete_flag==0).one()
    commentList = models.db.session.query(models.StComment).filter(models.StComment.content_id==contentId,models.StComment.delete_flag==0).all()
    comments = []
    for commentInfo in commentList:
        userId = commentInfo.user_id
        user = models.db.session.query(models.StUser).filter(models.StUser.id==userId).first()
        appendInfo = {"comment":commentInfo,"user":user}
        comments.insert(0,appendInfo)
    content = {
        "content":contentInfo,
        "comment":comments
    }
    return render_template("admin/contentDetail.html",content=content)


# 编辑文章
@admin.route("/updateContent",methods=["GET","POST"],endpoint="updateContent")
@decorator.authentication
def updateContent():
    msg = {}
    msg["data"] = []
    if request.method == "GET":
        params = request.args
        contentId = params.get("contentId")
        content = models.db.session.query(models.StContent).filter(models.StContent.id==contentId,models.StContent.delete_flag==0).one()
        return render_template("admin/updateContent.html",content=content)
    elif request.method == "POST":
        params = request.form
        contentId = params.get("contentId")
        title = params.get("title")
        des = params.get("des")
        mdText = params.get("editormd-markdown-doc")
        htmlText = params.get("editormd-html-code")
        nowTime = time.strftime("%Y-%m-%d %H:%M:%S")
        content = models.db.session.query(models.StContent).filter(models.StContent.id == contentId,models.StContent.delete_flag==0).one()
        content.title = title
        content.des = des
        content.md_text = mdText
        content.html_text = htmlText
        content.update_time = nowTime
        models.db.session.commit()
        msg["code"] = 0
        msg["msg"] = "保存成功！"
        return jsonify(msg)

# 添加文章分类
@admin.route("/addCategory",methods=["GET","POST"],endpoint="addCategory")
@decorator.authentication
def addCategory():
    if request.method == "GET":
        return render_template("admin/addCategory.html")
    elif request.method == "POST":
        params = request.form
        categoryName = params.get("categoryName")
        categoryDes = params.get("categoryDes")
        categoryImg = params.get("categoryImg")
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S")
        msg = contentCategory.addCategory(categoryName=categoryName, categoryDes=categoryDes, categoryImg=categoryImg, currentTime=currentTime)
        return jsonify(msg)

# 文章分类列表
@admin.route("/categoryList",endpoint="categoryList")
@decorator.authentication
def categoryList():
    msg = contentCategory.categoryList()
    return jsonify(msg)