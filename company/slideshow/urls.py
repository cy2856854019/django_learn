from django.urls import path
from slideshow import views


urlpatterns = [
    path('show/', views.show),
]
