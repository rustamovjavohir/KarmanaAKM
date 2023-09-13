from django.contrib import admin
from apps.events.models import Events


# Register your models here.


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'description', 'date', 'created_by')
    list_filter = ('name', 'slug', 'description', 'date', 'created_by')
    search_fields = ('name', 'slug', 'description', 'date', 'created_by')
    empty_value_display = '-пусто-'
    readonly_fields = ('slug', 'created_at', 'updated_at')
