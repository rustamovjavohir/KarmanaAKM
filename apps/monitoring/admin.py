from django.contrib import admin
from apps.monitoring.models import Visitors


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'user_agent', 'path', 'created_at', 'updated_at')
