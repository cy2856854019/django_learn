from django.urls import path, re_path
from . import views

urlpatterns = [
    path('home/', views.home, name='report_fault_home'),
]
