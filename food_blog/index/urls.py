from django.urls import path
from index.views import index
from index import views
urlpatterns = [
    path(r'signup', views.sigup),
    path(r'', index),
    path(r'logIn', views.logIn),
    path(r'home', views.home),
    path(r'writeblog', views.write_blog),
    path(r'me', views.me),
]
