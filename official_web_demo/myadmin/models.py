from django.db import models


class Direction(models.Model):
    '''
    方向： 自动化 测试 运维 前端
    '''
    name = models.CharField(verbose_name='名称', max_length=32)
    classification = models.ManyToManyField('Classification')

    class Meta:
        db_table = 'Direction'
        verbose_name_plural = '方向(视频方向)'

    def __str__(self):
        return self.name


class Classification(models.Model):
    '''
    分类：Python Linux JavaScript OpenStack Node.js
    '''
    name = models.CharField(verbose_name='名称', max_length=32)

    class Meta:
        db_table = 'Classification'
        verbose_name_plural = '分类(视频分类)'

    def __str__(self):
        return self.name


class Level(models.Model):
    title = models.CharField(max_length=32)

    class Meta:
        verbose_name_plural = '难度'

    def __str__(self):
        return self.title


class Video(models.Model):
    status_choice = (
        (0, '下线'),
        (1, '上线'),
    )

    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)
    level = models.ForeignKey('Level', on_delete=False)
    classification = models.ForeignKey('Classification', null=True, blank=True, on_delete=False)

    weight = models.CharField(verbose_name='权重(按从大到小)', max_length=32)

    title = models.CharField(verbose_name='标题', max_length=32)
    summary = models.CharField(verbose_name='简介', max_length=32)
    img = models.ImageField(verbose_name='图片', upload_to='./static/img/video/')
    href = models.CharField(verbose_name='链接', max_length=256)

    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = '视频'
