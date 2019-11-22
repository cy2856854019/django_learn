from django.db import models


# 用户表
class User(models.Model):
    username = models.CharField(
        max_length=64,
        null=False,
        verbose_name='用户名',
    )

    psw = models.CharField(
        max_length=64,
        null=False,
        verbose_name='密码',
    )

    email = models.CharField(
        max_length=64,
        null=False,
        verbose_name='邮箱',
    )


# 博客表
class Blog(models.Model):
    suffix = models.CharField(
        max_length=64,
        null=False,
        verbose_name='标语',
    )
    theme = models.CharField(
        max_length=64,
        null=False,
        verbose_name='主题',
    )
    title = models.CharField(
        max_length=64,
        null=False,
        verbose_name='标题',
    )
    summary = models.CharField(
        max_length=1024,
        null=True,
        verbose_name='简介',
    )
    user = models.OneToOneField(
        'User',
        verbose_name='用户ID',
        on_delete=False,
        null=False,
    )


# 互粉表
class Fans(models.Model):
    user = models.ForeignKey(
        'User',
        verbose_name='用户ID',
        on_delete=False,
        null=False,
    )
    fan = models.ForeignKey(
        'User',
        verbose_name='粉丝ID',
        on_delete=False,
        null=True,
    )
