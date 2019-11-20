from django.urls import path
from ca_redis import views

urlpatterns = [
    path('ca_set/', views.ca_set),
    path('port_set/', views.port_set),
    path('port_get/', views.port_get),
    path('get_available_port/', views.get_available_port),
]
