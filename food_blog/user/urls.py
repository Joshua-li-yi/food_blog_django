from django.urls import path
from user import views
urlpatterns = [
    path(r'register', views.register),
    path(r'logIn', views.logIn),
    path(r'home', views.home),
    path(r'me', views.me),
    path(r'writeBlog', views.writeBlog),
]