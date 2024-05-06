from django.contrib import admin
from .models import ExchangeRule

@admin.register(ExchangeRule)
class ExchangeRuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'text',)
    search_fields = ('title', 'text',)
    list_filter = ('title', 'text',)
