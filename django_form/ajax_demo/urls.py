from django.urls import path
from ajax_demo import views

urlpatterns = [
    path('ajax1/', views.ajax1),
]
