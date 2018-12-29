from flask import session,redirect
from pro import models



def authentication(func):
    def wrapper(*args,**kwargs):
        loginName = session.get("login_name")
        passWord = session.get("password")
        user = models.db.session.query(models.StUser).filter(models.StUser.login_name==loginName,models.StUser.delete_flag==0).first()
        if user is None:
            return redirect("user/login")
        else:
            if loginName==user.login_name and passWord==user.password:
                return func(*args,**kwargs)
            else:
                # return func(*args, **kwargs)
                return redirect("user/login")
    return wrapper