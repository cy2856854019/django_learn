from django.urls import path
from manage_form.views import student
from manage_form.views import teacher
from manage_form.views import classes

urlpatterns = [
    path('class/get/', classes.get),
    path('class/add/', classes.add),

    path('teacher/get/', teacher.get),
    path('teacher/add/', teacher.add),
    path('teacher/edit/', teacher.edit),
    path('teacher/delete/', teacher.delete),
]
