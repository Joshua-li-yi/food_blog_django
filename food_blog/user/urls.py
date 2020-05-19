from django.urls import path
from user import views
urlpatterns = [
    path(r'register', views.register),

]