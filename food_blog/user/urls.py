from django.urls import path
from user import views
urlpatterns = [
    path(r'register', views.register),
    path(r'login', views.login),
    path(r'home', views.home),
]