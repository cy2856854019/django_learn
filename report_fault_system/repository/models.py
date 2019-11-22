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

    class Meta:
        db_table = 'User'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


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

    class Meta:
        db_table = 'Blog'
        verbose_name = '博客'
        verbose_name_plural = verbose_name


# 互粉表
class Fan(models.Model):
    user = models.ForeignKey(
        'User',
        verbose_name='用户ID',
        on_delete=False,
        null=False,
        related_name='fan_user',
    )
    fan = models.ForeignKey(
        'User',
        verbose_name='粉丝ID',
        on_delete=False,
        null=True,
        related_name='fan_fan',
    )

    class Meta:
        db_table = 'Fan'
        verbose_name = '粉丝'
        verbose_name_plural = verbose_name
