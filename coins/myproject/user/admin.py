from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


# Register the Custom User model
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'is_staff', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_password', 'last_password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser', 'first_password', 'last_password'),
        }),
    )
    search_fields = ['email']
    ordering = ['email']

admin.site.register(User, CustomUserAdmin)

admin.site.register(UserProfile)