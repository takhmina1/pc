from django.contrib import admin
from .models import KYCAMLCheck


class KYCAMLCheckAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'text')

    fieldsets = (
        (None, {
            'fields': ('title', 'text')
        }),
    )
    ordering = ('title',)


admin.site.register(KYCAMLCheck, KYCAMLCheckAdmin)
