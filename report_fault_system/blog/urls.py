from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'home/$', views.home, name='blog_home'),
    re_path(r'home/(?P<classification_id>(\d+)).html', views.home, name='blog_home'),
    re_path('(?P<username>(.+))/myblog/', views.my_blog, name='myblog'),
    path('login/', views.login, name='login'),
    path('login_out/', views.login_out, name='login_out'),
    re_path('open/(?P<user_id>(\d+))/', views.blog_open, name='blog_open'),
    path('register/', views.register, name='register'),
    path('get_check_code/', views.get_check_code, name='get_check_code'),
]
