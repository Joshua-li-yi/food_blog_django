from django.urls import path
from index.views import index
from index import views
urlpatterns = [
    # 注册
    path(r'signup', views.sigup),
    # 起始页
    path(r'', index),
    # 登陆
    path(r'logIn', views.logIn),
    path(r'test', views.test),
]
