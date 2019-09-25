from django.db import models


class Terminal(models.Model):
    name = models.CharField(
        max_length=32,
        null=False,
        verbose_name='设备名称',
    )
    device_id = models.CharField(
        max_length=32,
        null=False,
        verbose_name='设备ID',
    )

    available_ports = models.CharField(
        max_length=1024,
        null=False,
        default=str([i for i in range(1, 101)]),
        verbose_name='设备可用端口(1~100)',
    )

    no_available_ports = models.CharField(
        max_length=1024,
        null=False,
        default='[]',
        verbose_name='设备已使用端口',
    )

    class Meta:
        # 数据库中对应表的名称，不写默认为<app_name>_<model_name>，该处即为slideshow_SlideShow
        # db_table = 'SlideShow'
        # 在admin中显示的SlideShow的别名，如不设置verbose_name_plural，则admin中显示 轮播图s
        verbose_name = 'CA机柜'
        # 在admin中显示的SlideShow的别名,复数时，此处表明单复数都是一样显示 轮播图
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
