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

    email = models.EmailField(
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
        null=True,
        verbose_name='标语',
    )
    theme = models.CharField(
        max_length=64,
        null=True,
        verbose_name='主题',
    )
    title = models.CharField(
        max_length=64,
        null=True,
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
        # related_name='user',
    )

    tag = models.ManyToManyField(
        'Tag'
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


# 文章信息表
class Article(models.Model):
    title = models.CharField(
        verbose_name='标题',
        max_length=64,
        null=False,
    )
    abstract = models.CharField(
        verbose_name='摘要',
        max_length=1024,
        null=False,
    )
    create_or_update_date = models.DateTimeField(
        verbose_name='创建(更新)时间',
        null=False,
        auto_now=True,
    )

    content = models.ForeignKey(
        'ArticleContent',
        verbose_name='文章内容',
        on_delete=True,
        null=False
    )

    blog = models.ForeignKey(
        'Blog',
        verbose_name='博客ID',
        on_delete=False,
    )

    tag = models.ManyToManyField(
        'Tag',
    )

    class Meta:
        db_table = 'Article'
        verbose_name = '文章信息'
        verbose_name_plural = verbose_name


# 文章内容表
class ArticleContent(models.Model):
    content = models.TextField(
        verbose_name='文章内容',
        null=False,
    )

    class Meta:
        db_table = 'ArticleContent'
        verbose_name = '文章内容'
        verbose_name_plural = verbose_name


# 标签表
class Tag(models.Model):
    tag = models.CharField(
        verbose_name='标签',
        max_length=64,
        null=False,
    )

    class Meta:
        db_table = 'Tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Direction(models.Model):
    '''
    方向：
    '''
    name = models.CharField(verbose_name='名称', max_length=32)

    # classification = models.ForeignKey('Classification', on_delete=True)

    class Meta:
        db_table = 'Direction'
        verbose_name_plural = '网站方向'

    def __str__(self):
        return self.name


class Classification(models.Model):
    '''
    分类：
    '''
    name = models.CharField(verbose_name='名称', max_length=32)
    direction = models.ForeignKey('Direction', on_delete=True, default='1', related_name='direction')

    class Meta:
        db_table = 'Classification'
        verbose_name_plural = '分类'

    def __str__(self):
        return self.name


# 报障单
class Trouble(models.Model):
    title = models.CharField(max_length=32)
    detail = models.TextField()
    user = models.ForeignKey('User', on_delete=False, related_name='u')
    ctime = models.DateTimeField()

    status_choice = (
        (1, '未处理'),
        (2, '处理中'),
        (3, '已处理'),
    )
    status = models.IntegerField(choices=status_choice, default=1)
    processor = models.ForeignKey('User', related_name='p', on_delete=False, null=True)
    solution = models.TextField(null=True)
    ptime = models.DateTimeField(null=True)

    evaluation_choice = (
        (1, '不满意'),
        (2, '一般'),
        (3, '满意'),
        (4, '非常满意'),
    )
    evaluation = models.IntegerField(choices=evaluation_choice, null=True)

    class Meta:
        db_table = 'Trouble'

    def __str__(self):
        return self.title


# RBAC role based access control
# 角色
class Role(models.Model):
    caption = models.CharField(max_length=32)
    user = models.ManyToManyField('User')

    class Meta:
        db_table = 'Role'
        verbose_name_plural = '角色'

    def __str__(self):
        return self.caption


# 权限
class Permission(models.Model):
    # http://127.0.0.1/report_fault/order.html 订单管理
    # http://127.0.0.1/report_fault/user.html 用户管理
    # http://127.0.0.1/report_fault/permission.html 权限管理
    caption = models.CharField(max_length=32)
    url = models.CharField(max_length=64)

    class Meta:
        db_table = 'Permission'
        verbose_name_plural = '权限'

    def __str__(self):
        return '%s-%s' % (self.caption, self.url)


# 操作
class Action(models.Model):
    # post 增
    # delete 删
    # put 改
    # get 查
    caption = models.CharField(max_length=32)
    action = models.CharField(max_length=32)

    class Meta:
        db_table = 'Action'
        verbose_name_plural = '操作'

    def __str__(self):
        return '%s-%s' % (self.caption, self.action)


# 权限与操作 多对多关联
class PermissionToAction(models.Model):
    # http://127.0.0.1/report_fault/order.html?action=post 订单管理（增）
    # http://127.0.0.1/report_fault/user.html?action=delete 用户管理（删）
    # http://127.0.0.1/report_fault/permission.html?action=put 权限管理(改)
    url = models.ForeignKey('Permission', on_delete=False)
    action = models.ForeignKey('Action', on_delete=False)
    menu = models.ForeignKey('Menu', on_delete=False, null=True)

    class Meta:
        db_table = 'PermissionToAction'
        verbose_name_plural = '权限To操作'

    def __str__(self):
        return '%s-%s: %s?action=%s' % (self.url.caption, self.action.caption, self.url.url, self.action.action)


# 权限与角色多对多
class PermissionToActionToRole(models.Model):
    role = models.ForeignKey('Role', on_delete=False)
    permissionToAction = models.ForeignKey('PermissionToAction', on_delete=False)

    class Meta:
        db_table = 'PermissionToActionToRole'
        verbose_name_plural = '权限To操作To角色'

    def __str__(self):
        return '%s: %s' % (self.role.caption, self.permissionToAction)


# 菜单
class Menu(models.Model):
    caption = models.CharField(max_length=32)
    parent = models.ForeignKey('self', null=True, related_name='p', on_delete=False)

    class Meta:
        db_table = 'Menu'
        verbose_name_plural = '菜单'

    def __str__(self):
        return self.caption
