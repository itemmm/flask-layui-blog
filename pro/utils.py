import hashlib
from pro import models



def md5_key(str):
    hash = hashlib.md5()
    hash.update(str)
    return hash.hexdigest()



# 根据登录账号查询用户
def getUserByLoginName(loginName):
    user = models.db.session.query(models.StUser).filter(models.StUser.login_name==loginName,models.StUser.delete_flag==0).first()
    return user

# 根据用户Id查询用户
def getUserByUserId(userId):
    user = models.db.session.query(models.StUser).filter(models.StUser.id==userId,models.StUser.delete_flag==0).first()
    return user


# 根据用户Id获取该用户的所有分类
def getCategoryByuserId(userId):
    categoryList = models.db.session.query(models.StContentCategory).filter(models.StContentCategory.user_id==userId,models.StContentCategory.delete_flag==0).all()
    return categoryList

# 根据分类Id查询文章
def getContentByCategoryId(categoryId):
    contentList = models.db.session.query(models.StContent).filter(models.StContent.category_id==categoryId,models.StContent.delete_flag==0).all()
    return contentList

# 根据分类Id查询分类
def getCategoryByCategoryId(categoryId):
    try:
        category = models.db.session.query(models.StContentCategory).filter(models.StContentCategory.id==categoryId,models.StContentCategory.delete_flag==0).first()
        return category
    except:
        return False