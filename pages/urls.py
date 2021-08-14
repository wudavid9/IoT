# _*_ coding: UTF-8 _*_
# Copy rights belong to : JustIt Co., Ltd.
# File Author: David Wu
# Dev Date: 2021/8/14 22:40
# File name: urls.py
from django.urls import path
from .views import homePageView
urlpatterns = [
    path('',homePageView, name='home'),
]