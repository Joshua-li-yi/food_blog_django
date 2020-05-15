from django.urls import path
from index.views import index
from index import views
urlpatterns = [
    path(r'singup/', views.sigup),
    path(r'', index)
]
