from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=32)
    teacher = models.ManyToManyField('Teacher')


class Teacher(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField(null=True)
    gender = models.BooleanField(null=True)  # 不可为空的bool


class Student(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()  # 不可为空的bool
    # gender = models.NullBooleanField  # 可为空的bool
    Class = models.ForeignKey('Class', on_delete=True)
