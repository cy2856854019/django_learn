from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home, name='report_fault_home'),
    path('get_trouble/', views.get_trouble, name='get_trouble'),
    re_path('get_trouble/(?P<trouble_id>(\d+)).html', views.get_trouble, name='get_trouble'),
    re_path(r'set_trouble/(?P<trouble_id>(\d+)).html', views.set_trouble, name='set_trouble'),
    re_path(r'del_trouble/(?P<trouble_id>(\d+)).html', views.del_trouble, name='del_trouble'),
]
