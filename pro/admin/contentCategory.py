from pro import models
import time




def addCategory(categoryName,categoryDes,categoryImg,currentTime):
    msg = {}
    if categoryName and categoryDes and categoryImg and currentTime:
        newCategory = models.StContentCategory(category_name=categoryName,category_des=categoryDes,category_img=categoryImg,create_time=currentTime,update_time=currentTime)
        models.db.session.add(newCategory)
        models.db.session.commit()
        msg["code"] = 0
        msg["data"] = []
        msg["msg"] = "保存成功！"
    else:
        msg["code"] = 1001
        msg["msg"] = "必填项不能为空！"
    return msg

def categoryList():
    msg = {}
    msg["data"] = []
    categoryList = models.db.session.query(models.StContentCategory).filter(models.StContentCategory.delete_flag==0).all()
    msg["count"] = len(categoryList)
    for category in categoryList:
        appendInfo = {
            "categoryId":category.id,
            "categoryName":category.category_name,
            "categoryDes":category.category_des,
            "categoryImg":category.category_img,
            "createTime":str(category.create_time)
        }
        msg["data"].append(appendInfo)
        msg["code"] = 0
        msg["msg"] = "请求成功！"
    return msg