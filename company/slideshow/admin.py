from django.contrib import admin
from slideshow.models import SlideShow


class SlideShowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'img', 'target')
    list_editable = ('name', 'img', 'target')


admin.site.site_header = '企业官网管理'
admin.site.site_title = '扬眉企业官网管理'
admin.site.register(SlideShow, SlideShowAdmin)
