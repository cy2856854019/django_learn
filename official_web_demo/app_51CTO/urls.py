from django.contrib import admin
from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'video-(?P<classification_id>(\d+))-(?P<level_id>(\d+)).html', views.video),
]
