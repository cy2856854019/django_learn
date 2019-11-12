from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'video-(?P<classification_id>(\d+))-(?P<level_id>(\d+))-(?P<status>([0-2])).html',
            views.video),
    re_path(r'video2-(?P<direction_id>(\d+))-(?P<classification_id>(\d+))-(?P<level_id>(\d+))-(?P<status>([0-2])).html',
            views.video2),
    path('get_pdf', views.get_pdf)
]
