from django.urls import path
from ca_redis import views

urlpatterns = [
    path('set/', views.ca_set),
    path('get_available_port/', views.get_available_port),
]
