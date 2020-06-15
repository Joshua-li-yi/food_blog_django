"""food_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from blog import views
urlpatterns = [
    # 写博客
    path(r'writeBlog', views.writeBlog),
    # 保存blog
    path(r'saveDraft', views.save_draft),
    # 发布blog
    path(r'blogDeploy', views.blog_deploy),
    # 看blog
    url('blog-(\d+)', views.see_blog),
    # 修改blog
    url('blogModify-(\d+)', views.blog_modify),
    # 删除blog
    url('blogDelete-(\d+)', views.delete_blog),
]
