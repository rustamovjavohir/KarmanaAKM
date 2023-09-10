from django.contrib import admin
from apps.writers.models import Writers


@admin.register(Writers)
class WritersAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at', 'updated_at')
    readonly_fields = ('slug', 'created_at', 'updated_at')
