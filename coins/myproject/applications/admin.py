from django.contrib import admin
from .models import CurrencyRequest

@admin.register(CurrencyRequest)
class CurrencyRequestAdmin(admin.ModelAdmin):
    list_display = ('number', 'date', 'direction', 'currency', 'status')
    list_filter = ('currency', 'status')
    search_fields = ('number', 'direction')
    date_hierarchy = 'date'
