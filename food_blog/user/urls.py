from django.urls import path
from django.conf.urls import url
from user import views
urlpatterns = [
    # 用户注册
    path(r'register', views.register),
    # 用户登陆
    path(r'logIn', views.logIn),
    # 回家
    path(r'home', views.home),
    # 个人简历
    path(r'me', views.me),
    # 写博客
    path(r'writeBlog', views.writeBlog),
    # 用户成功注册
    path(r'successRegisted', views.successRegisted),
    # 用户退出登陆
    path(r'logOut', views.logOut),
    # 用户修改信息
    path(r'alterInfo', views.alter_info),
    # 用户注销此账户
    path(r'logOff', views.log_off),
    # 保存blog
    path(r'saveDraft', views.save_draft),
    # 发布blog
    path(r'blogDeploy', views.blog_deploy),
    # 搜索垃圾
    path(r'garbageSearch', views.garbage_search),
    # 必须使用url才行
    # 看blog
    url('blog-(\d+)', views.see_blog),
    # 修改blog
    url('blogModify-(\d+)', views.blog_modify),
    # 删除blog
    url('blogDelete-(\d+)', views.delete_blog),
]