from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'home/$', views.home, name='blog_home'),
    re_path(r'home/(?P<classification_id>(\d+)).html', views.home, name='blog_home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]
