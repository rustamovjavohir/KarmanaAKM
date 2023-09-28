from django.contrib import admin
from django.db.models import QuerySet

from apps.monitoring.models import Visitors


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'path', 'created_at', 'updated_at')
    list_display_links = ('ip_address', 'path')
    actions = ('get_extra_datas',)
    ordering = ('-updated_at',)

    def get_extra_datas(self, queryset, *args, **kwargs):
        for obj in args:
            if isinstance(obj, QuerySet):
                for item in obj:
                    item.fill_data()

    get_extra_datas.short_description = 'Дополнительные данные'
