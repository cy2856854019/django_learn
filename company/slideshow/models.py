from django.db import models


class SlideShow(models.Model):
    name = models.CharField(
        max_length=32,
        verbose_name='名称',
        null=False,
        default='示例(百度)',
    )

    img = models.ImageField(
        max_length=32,
        verbose_name='图片路径',
        upload_to='img',
        null=False,
        default=r'\img\aa.png',
    )

    target = models.URLField(
        max_length=64,
        verbose_name='目标网址',
        null=False,
        default='http://www.baidu.com/',
    )

    def __str__(self):
        return self.name

    class Meta:
        # 数据库中对应表的名称，不写默认为<app_name>_<model_name>，该处即为slideshow_SlideShow
        # db_table = 'SlideShow'
        # 在admin中显示的SlideShow的别名，如不设置verbose_name_plural，则admin中显示 轮播图s
        verbose_name = '轮播图'
        # 在admin中显示的SlideShow的别名,复数时，此处表明单复数都是一样显示 轮播图
        verbose_name_plural = verbose_name
