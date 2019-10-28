from django.contrib import admin
from .models import Direction, Classification, Level, Video


class VideoAdmin(admin.ModelAdmin):
    # 在admin后台中显示的字段，不可加上多对多关系
    list_display = ('id', 'status', 'title', 'summary', 'img', 'href', 'level', 'classification')


admin.site.register(Direction)
admin.site.register(Classification)
admin.site.register(Level)
admin.site.register(Video, VideoAdmin)
