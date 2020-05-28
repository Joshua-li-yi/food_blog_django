from django.urls import path
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
]