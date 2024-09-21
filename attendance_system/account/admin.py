from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.conf import settings

''' User admin'''
class UserModelAdmin(BaseUserAdmin):
    list_display = ('id', 'email', 'first_name','last_name','is_admin','is_superuser')
    list_filter = ('is_admin',)
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
        ('Role', {'fields': ('role',)}),
        ('Permissions', {'fields': ('is_admin','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name','last_name','email','password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email', 'id')

admin.site.register(User, UserModelAdmin)

