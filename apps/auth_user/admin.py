from django.contrib import admin
from apps.auth_user.models import User, UserReader
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'date_joined')
    search_fields = ('username', 'email')
    ordering = ('-date_joined',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Персональная информация', {'fields': ('full_name', 'email', 'phone_number', 'birthday', 'profile_photo')}),
        ('Права доступа', {'fields': ('is_reader', 'is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )


@admin.register(UserReader)
class UserReaderAdmin(admin.ModelAdmin):
    list_display = ('user', 'passport', 'address', 'date_joined')
    search_fields = ('user', 'passport', 'address')
    readonly_fields = ('date_joined',)

    def date_joined(self, obj):
        return obj.user.date_joined

    date_joined.short_description = 'Дата регистрации'
