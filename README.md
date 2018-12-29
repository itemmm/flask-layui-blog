# shengTangBlog
python语言，后端flask框架，前端layui框架，markdown编辑器使用editormd编辑器

# 部署
Python3
Linux + Nginx + uwsgi

### uwsgi.ini配置：
```
[uwsgi]
# 使用的通讯协议，有http,socket,http-socket
http = 127.0.0.1:5000

# flask应用所在的文件
wsgi-file = /usr/local/nginx/html/shengTangBlog/manager.py

# flask应用实例的名称
callable = app
processes = 1
threads = 2
touch-reload = /usr/local/nginx/html/shengTangBlog/
```
### 使用http协议是配置Nginx：
```
server{
　　listen  80;
　　server_name  localhost;
　　location /flask {
　　　　proxy_pass  http://127.0.0.1:5000;
　　}
}
```

启动命令：
uwsgi uwsgi.ini

# 功能说明
目前功能较少，只能支持个人使用

## 用户管理
当前没有用户注册功能，仅支持登录

### 登录

## 文章管理
目前文章管理拥有分类，但是还没有添加分类功能，后期迭代

### 增加
markdown语言书写博客，以editormd编辑器为主

### 编辑
支持修改文章

### 查看
支持查看文章
