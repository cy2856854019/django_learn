from django.contrib import admin
from .models import Classification, Direction, Trouble, User, Role, Permission, Action, PermissionToAction, PermissionToActionToRole, Menu


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction')
    list_editable = ('direction',)


admin.site.register(Direction)
admin.site.register(Classification, ClassificationAdmin)
admin.site.register(Trouble)

# 权限管理
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Permission)
admin.site.register(Action)
admin.site.register(PermissionToAction)
admin.site.register(PermissionToActionToRole)
admin.site.register(Menu)
