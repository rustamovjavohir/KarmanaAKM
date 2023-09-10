from django.contrib import admin

from apps.toponym.models import Toponym


@admin.register(Toponym)
class ToponymAdmin(admin.ModelAdmin):
    list_display = ('name', 'meaning', 'created_by')
    list_filter = ('created_by',)
    search_fields = ('name', 'meaning')
    # prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('slug', 'created_at', 'updated_at')
