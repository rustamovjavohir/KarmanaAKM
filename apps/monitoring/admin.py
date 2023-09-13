from django.contrib import admin
from apps.monitoring.models import Visitors


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'path', 'created_at', 'updated_at')
    list_display_links = ('ip_address', 'path')
    actions = ('get_extra_datas',)
    ordering = ('-updated_at',)

    def get_extra_datas(self, queryset):
        for obj in queryset:
            obj.fill_data()

    get_extra_datas.short_description = 'Дополнительные данные'
