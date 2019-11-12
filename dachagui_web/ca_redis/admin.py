from django.contrib import admin
from ca_redis.models import Terminal as ca_redis_Terminal


class TermianlAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'device_id', 'available_ports', 'no_available_ports')
    list_editable = ('name', 'device_id',)
    ordering = ('id',)


admin.site.site_header = 'CA机柜配置'
admin.site.site_title = 'CA机柜配置'
admin.site.register(ca_redis_Terminal, TermianlAdmin)
