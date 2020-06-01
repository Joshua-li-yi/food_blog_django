from django.urls import path
from django.conf.urls import url
from user import views
urlpatterns = [
    path(r'register', views.register),
    path(r'logIn', views.logIn),
    path(r'home', views.home),
    path(r'me', views.me),
    path(r'writeBlog', views.writeBlog),
    path(r'successRegisted', views.successRegisted),
    path(r'logOut', views.logOut),
    path(r'alterInfo', views.alter_info),
    path(r'logOff', views.delete_user),
    path(r'saveDraft', views.save_draft),
    path(r'blogDeploy', views.blog_deploy),
    # 必须使用url才行
    url('blog-(\d+)', views.see_blog),
]