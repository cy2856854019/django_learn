from django.contrib import admin
from .models import Classification, Direction


class ClassificationAdmin(admin.ModelAdmin):
    list_display = ('name', 'direction')
    list_editable = ('direction',)


admin.site.register(Direction)
admin.site.register(Classification, ClassificationAdmin)
